import os
import django
import json
from django.db import connection

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BongoVandar.settings')
django.setup()

from vocabulary.models import Word

def resequence_word_ids():
    """Resequence the id values of Word model to remove gaps."""
    print("=== Resequencing Word IDs ===")
    
    # Get all words ordered by current id
    words = Word.objects.all().order_by('id')
    if not words.exists():
        print("No words to resequence.")
        return

    # Start a transaction to update IDs
    with connection.cursor() as cursor:
        # Create a temporary table with the same structure as vocabulary_word
        cursor.execute("CREATE TABLE temp_word AS SELECT * FROM vocabulary_word WITH NO DATA;")
        
        # Insert words with new IDs
        new_id = 1
        for word in words:
            # Convert details dict to JSON string
            details_json = json.dumps(word.details, ensure_ascii=False)
            cursor.execute(
                """
                INSERT INTO temp_word (id, varna_id, source_id, type_id, root_word, details)
                VALUES (%s, %s, %s, %s, %s, %s);
                """,
                [new_id, word.varna_id, word.source_id, word.type_id, word.root_word, details_json]
            )
            print(f"Reassigned: {word.root_word} from ID {word.id} to {new_id}")
            new_id += 1

        # Drop the old table and replace it with the new one
        cursor.execute("DROP TABLE vocabulary_word;")
        cursor.execute("ALTER TABLE temp_word RENAME TO vocabulary_word;")
        
        # Recreate primary key and foreign key constraints
        cursor.execute("ALTER TABLE vocabulary_word ADD PRIMARY KEY (id);")
        cursor.execute("""
            ALTER TABLE vocabulary_word
            ADD CONSTRAINT vocabulary_word_varna_id_fkey
            FOREIGN KEY (varna_id) REFERENCES vocabulary_varna(id) ON DELETE CASCADE;
        """)
        cursor.execute("""
            ALTER TABLE vocabulary_word
            ADD CONSTRAINT vocabulary_word_source_id_fkey
            FOREIGN KEY (source_id) REFERENCES vocabulary_source(id) ON DELETE CASCADE;
        """)
        cursor.execute("""
            ALTER TABLE vocabulary_word
            ADD CONSTRAINT vocabulary_word_type_id_fkey
            FOREIGN KEY (type_id) REFERENCES vocabulary_type(id) ON DELETE CASCADE;
        """)

        # Reset the sequence for future inserts
        cursor.execute("SELECT setval('vocabulary_word_id_seq', (SELECT MAX(id) FROM vocabulary_word));")

    print("ID resequencing completed!")

if __name__ == "__main__":
    resequence_word_ids()