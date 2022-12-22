# первый задача
# phrase = input().title().strip()  #                РОССИЯ, РОССИЯ, РОССИЯ И БОГДАН!
# symbols = list("!@#$%^&*()1234567890'\",.?№;:")  # \ - экранирование.
# phrase_clear = ""  # щас будем мыть фразу
# for ovoshi in phrase:  # итерироваться по фразе
#     if ovoshi not in symbols:  # если это не спец. символ
#         phrase_clear += ovoshi
#
# phrase_list = phrase_clear.split(" ")
# print(phrase_list)
#
# d = {}
# for dom in phrase_list:
#     if dom not in d:  # если ключа нет
#         d[dom] = 1  # обозначение нового элемента {"Росиия": 1}
#     else:  # если ключ есть
#         d[dom] += 1  # плюс один элемент
# print(d)



# Фдалаи сотащы.
sloj = 0
d = {"Молоко": 100,
     "Доширак":21,
     "Чипсы":0.5,
     "Богдан":999.5,}
print("Много")
for i in d.values():  # перебор по значениям
    sloj = sloj + i
print(sloj)

# Тлитеи (со тащие)
DIE_SIDES = 6
DIE_COUNT = 2
d = {}


for first in range(1, DIE_SIDES + 1):  # от одного до 6
    for second in range(1, DIE_SIDES + 1):
        if first + second not in d:  # если суммы кубиков нет в словаре
            d[first + second] = [(first, second)]
        else:
            d[first + second].append((first, second))  # добовляем в словарь

# вывод
for tajikistan in d:
    print(f"{tajikistan}: {d[tajikistan]}")




