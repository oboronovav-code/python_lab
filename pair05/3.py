def average(grades):
    return sum(grades)/len(grades)

def minimum(grades):
    return min(grades)

def maximum(grades):
    return max(grades)

def count_above(grades, value):
    return sum(1 for grade in grades if grade > value)

def main():
    grades = [int(x) for x in input("Запишіть оцінки через пробіл: ").split()]
    value = int(input("Поріг: "))

    print("Середній бал:", average(grades))
    print("Мінімальна:", minimum(grades))
    print("Максимальна:", maximum(grades))
    print(f"Вище {value}:", count_above(grades, value))

main()
