import string
import datetime
# class Nazvanie:
#     def __init__(self):
#         self.money = 1_000  # public "self.peremennaya"
#         self.__zarplata = 5  # private "self.__peremennaya"
#
#     def bar(self):
#         if self.__zarplata > 4:
#             return True
#         else:
#             self.__sad()
#             return False
#
#     def __sad(self):
#         print("*Сане грустно*")
#
# sanya = Nazvanie()
# # print(sanya.money)  # public можно выводить
# # sanya.money += 100  # public можно менять
#
# # print(sanya.zarplata)  # private нельзя выводить
# # sanya.__zarplata = 10  # это public, private нельзя менять
# # sanya.__zarplata += 10  # это public, private нельзя менять
# # print(sanya.__zarplata)
# print(sanya.bar())
#
# sanya.__Nazvanie__zarplata = 1_000_000  # так можно менять private "chel."__class"__"peremennaya"
# print(sanya.bar())

# за дачей 1
# class car:
#     def start(self):
#         self.ON = print("«Автомобиль заведен»")
#         return
#
#     def stop(self):
#         self.OFF = print("«Автомобиль заглушен»")
#
#     def years(self, years):
#         self.years = years
#
#     def tip(self, type):
#         self.type = type
#
#     def color(self, color):
#         self.color = color
#
# car = car()
# car.color("черный(синий)")
#
# print(car.start())
# print(car.stop())

# за дачей 2
# class Alphabet:
#     def __init__(self, lang):
#         self.lang = lang
#         self.letters = string.ascii_lowercase
#
#     def print(self):
#         print(self.letters)
#     def letters_num(self):
#         print(len(self.letters))
#
# alphabet = Alphabet("eng")
# alphabet.print()
# alphabet.letters_num()

# за дачей 3
class Clock:
    def __init__(self):
        self.__time = "08:07:06"
        # self.__time = datetime.datetime.now().strftime("%H:%M:%S")
        self.__hours, self.__minutes, self.__second = self.__time.split(":")
        self.__hours, self.__minutes, self.__second = int(self.__hours), int(self.__minutes), int(self.__second)
        # self.minutes = self.__time.split(":")[1]
        # self.second = self.__time.split(":")[2]

    def hours(self):
        self.__hours += 1

    def minutes(self):
        self.__minutes += 1

    def second(self):
        self.__second += 1

    def test_h(self):
        if self.__hours > 23:
            self.__hours == 00

    def test_m(self):
        if self.__minutes > 59:
            self.__minutes == 00
            self.__hours += 1

    def vivod(self):
        print(f"{self.__hours}:{self.__minutes}:{self.__second}")

time_0 = Clock()
time_0.minutes()
time_0.test_m()
time_0.vivod()














