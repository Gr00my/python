# ============ классная работа ============

# def abc(a: int = 5) -> str:
#     return a
#
# func = lambda a, b: a + b
# print(func(2, 3))

# Классы. Полиморфизм. Наследование. Инкапсуляция.

# class Human:
#     pi = 3.14  # статический атребут
#     def say(self, fraza):  # публичный метод
#         return fraza
#
#     def __init__(self, vozrast:int = 0): # init -> initialization
#         print("я инит")
#         self.age = vozrast  # динамический атребут
#         self.money = 0
#
#     def __sad(self):  # __x преватный метод это добавление __ перед x
#         print("😢")
#
#     def work(self):
#         self.money += 10_000
#         self.__sad()  # приватные можно использовать в нутри классов
#
#     def __call__(self, *args, **kwargs):
#         print(f"Я человек, мне {self.age} лет и я имею {self.money} руб")
#
#     def __add__(self, other):
#         if type(other) == int:
#             return "Мандаринка" * other
#         return "Мандаринка"
#
# grisha = Human()  # основание обьекта на основе класса ->
# print(grisha.say("Привет"))
# print(grisha.age)
# grisha.age = 50
# anton = Human(21)
# print(anton.say("На урок!"))
# anton.work()
# print(anton.money)
# grisha()
# print(anton + 999)

# ================================


class Abc:
    def __init__(self):
        self.param = 5

    def komanda(self):
        return "Я - команда"


class Def(Abc):  # class x(zxc) zxc - родительский класс
    def action(self):
        return "Я - экшон"


a = Abc()
print(a.param)
b = Def()
print(b.param)
print(b.action(), )

# ============ криндж (полиморф) ============

# print = input
# print("Введи число: ")

# ================================
