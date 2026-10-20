pib = input("Введіть ПІБ: ")
parts = pib.split()
if len(parts) == 3:
    parts[0] = parts[0].capitalize()
    parts[1] = parts[1][0].capitalize()
    parts[2] = parts[2][0].capitalize()
    print(f"{parts[0]} {parts[1]}. {parts[2]}.")
else:
    print("Відсутня хоча б одна частина ПІБ")