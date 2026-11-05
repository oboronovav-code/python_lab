def rectangle(a, b):
    return a * b

def circle(r):
    return 3.14159 * r * r

def triangle(base, height):
    return 0.5 * base * height

def main():
    figure = input("Введіть фігуру (прямокутник, коло, трикутник): ")
    if figure == "прямокутник":
        height = float(input("Введіть висоту сторони a: "))
        width = float(input("Введіть ширину сторони b: "))
        print("Площа прямокутника:", rectangle(height, width))
    elif figure == "коло":
        r = float(input("Введіть радіус круга: "))
        print("Площа круга:", circle(r))
    elif figure == "трикутник":
        base = float(input("Введіть основу трикутника: "))
        height = float(input("Введіть висоту трикутника: "))
        print("Площа трикутника:", triangle(base, height))
    else:
        print("Невідома фігура")

main()
