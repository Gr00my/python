from musicbox import MusicBox
a = MusicBox()  # плеер
while True:
    a.igraem()
    otvet = input("Что ты услышал?:").lower()
    if otvet == "exit":  # Выход
        print("Пока")
        break
    a.proverit(otvet)