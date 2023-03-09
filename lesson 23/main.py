# class Person:  # объявление класса
#     def __init__(self, imya, vozrast):  # метод инициализации
#         self.age = vozrast  # Установка значений атрибутов
#         self.name = imya
#
#     def __str__(self):
#         return "x + y = 20"
#
#
# eugenii = Person("Еюгении", 40)
# anna = Person(vozrast=0, imya="Кристинна")
#
# print(anna.name)
# print(eugenii.age)
#
# print(anna)




# за дачей
from random import randint
#
# class Chel:
#     def __init__(self, vozrast, imya, familiya):
#         self.name = imya
#         self.surname = familiya
#         self.age = vozrast
#         self.grades = nums = [randint(2, 5) for n in range(randint(5, 10))]
#         self.sa = sum(self.grades) / len(self.grades)
#     def __str__(self):
#         return f"{self.age} {self.name} {self.surname}"
#     def greet(self):
#         return f"Привет! Я {self.name} {self.surname} мне {self.age}"
#
# Kiriecshka = Chel(20, "Кирилл", "Носков")
# Melanya = Chel(13, "Мелаша", "Дорн")
# Vladislav = Chel(14, "Владюша" ,"Пупочкин")
# Anton = Chel(20, "Антоша", "Смирнов")
# studen = [Kiriecshka, Melanya, Vladislav, Anton]
# # print(Kiriecshka.greet())
# # print("Возраст: ", Kiriecshka.age)
# # print("Имя: ", Kiriecshka.name)
# # print("Фамилия: ", Kiriecshka.surname)
# # print(Kiriecshka)
# # print("Оценки Кирилла",Kiriecshka.grades)
# # print("Средний бал: ", Kiriecshka.sa)
#
# dorogoidnevnik = {}
# for item in studen:
#     dorogoidnevnik[item.name] = item.sa
#
#
# sorted_dorogoidnevnik = dict(reversed(sorted(dorogoidnevnik.items(), key=lambda  item:item[1])))
#
# schetchik = 0
#
# for item in sorted_dorogoidnevnik:
#     schetchik += 1
#     print(f"{schetchik} {item} - {sorted_dorogoidnevnik[item]}")

# за дачей

class Rectangle:
    def __init__(self, d1, d2):
        self.dot1 = d1
        self.dot2 = d2

    def ploshad(self):
        a = self.dot2.y - self.dot1.y
        b = self.dot2.x - self.dot1.x
        return  a * b

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


dot1 = Point(1, 152)
dot2 = Point(2, 250)
pryamoug = Rectangle(dot1, dot2)
print(pryamoug.ploshad())

