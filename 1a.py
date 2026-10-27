numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

dod = []
vid = []
parni = []
kratni3 = []
suma = 0

for num in numbers:
    if num > 0:
        dod.append(num)
    elif num < 0:
        vid.append(num)
    
    if num % 2 == 0:
        parni.append(num)
    
    if num % 3 == 0:
        kratni3.append(num)
    
    suma += num

print(f"Додатні: {dod}\nВід'ємні: {vid}\nПарні: {parni}\nКратні 3: {kratni3}\nМінімальне: {min(numbers)} Максимальне: {max(numbers)} Сума: {suma} Середнє: {suma / len(numbers)}" )