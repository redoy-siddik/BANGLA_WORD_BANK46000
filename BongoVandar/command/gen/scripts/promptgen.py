import json
import os

# আউটপুট ডিরেক্টরি যেখানে ফাইল তৈরি করা হবে
output_directory = r"E:\SoftwareProject\shabdabhandar\BANGLA_WORD_BANK460000\BongoVandar\command\gen\output"

# যদি ডিরেক্টরি না থেকে থাকে, তাহলে তৈরি কর
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# পুরো ফাইল পাথ নির্দিষ্ট করা হচ্ছে (এখন output.txt নামে)
output_file = os.path.join(output_directory, "output.txt")

# ব্যবহারযোগ্য কনফিগারেশন:
main_category = "তদ্ভব"           # আপনি চাইলে এখানে "তদ্ভব" বা অন্য কোন মান লিখতে পারেন।
sub_category = "বিশেষ্য"           # প্রয়োজন অনুযায়ী পরিবর্তন করুন।
label_text = f"কোন প্রকার {sub_category}"
base_letter = "খ"                # মূল শব্দের শুরুতে এই অক্ষরটি ব্যবহার হবে।
num_entries = 1                 # এখানে ১টি এন্ট্রি তৈরি করা হচ্ছে (আপনি চাইলে ৫০টি করতে পারেন)

entries = []

for i in range(num_entries):
    # প্রতিটি এন্ট্রির জন্য ডামি 'মূল' শব্দ
    main_word = "মূল শব্দ"
    # ৫টি সমার্থক শব্দ (আপনি চাইলে এগুলো পরিবর্তন বা সংশোধন করতে পারেন)
    synonyms = [f"সমার্থক শব্দ {j+1}" for j in range(5)]
    
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

# নির্দেশনা যুক্ত করা হচ্ছে
instructions = {
    "ডাটার উপর ভিত্তি করে যা করবে ": f"{base_letter} দিয়ে এরকম আরো ৫০ টি সতন্ত্র {main_category} হবে এবং  একই সাথে  {sub_category} বাচকও হবে এমন শব্দের  জন্য আলাদা ভাবে JSON ফাইল তৈরি করে দাও"
}

# উভয় JSON অবজেক্ট (ডাটা ও নির্দেশনা) লিখে সংযুক্ত করা হচ্ছে
with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write("ডাটা:\n")
    json.dump(data, outfile, ensure_ascii=False, indent=4)
    outfile.write("\n\nনির্দেশনা:\n")
    json.dump(instructions, outfile, ensure_ascii=False, indent=4)

print(f"{output_file} The file has been created successfully!")