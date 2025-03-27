import json
import os

# আউটপুট ডিরেক্টরি যেখানে JSON ফাইলটি তৈরি হবে
output_directory = r"E:\SoftwareProject\shabdabhandar\BANGLA_WORD_BANK460000\BongoVandar\command\gen\json"

# যদি ডিরেক্টরি না থাকে, তাহলে তৈরি কর
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# JSON ফাইলের সম্পূর্ণ পাথ (উদাহরণস্বরূপ output_kria.json)
output_file = os.path.join(output_directory, "output_kria.json")

# কনফিগারেশন: কতটি এন্ট্রি তৈরি করতে চান
num_entries = 1

entries = []

for i in range(num_entries):
    # প্রতিটি এন্ট্রির জন্য ডামি 'মূল' শব্দ তৈরি করা হচ্ছে
    main_word = f"ক্রিয়া_মূল"
    # ৫টি সমার্থক শব্দের জন্য ডামি ডাটা (আপনি চাইলে এদের পরিবর্তন করতে পারেন)
    synonyms = [f"ক্রিয়া_সমার্থক {j+1}" for j in range(5)]
    
    # প্রতিটি "ক্রিয়া" এন্ট্রির স্ট্রাকচার
    entry = {
        "লেবেল": f"ক্রিয়া লেবেল {i+1}",  # প্রয়োজনে পরিবর্তন করুন
        "মূল": main_word,
        "সমার্থক": synonyms,
        "উৎপত্তি": f"{main_word} শব্দটির উৎপত্তি বর্ণনা",
        "উদাহরণ": f"এই বাক্যে {main_word} ব্যবহৃত হয়েছে।",
        "প্রকৃতি": f"ক্রিয়া প্রকৃতি ",
        "কাল": {
            "অতীত": f"{main_word} - অতীত",
            "বর্তমান": f"{main_word} - বর্তমান",
            "ভবিষ্যৎ": f"{main_word} - ভবিষ্যৎ"
        }
    }
    entries.append(entry)

# চূড়ান্ত JSON ডাটা স্ট্রাকচার প্রস্তুত করা হলো:
data = {
    "ক্রিয়া": entries
}

# JSON ফাইলটি নির্দিষ্ট ফোল্ডারে লেখা হচ্ছে
with open(output_file, "w", encoding="utf-8") as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)

print(f"JSON file successfully created at: {output_file}")