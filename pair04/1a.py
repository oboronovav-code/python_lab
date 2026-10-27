group_info = ("10-IT", "2026/2027")
journal = {}

while True:
    print("Для редагування журналу групи користуйтеся наступними командами:")
    print("1. Дадати студента\n2.Показати весь журнал\n3.Вивезти рейтинг студентів зв середнім балом\n4. Знайти студента з найвищим середнім балом\n5. Вийти")
    a = int(input("Введіть номер команди: "))

    if a == 1:
        student = input("Введіть ім'я і 5 оцінок студента через пробіл (ПІБ: 1, 2, 3, 4, 5): ").split()
        if len(student) < 6:
                print("Помилка! Замало даних. Потрібно ввести ім'я та рівно 5 оцінок.")
        else:
            name = student[0]
            grades_input = student[1:]
                
            is_valid = True
            grades = []
            
            if len(grades_input) != 5:
                is_valid = False
            else:
                for item in grades_input:
                    if item.isdigit():
                        val = int(item)
                        if 1 <= val <= 12:
                            grades.append(val)
                        else:
                            is_valid = False
                            break
                    else:
                        is_valid = False
                        break
            
            if is_valid:
                journal[name] = grades
                print(f"Учня {name} успішно додано/оновлено!")
            else:
                print("Помилка! Перевірте оцінки: їх має бути рівно 5, і вони мають бути в діапазоні від 1 до 12.")
    elif a == 2:
        print(f"{group_info[0]} — {group_info[1]}")
        if not journal:
            print("Журнал порожній.")
        else:
            for name, grades in journal.items():
                print(f"{name}: ", end="")
                for grade in grades:
                        print(grade, end=" ")
                print()
    elif a == 3:
        print(f"{group_info[0]} — {group_info[1]}")
        if not journal:
            print("Журнал порожній.")
        else:
            average_grades = []
            for name, grades in journal.items():
                average = sum(grades) / len(grades)
                average_grades.append((average, name))

            average_grades.sort(reverse=True)

            grouped_ratings = {}
            for average, name in average_grades:
                avg_val = int(average) if average.is_integer() else round(average, 1)
                if avg_val not in grouped_ratings:
                    grouped_ratings[avg_val] = []
                grouped_ratings[avg_val].append(name)

            for avg_val, students_list in grouped_ratings.items():
                names_str = ", ".join(students_list)
                print(f"{names_str} — {avg_val}")
    elif a == 4:
        print(f"{group_info[0]} — {group_info[1]}")
        if not journal:
                print("Журнал порожній.")
        else:
            best_student = None
            max_avg = -1.0
            
            for name, grades in journal.items():
                avg = sum(grades) / len(grades)
                if avg > max_avg:
                    max_avg = avg
                    best_student = name
            
            max_avg_display = int(max_avg) if max_avg.is_integer() else round(max_avg, 1)
            print(f"\nНайкращий результат: {best_student} — {max_avg_display}")

    elif a == "5":
        print("Завершення роботи програми.")
        break
    else:
        print("Некоректний вибір. Спробуйте ще раз.")