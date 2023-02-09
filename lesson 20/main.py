import easygui
# за дачей 1
def atbash(tekst):
    eng_alfavit = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z "
    reversed_eng_alfavit = eng_alfavit[::-1]
    rus_alfavit = " А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я "
    reversed_rus_alfavit = rus_alfavit[::-1]
    itog = ""
    for letter in tekst:
        if letter not in rus_alfavit and letter not in eng_alfavit:
            itog += letter
        elif letter in rus_alfavit:
            zxc = rus_alfavit.index(letter)
            zxb = reversed_rus_alfavit[zxc]
            itog = itog + zxb
        else:
            zxc = eng_alfavit.index(letter)
            zxb = reversed_eng_alfavit[zxc]
            itog = itog + zxb
    easygui.msgbox()
    #print(itog)
shift =  easygui.enterbox(
    msg = "Введи сообщение, буба"

)
shifr = input("Введи сообщение: ").upper()
atbash(shifr)

#за дачей 2




