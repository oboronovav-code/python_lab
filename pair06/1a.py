from datetime import date

try:
    date0 = [int(x) for x in input("Введіть дату події у форматі ( рік-місяць-день ): ").split('-')]
    date1 = date(date0[0], date0[1], date0[2])

    date2 = date.today()

    if date1 > date2:
        print("До події залишилось: ", (date1 - date2).days, "днів")
    elif date1 == date2:
        print("Подія відбудеться сьогодні!")
    else:
        print("Подія відбулась: ", (date2 - date1).days, "днів тому")
except ValueError:
    print("Введено некоректну дату. Будь ласка, перевірте формат та значення.")