import requests
import random
class User:
    def __init__(self):
        self.__lorem = ""
        self.__data = requests.get("https://api.randomdatatools.ru/").json()
        self.login = self.__data["Login"]
        self.__password = self.__data["Password"]
        self.imya = self.__data["FirstName"]
        self.familiya = self.__data["LastName"]
        self.otchestvo = self.__data["FatherName"]
        self.posts = [self.__lorem[random.randint(0, 35):random.randint(36, 70)]]