from random import randint

# class Chelovek:
#     pi = 3.14  # статический
#     __city = "Новосибирск"
#     def __init__(self):
#         self.high = 888  # public динамический
#         self.__vozrast = 40  # private динамический
#
#
# object = Chelovek()
# print(object.pi)




# class Chelovek:
#     def __init__(self, height):
#         self.hi = height
#
# object = Chelovek()  # не передал -> по умолчанию
# print(object.hi)
#
# object2 = Chelovek(150)  # передал ->
# print(object2.hi)

class Human:
    default_name = "Антон"
    default_age = 56
    def __init__(self, name = default_name, age = default_age):
        self.name = "Антон"
        self.age = 40
        self.__money = 4444_4444_4444
        self.__house = None

    def info(self):
        return (self.name, self.age, self.__money, self.__house)

    def earn_money(self):
        self.__money += 4444_0000_0000_0000

    def default_info(self):
        return (self.default_name, self.default_age)

    def __make_deal(self, dom):
        if self.__money > dom.final_price():
            self.__money -= dom.final_price()
            print("Денег достаточно")
            return True

    def buy_house(self, dom):
        if self.__make_deal(dom):
            dom.owner = self.name
            self.__money -= dom.final_price
            return "Хата приобретена"
        else:
            return f"Денег нехватает, нужно: {dom.price} а у тебя: {self.__money} осталось накопить: {dom.price - self.__money}"


class House:
    def __init__(self, ar = "Новосибирск", pr = 4444_0000_0000_0000):
        self.area = ar
        self.price = pr
        self.discount = randint(5, 25) / 100

    def final_price(self):
        return self.price - self.price * self.discount

chelovek = Human()
house = House()

print(chelovek.buy_house(house))


















































