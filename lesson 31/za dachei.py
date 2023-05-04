from tkinter import *

# ================ 1 за дачей =========

# ================ def ================
# def poop():
    # global timer
    # c.delete("all")
    # timer += 1

    # ================ часы ================
    # c.create_image(300, 245, image=img)

    # ================ text ================
    # c.create_text(301, 250, text=timer, font='Arial 20')
    # c.after(1000, poop)

    # ================ условие ================
    # if timer == 16:
    #     win.destroy()

# ================ Win =========

# win = Tk()
# win.geometry("700x600")

# ================ Canvas =========
# c = Canvas(win, width=600, height=500, bg='silver')

# c.pack(anchor=CENTER, expand=True)

# ================ timer =========
# timer = 0

# ================ c.text =========
# c.create_text(300, 250,
#               text=timer,
#               font='Arial 20',)

# ================ image ================
# img = PhotoImage(file='clock.png').subsample(4, 4)

# ================ другое ================


# poop()
# win.mainloop()

# ================ 2 за дачей ================

# ================ Win ================
win = Tk()
win.geometry("1000x600")
# ================ Canvas ================
c = Canvas(win, width=700, height=200, bg='silver')
c.pack(anchor=CENTER, expand=True)

# ================ text ================
c.create_text(10, 10,
              anchor=NW,
              text='Школа',
              font='Arial20',)

c.create_text(300, 10,
              anchor=NW,
              text="Туда-сюда",
              font="Arial 20")

c.create_text(650, 10,
              anchor=NW,
              text="Успешный успех",
              font="Arial 20")

# ================ line ================
c.create_line(150, 25,
              250, 25,
              arrow=LAST)

c.create_line(500, 25,
              600, 25,
              arrow=LAST)













win.mainloop()