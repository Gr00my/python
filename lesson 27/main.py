# 2
print(int("08"))

start = input("Начало первого урока (чч:мм): ")
urok = input("Длительность урока (мин): ")
peremenaya = input("Длительность перемен (мин): ")
raspisanie = input("На сколько уроков нужно расписание: ")

splited_start = start.split(":")
hours = int(splited_start[0])
minutes = int(splited_start[1])
vremya = hours * 60 + minutes

for i in range(vremya):
    print(i + 1, "урок: ", end="")
    print(f"{str(vremya//60).rjust(2, '0')}:{str(vremya%60).rjust(2, '0')} - ", end="")
    vremya += urok
    print(f"{str(vremya//60).rjust(2, '0')}:{str(vremya%60).rjust(2, '0')}")
    vremya += peremenaya
