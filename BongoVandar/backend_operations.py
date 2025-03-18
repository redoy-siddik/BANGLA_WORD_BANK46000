import os
import django
from django.db.models import Q, Count

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BongoVandar.settings')
django.setup()

from vocabulary.models import Varna, Source, Type, Word

# Sample data for creating words (including a duplicate for testing)
SAMPLE_WORDS = [
    {
        "varna": "অ",
        "source": "তৎসম",
        "type": "বিশেষ্য",
        "root_word": "অমৃত",
        "details": {
            "label": "সাধারণ বিশেষ্য",
            "origin": "সংস্কৃত",
            "example": "দেবতারা অমৃত পান করেন।",
            "synonyms": ["পানীয়", "অমৃতরস"]
        }
    },
    {
        "varna": "অ",
        "source": "তৎসম",
        "type": "বিশেষ্য",
        "root_word": "অমৃত",  # Duplicate entry
        "details": {
            "label": "সাধারণ বিশেষ্য",
            "origin": "সংস্কৃত",
            "example": "অমৃত একটি পবিত্র পানীয়।",
            "synonyms": ["পানীয়"]
        }
    },
    {
        "varna": "অ",
        "source": "তৎসম",
        "type": "ক্রিয়া",
        "root_word": "অর্জন",
        "details": {
            "label": "সকর্মক ক্রিয়া",
            "origin": "সংস্কৃত",
            "example": "তিনি অনেক সম্পদ অর্জন করেছেন।",
            "synonyms": ["প্রাপ্ত করা", "লাভ করা"],
            "nature": "সকর্মক",
            "tense": {
                "past": "অর্জন করেছিল",
                "present": "অর্জন করে",
                "future": "অর্জন করবে"
            }
        }
    }
]

def create_words():
    """Create words in the database from SAMPLE_WORDS."""
    print("=== Creating Words ===")
    for word_data in SAMPLE_WORDS:
        varna, _ = Varna.objects.get_or_create(varna_name=word_data["varna"])
        source, _ = Source.objects.get_or_create(source_name=word_data["source"])
        word_type, _ = Type.objects.get_or_create(type_name=word_data["type"])

        # Allow duplicates for testing (removed the exists check)
        word = Word(
            varna=varna,
            source=source,
            type=word_type,
            root_word=word_data["root_word"],
            details=word_data["details"]
        )
        word.save()
        print(f"Created: {word.root_word} (ID: {word.id})")

def delete_word():
    """Delete a word by root_word or ID."""
    print("=== Deleting Word ===")
    choice = input("Delete by (1) root_word or (2) ID? Enter 1 or 2: ")
    if choice == "1":
        root_word = input("Enter root word to delete: ")
        words = Word.objects.filter(root_word=root_word)
    elif choice == "2":
        word_id = input("Enter word ID to delete: ")
        words = Word.objects.filter(id=word_id)
    else:
        print("Invalid choice!")
        return

    if words.exists():
        for word in words:
            print(f"Deleting: {word.root_word} (ID: {word.id})")
            word.delete()
    else:
        print("No matching word found to delete")

def search_words():
    """Search words by root_word, varna, source, type, or details."""
    print("=== Searching Words ===")
    query = input("Enter search query (e.g., word, varna, source): ")
    results = Word.objects.filter(
        Q(root_word__icontains=query) |
        Q(varna__varna_name__icontains=query) |
        Q(source__source_name__icontains=query) |
        Q(type__type_name__icontains=query) |
        Q(details__label__icontains=query) |
        Q(details__origin__icontains=query) |
        Q(details__example__icontains=query)
    ).distinct()

    if results:
        for word in results:
            print(f"Found: {word.root_word} (Varna: {word.varna}, Source: {word.source}, Type: {word.type})")
            print(f"  Details: {word.details}")
    else:
        print(f"No results for query: {query}")

def find_duplicates():
    """Find duplicate words and offer to delete them."""
    print("=== Finding Duplicates ===")
    duplicates = Word.objects.values('root_word', 'varna', 'source', 'type').annotate(
        count=Count('id')
    ).filter(count__gt=1)

    if duplicates:
        for dup in duplicates:
            words = Word.objects.filter(
                root_word=dup['root_word'],
                varna=dup['varna'],
                source=dup['source'],
                type=dup['type']
            )
            print(f"Duplicate found: {dup['root_word']} (Count: {dup['count']})")
            for word in words:
                print(f"  ID: {word.id}, Details: {word.details}")

            # Prompt to delete duplicates
            delete_choice = input(f"Do you want to delete duplicates for '{dup['root_word']}'? (y/n): ").lower()
            if delete_choice == 'y':
                print("Which duplicates to delete?")
                for word in words:
                    print(f"  ID: {word.id}, Details: {word.details}")
                ids_to_delete = input("Enter IDs to delete (comma-separated, or 'all' for all but one): ").strip()
                
                if ids_to_delete.lower() == 'all':
                    # Keep the first word, delete the rest
                    for word in words[1:]:
                        print(f"Deleting: {word.root_word} (ID: {word.id})")
                        word.delete()
                else:
                    try:
                        id_list = [int(id.strip()) for id in ids_to_delete.split(',')]
                        for word in words:
                            if word.id in id_list:
                                print(f"Deleting: {word.root_word} (ID: {word.id})")
                                word.delete()
                    except ValueError:
                        print("Invalid ID format! Use numbers separated by commas.")
    else:
        print("No duplicates found")

def menu():
    """Display menu and handle user choice."""
    while True:
        print("\n=== BANGLA_WORD_BANK Backend Operations ===")
        print("1. Create Words")
        print("2. Delete Word")
        print("3. Search Words")
        print("4. Find Duplicates")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            create_words()
        elif choice == "2":
            delete_word()
        elif choice == "3":
            search_words()
        elif choice == "4":
            find_duplicates()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

def main():
    """Run the menu-driven backend operations."""
    menu()

if __name__ == "__main__":
    main()