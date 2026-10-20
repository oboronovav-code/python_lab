sentence = input("Введіть речення: ")
sentence1 = sentence.lower().split()
delet = input("Введіть слово яке заміняємо: ").lower()
zamina = input("Введіть слово на яке заміняємо: ").lower()

longest_list = []
shortest_list = []
unic_list = []

max_len = max(len(w) for w in sentence1)
min_len = min(len(w) for w in sentence1)

for w in sentence1:
    if len(w) == max_len and w not in longest_list:
        longest_list.append(w)
    if len(w) == min_len and w not in shortest_list:
        shortest_list.append(w)

for char in sentence1:
    if char not in unic_list:
        unic_list.append(char)

sentence2 = sentence.replace(delet, zamina)
print("Найдовші слова: ", longest_list, "Найкоротші слова: ", shortest_list, "Унікальні слова: ", len(unic_list), "Речення після заміни: ", sentence2)