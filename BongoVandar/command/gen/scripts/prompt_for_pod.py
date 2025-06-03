import os

# আউটপুট ডিরেক্টরি
output_directory = r"E:\SoftwareProject\shabdabhandar\BANGLA_WORD_BANK460000\BongoVandar\command\gen\output"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# TXT ফাইলের নাম
txt_file = os.path.join(output_directory, "বিশেষ্য.txt")

# কনফিগারেশন
main_category = "দেশীয়"
sub_category = "বিশেষ্য"
base_letter = "খ"
label_text = f"কোন প্রকার {sub_category} পদের শব্দ"
num_entries = 50

# TXT ফাইলে লিখছি
with open(txt_file, "w", encoding="utf-8") as txtfile:
    for i in range(num_entries):
        main_word = f"{base_letter} শব্দ"
        synonyms = [f"{main_word} সমার্থক " for j in range(5)]

        entry = f"""লেবেল: {label_text}
মূল: {main_word}
সমার্থক ১: {synonyms[0]}
সমার্থক ২: {synonyms[1]}
সমার্থক ৩: {synonyms[2]}
সমার্থক ৪: {synonyms[3]}
সমার্থক ৫: {synonyms[4]}
উৎপত্তি: {main_word} শব্দটির উৎপত্তি লিখবে
উদাহরণ: এই বাক্যে উদাহরণ হিসেবে {main_word} যুক্ত করবে ।

"""
        txtfile.write(entry)

    # অতিরিক্ত লাইন যুক্ত করছি
    txtfile.write("টেমপ্লেট টি  ব্যবহার  করে CSV ফরম্যাটে, খ - দিয়ে শুরু হয় এমন  মোট ৫০ টি {sub_category} বাচক শব্দ দাও\n")

print(f"✅ TXT file successfully created at: {txt_file}")
