import statistics
import random
N = int(input("Введіть кількість оцінок: "))

if N <= 0:
    print("Кількість оцінок повинна бути додатньою.")
else:
    grades = [random.randint(1, 12) for i in range(N)]

    count = 0

    for j in grades:
        if j >=10 and j <= 12:
            count += 1

    print("Оцінки:", grades)
    print("Мінімальна оцінка:", min(grades))
    print("Максимальна оцінка:", max(grades))
    print("Середнє значення:", statistics.mean(grades))
    print("Медіана:", statistics.median(grades))
    print("Кількість оцінок від 10 до 12:", count)
