import requests
import random
class User:
    def __init__(self, im="", fam="", log="", pas=""):
        self.__lorem = "abcd"
        self.__data = requests.get("https://api.randomdatatools.ru/").json()
        self.login = self.__data["Login"] if not log else log
        self.__password = self.__data["Password"] if not pas else pas
        self.imya = self.__data["FirstName"] if not im else im
        self.familiya = self.__data["LastName"] if not fam else fam
        self.otchestvo = self.__data["FatherName"] if not log else log
        self.posts = [self.__lorem[random.randint(0, 35):random.randint(36, 70)]]