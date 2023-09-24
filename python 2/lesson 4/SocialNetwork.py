class User:
    def __init__(self, imya, parol, login):
        self.name = imya
        self.password = parol
        self.nickname = login
        self.followers = []  # кто на тебя подписан
        self.subscribers = []  # на кого ты подписан
        self.session = False



    def change_pas(self):
        print("Если хотите выйти напишите exit")
        while True:
            paroll = input("Введите старый пароль: ")
            if paroll == self.password:
                self.password == input("Введите новый пороль: ")
                print("Пароль успешно изменен")
                break
            elif paroll.lower() == "exit":
                break
            else:
                print("Неправильно, попробуй ещё раз!")

    def authorize(self):
     print("Войдите пожалуйста")
     while True:
         if not self.session:  # если не вошел
             if input("Логин: ") == self.nickname and \
                 input("Пароль: ") == self.password:
                 self.session = True
             else:
                 print("Неправильно, попробуй ещё раз")
         else:  # вошел в акаунт
            print("Если хотите выйти то напишите 'ничего' без ковычек")
            why = input("Что будем делать? : ")
            if why.lower() == "изменить пароль":
                u2.change_pas()
            else:
                break


u1 = User("Вероника", "1234", "vena1900")
u2 = User("БандитНСК", "slojno", "abybandit")
u2.authorize()