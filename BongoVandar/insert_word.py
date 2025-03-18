import os
import django
import json

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BongoVandar.settings')
django.setup()

from vocabulary.models import Varna, Source, Type, Word

def insert_data_from_json():
    # Load JSON data from file
    with open('json/vocabulary.json', 'r', encoding='utf-8') as file:
        vocabulary_data = json.load(file)

    # Extract vocabulary data
    vocabulary = vocabulary_data['শব্দভাণ্ডার']

    # Iterate through the JSON structure and insert data
    for varna_name, sources in vocabulary.items():
        # Get or create Varna object
        varna, _ = Varna.objects.get_or_create(varna_name=varna_name)
        print(f"Processing varna: {varna_name}")

        for source_name, types in sources.items():
            # Get or create Source object
            source, _ = Source.objects.get_or_create(source_name=source_name)
            print(f"  Source: {source_name}")

            for type_name, words in types.items():
                # Get or create Type object
                type_obj, _ = Type.objects.get_or_create(type_name=type_name)
                print(f"    Type: {type_name}")

                word_objects = []
                for word_data in words:
                    # Map Bengali keys to English for consistency with the Django app
                    details = {
                        'label': word_data.get('লেবেল', ''),
                        'origin': word_data.get('উৎপত্তি', ''),
                        'example': word_data.get('উদাহরণ', ''),
                        'synonyms': word_data.get('সমার্থক', [])
                    }
                    # Add verb-specific fields if type is 'ক্রিয়া'
                    if type_name == 'ক্রিয়া':
                        details['nature'] = word_data.get('প্রকৃতি', '')
                        tense = word_data.get('কাল', {})
                        details['tense'] = {
                            'past': tense.get('অতীত', ''),
                            'present': tense.get('বর্তমান', ''),
                            'future': tense.get('ভবিষ্যৎ', '')
                        }
                    # Create Word object (to be bulk inserted later)
                    word_objects.append(Word(
                        varna=varna,
                        source=source,
                        type=type_obj,
                        root_word=word_data['মূল'],
                        details=details
                    ))
                # Bulk create all words for this type
                if word_objects:
                    Word.objects.bulk_create(word_objects)
                    print(f"      Inserted {len(word_objects)} words")
                else:
                    print("      No words to insert")

    print("Data insertion completed!")

if __name__ == "__main__":
    insert_data_from_json()