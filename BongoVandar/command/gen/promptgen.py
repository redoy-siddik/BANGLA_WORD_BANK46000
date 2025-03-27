import json
import os

# আউটপুট ডিরেক্টরি যেখানে ফাইল তৈরি করা হবে
output_directory = r"E:\SoftwareProject\shabdabhandar\BANGLA_WORD_BANK460000\BongoVandar\command\gen\json"

# যদি ডিরেক্টরি না থেকে থাকে, তাহলে তৈরি কর
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# পুরো ফাইল পাথ নির্দিষ্ট করা হচ্ছে
output_file = os.path.join(output_directory, "output.json")

# ব্যবহারযোগ্য কনফিগারেশন:
main_category = "তৎসম"           # আপনি চাইলে এখানে "তদ্ভব" বা অন্য কোন মান লিখতে পারেন।
sub_category = "বিশেষণ"           # প্রয়োজন অনুযায়ী পরিবর্তন করুন।
label_text = "গুণবাচক বিশেষণ/পরিমাণবাচক বিশেষণ/সংখ্যাবাচক বিশেষণ/সম্পর্কবাচক বিশেষণ/অবিশেষণবাচক বিশেষণ/সমাসবদ্ধ বিশেষণ"
base_letter = "ক"                # মূল শব্দের শুরুতে এই অক্ষরটি ব্যবহার হবে।
num_entries = 1                 # ৫০টি এন্ট্রি তৈরি হবে।

entries = []

for i in range(num_entries):
    # প্রতিটি এন্ট্রির জন্য ডামি 'মূল' শব্দ
    main_word = f"{"মূল শব্দ"}"
    # ৫টি সমার্থক শব্দ (আপনি চাইলে এগুলো পরিবর্তন বা সংশোধন করতে পারেন)
    synonyms = [f"{"সমার্থক শব্দ"} {j+1}" for j in range(5)]
    
    word_entry = {
        "লেবেল": label_text,
        "মূল": main_word,
        "সমার্থক": synonyms,
        "উৎপত্তি": "শব্দটির উৎপত্তি লিখবে ",
        "উদাহরণ": f"এই বাক্যে উদাহরণ হিসেবে {main_word} যুক্ত করবে ।"
    }
    entries.append(word_entry)

# চূড়ান্ত JSON স্ট্রাকচারটি তৈরি করা হলো
data = {
    main_category: {
        sub_category: entries
    }
}

# নির্দিষ্ট ফোল্ডারে JSON ফাইলটি লেখা হচ্ছে
with open(output_file, "w", encoding="utf-8") as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)

print(f"{output_file} The file has been created successfully!")