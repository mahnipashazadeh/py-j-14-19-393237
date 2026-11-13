print("========== QUIZ GAME ==========")

# سوالات بازی
questions = {
    "1": {
        "name": "سوالات علمی",
        "questions": [
            ("پایتخت ایران کجاست؟", "تهران"),
            ("بزرگ‌ترین سیاره منظومه شمسی چیست؟", "مشتری"),
            ("نماد شیمیایی آب چیست؟", "h2o")
        ]
    },
    "2": {
        "name": "سوالات کامپیوتری",
        "questions": [
            ("زبان برنامه‌نویسی مورد استفاده در این پروژه چیست؟", "python"),
            ("CPU مخفف چیست؟", "central processing unit"),
            ("عدد 1 در مبنای دودویی چه معنایی دارد؟", "یک")
        ]
    },
    "3": {
        "name": "سوالات عمومی",
        "questions": [
            ("تعداد روزهای هفته چند تاست؟", "7"),
            ("رنگ حاصل از ترکیب آبی و زرد چیست؟", "سبز"),
            ("بزرگ‌ترین اقیانوس جهان کدام است؟", "اقیانوس آرام")
        ]
    }
}

print("\nلطفا نوع سوالات را انتخاب کنید:")
for key, value in questions.items():
    print(key + ".", value["name"])

choice = input("\nانتخاب شما: ")

if choice in questions:
    score = 0
    selected_questions = questions[choice]["questions"]

    print("\nشروع بازی:", questions[choice]["name"])

    for question, answer in selected_questions:
        print("\n" + question)
        user_answer = input("پاسخ شما: ").strip().lower()

        if user_answer == answer.lower():
            print("آفرین! پاسخ صحیح است.")
            score += 1
        else:
            print("پاسخ اشتباه است.")
            print("پاسخ صحیح:", answer)

    print("\n========== نتیجه بازی ==========")
    print("تعداد پاسخ صحیح:", score)
    print("تعداد کل سوالات:", len(selected_questions))
    print("امتیاز نهایی شما:", score)
else:
    print("انتخاب نامعتبر است!")
