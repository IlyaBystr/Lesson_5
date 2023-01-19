#38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)

text = input("Введите текст через пробел:\n")
print(f"Исходный текст: {text}")
find_txt = "абв"
lst = [i for i in text.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')