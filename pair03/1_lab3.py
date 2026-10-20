text = input("Введіть текст: ")
digits = 0
bukva = 0
vowels = 0
vowel = "аеєиіїоуюяaeiou"
space = 0

for char in text.lower():
    if char.isdigit():
        digits += 1
    if char in vowel:
        vowels += 1
    if char == " ":
        space += 1
    if char.isalpha():
        bukva += 1

print(f"Кількість цифр: {digits}\nКількість букв: {bukva}\nКількість голосних: {vowels}\nКількість пробілів: {space}\nКількість слів: {len(text.split())}\nКількість символів: {len(text)}")
