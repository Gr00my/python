a = 0
z = int(input())
for i in range(z):
    s = input()
    if s == "X++" or s == "++X":
        a += 1
    elif s == "X--" or s == "--X":
        a -= 1
print(a)



