sentence1 = input("Введіть рядок1: ").lower().replace(" ", "")
sentence2 = input("Введіть рядок2: ").lower().replace(" ", "")
if sorted(sentence1) == sorted(sentence2):
    print("Рядки є анаграмами.")
else:
    print("Рядки не є анаграмами.")