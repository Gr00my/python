import tkinter as tk

def baget(qwerty):
    print("Я круассан")

window = tk.Tk()  # инициализация, создание В НАЧАЛЕ
window.geometry("500x400")  # размеры окна
window.title("моё первое окошечко :з")

btn = tk.Button(window, text="Моя первая кнопачка :з")  # создание кнопки и текста здесь
btn.pack()
btn['text'] = "Ы 🌷 "  # изменение конфигурации
btn['font'] = ("JetBrains Mono",  # шрифт
               15,  # его размер
               "bold",  # его обводка
               "underline",  # подчеркнуто
               "italic",  # курсив
               "overstrike",  # зачеркнуто
               )

#btn['background'] = "gold4"  # цвет на фоне
btn['bg'] = "gold4"
#btn['foreground'] = "pink"  # цвет текста
btn['fg'] = "pink"
btn['width'] = 10  # Ширина
btn['height'] = 3  # Высота
#btn['borderwidth'] = 10  # Ширина рамки
btn['bd'] = 10
#btn['command'] = baget  # нажатие кнопки в консоли выведет def baget, ВСЕГДА БЕЗ "()" !!!
btn.bind("<Double-Button-1>", baget)  # либо уоманд либо бинд

window.mainloop()  # отображение в окна В КОНЦЕ