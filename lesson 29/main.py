import tkinter as tk

#========== CHECKBUTTON ==========

# def check():
#     print(val_cb.get())

#root = tk.Tk()

# val_cb = tk.BooleanVar()  # переменнафя для хронения True/False
# cb = tk.Checkbutton(root,
#                     text="Подписка",
#                     font=15,
#                     variable=val_cb,
#                     onvalue=True,
#                     offvalue=False,
#                     command=check)
# cb.pack()


#root.mainloop()

#========== RADIOBUTTON ==========

# def get_rb():
#     print(val_rb.get)
#
# root = tk.Tk()
#
# val_rb = tk.IntVar
# rb1 = tk.Radiobutton(root,
#                      text="Я почему-то РАДИОкнопка",
#                      variable=val_rb,
#                      value=246,
#                      command=get_rb)
# rb1.pack()
# rb2 = tk.Radiobutton(root,
#                      text="Я почему-то РАДИОкнопка",
#                      variable=val_rb,
#                      value=246,
#                      command=get_rb)
# rb2.pack()
#
#
# root.mainloop()



# root = tk.Tk()
# root.geometry("400x500")
#
# def get_skala(lolkek):
#     print(skala.get())
#     print(lolkek)
#
# skala = tk.Scale(root,
#                  from_=500,
#                  to=1000,
#                  width=50,
#                  length=300,
#                  orient=tk.HORIZONTAL,
#                  tickinterval=100,
#                  resolution=50,
#                  command=get_skala)
#
# skala.pack()
#
#
#
#
# root.mainloop()

#root = tk.Tk()

# img = tk.PhotoImage(file="heheheha.png")
# img = img.subsample(3, 3)
# img = .zoom(2, 2)
# lab = tk.Label(root, image=img)
# lab.pack()

# def switch():
#     if btn1['state'] == "disabled":
#         btn1['state'] = "normal"
#     else:
#         btn1['state'] ="disabled"
#
# btn1 = tk.Button(root,
#                  text="Активируй меня",
#                  state=tk.DISABLED,
#                  fg="red",
#                  disabledforeground="grey80",
#                  width=30)
# btn1.pack(pady=20)
# btn2 = tk.Button(root,
#                  text="Активатор_и_Дезактиватор_2023_без_вирусов,_регистрации_и_маминой_карты",
#                  command=switch,
#                  width=30)
# btn2.pack()


# ent = tk.Entry(root)
# ent.pack()
# ent.insert(tk.END, "Перекус таксиста ...")

#root.mainloop()

# за дачей 1

# root = tk.Tk()
#
# # Функция
#
# def kak_hochesh():
#     if btn['state'] == "disabled":
#         btn['state'] = "normal"
#         btn['text'] = "Активен!🙂🎉"
#     else:
#         btn['state'] = "disabled"
#         btn['text'] = "Неактивен!😫"
#
# # CheckButton
#
# cb = tk.Checkbutton(root,
#                     text="Активировать",
#                     command=kak_hochesh)
# cb.pack()
# #cb.select() # вкл по умолчанию
#
# # Button
#
# btn = tk.Button(root,
#                 text="Неактивен!😫",
#                 state=tk.DISABLED,)
# btn.pack()
#
#
#
#
# root.mainloop()


# за дачей 2

root = tk.Tk

#

def bold():
    if cb1_val.get():
        lab['font'] += "bold"
    else:
        lab['font'] += "bold"

def italic():
    if cb2_val.get():
        lab['font'] += "italic"
    else:
        lab['font'] += "italic"

def overstrike():
    if cb3_val.get():
        lab['font'] += "overstrike"
    else:
        lab['font'] += "overstrike"

def underline():
    if cb4_val.get():
        lab['font'] += "underline"
    else:
        lab['font'] += "underline"
# Label

lab = tk.Label(root,
               text="abc",
               font="arial12")
lab.pack()

# CheckButton

cb1_val = tk.BooleanVar
cb1 = tk.Checkbutton(root,
                     text="ЖИРНЫЙ",
                     variable=cb1_val,
                     onvalue=True,
                     offvalue=False,
                     command=bold)
cb1.pack


cb2_val = tk.BooleanVar
cb2 = tk.Checkbutton(root,
                     text="ЖИРНЫЙ",
                     variable=cb1_val,
                     onvalue=True,
                     offvalue=False,
                     command=italic)

cb2.pack()

cb3_val = tk.BooleanVar
cb3 = tk.Checkbutton(root,
                     text="ЖИРНЫЙ",
                     variable=cb1_val,
                     onvalue=True,
                     offvalue=False,
                     command=oversrike)

cb3.pack()

cb4_val = tk.BooleanVar
cb4 = tk.Checkbutton(root,
                     text="ЖИРНЫЙ",
                     variable=cb1_val,
                     onvalue=True,
                     offvalue=False,
                     command=underline)

cb4.pack()


root.mainloop()