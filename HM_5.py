#38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)

# text = input("Введите текст через пробел:\n")
# print(f"Исходный текст: {text}")
# find_txt = "абв"
# lst = [i for i in text.split() if find_txt not in i]
# print(f'Результат: {" ".join(lst)}')


#40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def encode(s):
 
    encoding = ""
 
    i = 0
    while i < len(s):
        count = 1
 
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
 
        encoding += str(count) + s[i]
        i = i + 1
 
    return encoding
 
 
if __name__ == '__main__':
 
    s = '222223333332222211100'
    print(encode(s))