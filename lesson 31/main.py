from tkinter import *
root = Tk()
root.geometry("550x550")



c = Canvas(root, width=500, height=500, bg="Lightblue")
c.pack(anchor=CENTER, expand=True)

# ================ Текст ================
# c.create_text(0, 0,
#               text="Пельмени * 8 ",
#               font="Arial 20",
#               fill="gold2",
#               anchor="nw")

# ================ Прямоугольник ================
# c.create_rectangle(10, 10,
#                    200, 150,
#                    fill='red',
#                    width=10,
#                    outline='darkred')

# ================ Многоугольник ================
# c.create_polygon(10, 10,
#                  150, 150,
#                  10, 150)

# ================ Окружность ================
# c.create_oval(10, 10,
#             250, 150,)

# ================ arc ================
# c.create_oval(10, 10,
#               150, 150,
#               fill='silver')
#
# c.create_arc(10, 10,
#              150, 150,
#              fill='brown',
#              start=30,
#              extent=-45,)
#
# c.create_arc(10, 10,
#              150, 150,
#              fill='blue',
#              start=90,
#              extent=135,
#              style=CHORD)
#
# c.create_arc(10, 10,
#              150, 150,
#              fill='magenta',
#              start=110,
#              extent=135,
#              style=ARC,
#              width=10)

# ================ Линии ================
# c.create_line(10, 10,
#               150, 150,
#               arrow=BOTH,
#               arrowshape=(50, 50, 50),
#               width=20,)

# ================ DASH ================

# c.create_rectangle(10, 10,
#                    200, 150,
#                    fill='red',
#                    width=10,
#                    outline='darkred',
#                    dash='-..',
#                    activefill='blue',
#                    activewidth=50)











root.mainloop()