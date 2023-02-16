#import easygui
#
# result = easygui.msgbox(
#     msg = "Hello THE WORLD!!!",  # Тескт в окне
#     title = "Я карта",  # Название окна
#     ok_button = "Понял принял",  # Кнопка закрытия
#     image = "img/drel.png"
# )
#
# if result == None:
#     print("Ой, хорошего тебе дня, дружочек!")
# elif result == "img/drel.png"
#     print("Ты то что ты нажал")
#
#
#
# easygui.buttonbox(
#     msg = "Выбери какой сегодня ТЫ",
#     title = "Выбери",
#     choices = ("Заниженый","Опущеный", "Возвышеный", "Умеренный", "     "),
#     image = ["img/klybnika.png", "img/poo.png", "img/drel.png", "img/sun.png"]
# )
#
# easygui.integerbox(
#     msg = "Сколько раз?",
#     title =  "Чиселко",
#     lowerbound = 10,
#     upperbound = 50,
#     image = "img/sun.png",
#     default = 24
# )
#
# easygui.enterbox(
#     msg = "Ну, это самое..",
#     title = "Туда-суда",
#     image = "img/klybnika.png",
# )

import easygui
import random

def rock_paper_scissors():
    otvets = {
        "Bymaga":"img/Bymaga.png",
        "Nojnici":"img/Nojnici.png",
        "Kamen":"img/Kamen.png",
        "Russia":"img/Russia.png"
    }

    result = easygui.msgbox(
        msg = "Выбери",
        title = 'Игра "Камень ножници бумага"',
        image = ["img/Bymaga.png", "img/Kamen.png", "img/Nojnici.png", "img/Russia.png"],
        choices = ("Я ухожу, оставляя горы окурков,")
    )
    print(otvets.keys())
    answers_comp = random.choice(list(otvets.keys()))
    answers_comp = "Nojnici"
    print(answers_comp)
    if result == otvets["Kamen"] and answers_comp == "Nojnici":
        easygui.msgbox(msg = "Ты победил 👏")
#Дописать


def guess_the_number():
    n = easygui.indexbox(msg = "Какое число?",
                     lowerbound = 1,
                     upperbound = 99)
    n_c = random.randint(1, 99)
    if n == n_c:
        return
    while n != n_c:
        if n >n_c:
            n = easygui.indexbox(msg = "Какое число?",
                                 lowerbound = 1,
                                 upperbound = 99,)



games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()