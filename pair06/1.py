import math
radius = int(input("Введіть радіус круга: "))
katet = [int(x) for x in input("Введіть катети через пробіл: ").split()]
N = int(input("Введіть кількість предметів: "))
K = int(input("Скільки предметів вміщається в упаковці: "))

if radius <= 0:
    print("Радіус повинен бути додатнім числом.")
elif any(k <= 0 for k in katet):
    print("Катети повинні бути додатніми числами.")
elif N <= 0 or K <= 0:
    print("Кількість предметів та кількість предметів в упаковці повинні бути додатніми числами.")
else:
    area_circle = math.pi * radius ** 2
    hypotenuse = math.sqrt(sum(k ** 2 for k in katet))
    N1 = math.ceil(N / K)
    print("Площа круга: ", area_circle, "\nГіпотенуза: ", hypotenuse, "\nКількість упаковок: ", N1)
