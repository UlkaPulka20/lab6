from utils import get_countries_capitals, get_chars_rates, get_students_and_languages


def lab_6():
    country = input('Столицу какой страны хотите узнать? (или "all")  ')

    if country == "all" or country is None:
        print("Список всех стран из нашей базы:")
        for a, b in sorted(get_countries_capitals().items()):
            print("Страна:", a, "столица", b)
    elif country in get_countries_capitals():
        print("Страна:", country, "столица ", {get_countries_capitals().get(country)})
    else:
        print("Извините, кажется такой страны нет в нашей базе.")


def lab_62():
    chars_rate = get_chars_rates()

    print("Игра Эрудит")
    print("Вводите слово - получаете оценку сложости слова (посимвольно)")
    print("Если ввели несколько слов, то будет оцениваться только первое слово!")

    word_input = input("Введите слово: ")
    word_rate = 0

    if len(word_input) > 0:
        word = ""

        if len(word_input.split()) > 1:
            word = word_input.split()[0].lower()
        else:
            word = word_input.lower()

        for char in word:
            for rate, chars in chars_rate.items():
                if char in chars:
                    word_rate += rate
                    break

    print(f"Оценка вашего слова: {word_rate}")


def lab_6_3():
    students_and_languages = get_students_and_languages()

    all_known_languages = set({})
    student_who_know_chinese = []
    for student, langs in students_and_languages.items():
        if "китайский" in langs:
            student_who_know_chinese.append(student)
        for l in langs:
            all_known_languages.add(l)
    print("Языки, которые знают наши студенты:", ", ".join(sorted(all_known_languages)))
    print("Китайский язык знают:", ", ".join(student_who_know_chinese))


lab_6_3()
