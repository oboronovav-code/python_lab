prices = {"яблука": 50, "банани": 70, "апельсини": 60, "молоко": 30, "хліб": 25}
print("Задля редагування словнику товарів користуйтеся такими операціями")
print("1 - додати товар\n2 - змінити ціну товару\n3 - пошук товару за назвою\n4 - сортування за ціною товару")
a = int(input("Введіть номер операції: "))
if a == 1:
    new_tovar = input("Введіть назву і ціну нового товару через пробіл:").split()
    prices[new_tovar[0]] = int(new_tovar[1])
elif a == 2:
    tovar = input("Введіть назву товару, ціну якого хочете змінити: ")
    if tovar in prices:
        new_price = int(input("Введіть нову ціну товару: "))
        prices[tovar] = new_price
    else:
        print("Товар не знайдено.")
elif a == 3:
    tovar = input("Введіть назву товару, який хочете знайти: ")
    if prices.get(tovar) == None:
        print("Товар не знайдено.")
    else:
        print(f"Ціна товару {tovar} - {prices[tovar]} грн.")
elif a == 4:
    low = float(input("Введіть нижню межу ціни: "))
    high = float(input("Введіть верхню межу ціни: "))
    for key, value in prices.items():
        if low <= value <= high:
            print(f"{key} - {value} грн.")
        else:
            prices.get(key, "Товар не знайдено.")
else:
    print("Такої операції не існує.")
