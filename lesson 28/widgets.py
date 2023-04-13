# import tkinter as tk
# def show_message():
#     # приём значения из Entry
#     message = ent.get()  # сохранить сообщение с поля ввода
#     ent.delete(0, 'end')  # отчистка поля для ввода
#     lab['text'] = message
#     print(message)
#
# message2 = txt.get(0.0, 'end')
# print(message2)
#
# window = tk.Tk()
# window.geometry("300x400")
# lab = tk.Label(window, text="Бублики",
#                font="Verdana 18",
#                fg="pink4", bg="blue",
#                width=50)
# lab.pack()
# ent = tk.Entry(bd=7, width=10)  # поле для ввода
# ent.pack()
#
# btn = tk.Button(window, text="Отправить")
# btn['font'] = ("JetBrains Mono", 15)
# btn['bg'] = "blue"
# btn['fg'] = "black"
# btn['command'] = show_message
# btn.pack()
#
# txt = tk.Text(window, width=20, height=5)  # многострочный ввод
# txt.pack()
#
#
# window.mainloop()

import tkinter as tk

#window
window = tk.Tk()
window.geometry("500x400")

#lab1
lab1 = tk.Label(window, text="Ваш адрес:", fg="black", bd="white2")
lab1.pack()

#ent
ent = tk.Entry(window, bd=1, fg=20)
ent.pack()

#lab2
lab2 = tk.Label(window, text="Коментарий:")
lab2.pack()

#txt
txt = tk.Text(window, width=20, height=5)
txt.pack()

#btn
btn = tk.Button(window, text="")
btn.pack()



















window.mainloop()




































