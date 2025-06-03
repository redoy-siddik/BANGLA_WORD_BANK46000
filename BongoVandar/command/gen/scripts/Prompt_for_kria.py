import os

# আউটপুট ডিরেক্টরি
output_directory = r"E:\SoftwareProject\shabdabhandar\BANGLA_WORD_BANK460000\BongoVandar\command\gen\output"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# TXT ফাইলের নাম
txt_file = os.path.join(output_directory, "ক্রিয়া.txt")

# কনফিগারেশন
main_category = "দেশীয়"
sub_category = "ক্রিয়া"
base_letter = "খ"
num_entries = 11
label_text = f"কোন প্রকার {sub_category}"

# TXT ফাইলে লিখছি
with open(txt_file, "w", encoding="utf-8") as txtfile:
    # প্রথমে টেমপ্লেট টেক্সট লাইনটি লিখে দিচ্ছি
    txtfile.write(f"টেমপ্লেট টি ব্যবহার করে CSV ফরম্যাটে, {base_letter} - দিয়ে শুরু হয় এমন মোট ৫০ টি {sub_category} বাচক শব্দ দাও\n\n")
    
    # শিরোনাম লাইন
    header = "লেবেল,মূল,সমার্থক ১,সমার্থক ২,সমার্থক ৩,সমার্থক ৪,সমার্থক ৫,উৎপত্তি,উদাহরণ,প্রকৃতি,কাল - অতীত,কাল - বর্তমান,কাল - ভবিষ্যৎ"
    txtfile.write(header + "\n")
    
    for i in range(num_entries):
        main_word = f"ক্রিয়া_মূল"
        synonyms = [f"ক্রিয়া_সমার্থক {j+1}" for j in range(5)]
        
        # CSV ফরম্যাটে ১টি লাইন তৈরি করা
        line = f"{label_text},{main_word},{synonyms[0]},{synonyms[1]},{synonyms[2]},{synonyms[3]},{synonyms[4]}," \
               f"{main_word} শব্দটির উৎপত্তি বর্ণনা," \
               f"এই বাক্যে উদাহরণ হিসেবে {main_word} যুক্ত করবে ।," \
               "ক্রিয়া প্রকৃতি," \
               f"{main_word} - অতীত," \
               f"{main_word} - বর্তমান," \
               f"{main_word} - ভবিষ্যৎ"
        
        txtfile.write(line + "\n")

print(f"TXT file successfully created at: {txt_file}")
