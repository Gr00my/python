#  x1 = [] # пустой список(тип данных)
#  x1[0] # обращение по индексу 0
#  x1[0:2] # : - срез
#
#
# Cрезы(slice)
# alphabet = "ABCDEFG"
# print(alphabet[:6]) # 6 штук. но до индекса 5 (считаем от 0)
# print(alphabet[::2]) # все элементы через одного


# Error Handling
# x = 5 / 0 # ZeroDivisionError

# x = 15 + "a"  #TypeError

# x = [1, 2, 3, 4]
# print(x[4])  # IndexError: list index out of range (считаем от нуля)
#
# x = "привет # SyntaxError
#
# x = "o"
# print(int(x)) #ValueError
#
# print(spase) # NameError

# try:
#     y = int("a")
#     x = 5 / 0
# except Exception: # любой класс ошибок будет обработан
#     print("Я щас бы шашлыка бахнул")
# except ZeroDivisionError: # обрабатываем деление на ноль
#     print("Я небесный бог, а ты зелёный мох")

# try-except -> неразрывная конструкция
# nickname = input("Введи имя: ").lower()
# try:
#     if nickname == "админ" or nickname == "антон":
#         raise Exception("🚫 Это имя запрещено")
# except Exception as error_message:
#     # помещяем пояснение ошибки в переменную
#     print("Я зелёный мох, а ты небесный бог.", error_message)
# else: # если ошибок не было
#     print("Разрешаю")
# finally: # cработает вне зависимости от ошибок(было/не было)
#     print("Меня создал Антон")

#ЦИКЛЫ
#1. while
# x = 5
# while x > 0:
#     print("Э")
#     x -= 1  # тоже самое что и x = x - 1
#
# while True: # бесконечная ульта цикла
#     print("o   O     OOOOOOooo")
#     break  # отановку ближайшего цикла
#
# while False: # шизофрения - потому что не выполнится НИКОГДА

# 2. for
# 1) итерация по переменным
# """
# word = "movavi"
# lst = [1, 2, 3, 4]
# for anton in lst:
#     print(anton)
# """
# 2) in range(start, stop, step)
# """
# for i in range(10, 100, 2):
#     print(i)
#
# for a in range(5, 10, -2): # несрабатывающий цикл
#     print(a)
#
# for a in range(5, 10, -2): # несрабатывающий цикл
#     print(a)
# """