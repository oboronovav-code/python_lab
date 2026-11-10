def is_prime(n):
    if n < 1:
        return "Не натуральне число"
    elif n !=1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return "Ні"
        return "Так"

def divisors(n):
    if n < 1:
        return "Не натуральне число"
    else:
        divs = []
        for i in range(1, n + 1):
            if n % i == 0:
                divs.append(i)
        return divs

def digit_sum(n):
    if n < 1:
        return "Не натуральне число"
    else:
        return sum(int(digit) for digit in str(n))

def main():
    n = int(input("Введіть натуральне число: "))
    print(f"Просте число: {is_prime(n)}")
    print(f"Дільники: {divisors(n)}")
    print(f"Сума цифр: {digit_sum(n)}")

main()