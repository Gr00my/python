x = int(input())

for i in range(x):
    a = input()
    if len(a) > 10:
        n = a[0] + str(len("a")-2)+ a[-1]
        print("n")
    else:
        print(a)
