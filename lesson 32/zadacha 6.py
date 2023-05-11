#
#     H       H    EEEEEEEEE               H       H    EEEEEEEEE               H       H    EEEEEEEEE               H       H        A
#     H       H    E                       H       H    E                       H       H    E                       H       H       A A
#     H       H    E                       H       H    E                       H       H    E                       H       H      A   A
#     H       H    E                       H       H    E                       H       H    E                       H       H     A     A
#     HHHHHHHHH    EEEEEEE     ----------  HHHHHHHHH    EEEEEEE     ----------  HHHHHHHHH    EEEEEEE     ----------  HHHHHHHHH    A       A
#     H       H    E                       H       H    E                       H       H    E                       H       H    AAAAAAAAA
#     H       H    E                       H       H    E                       H       H    E                       H       H   A         A
#     H       H    E                       H       H    E                       H       H    E                       H       H   A         A
#     H       H    EEEEEEEEE               H       H    EEEEEEEEE               H       H    EEEEEEEEE               H       H   A         A








a1 = input().upper()
anser = 0
a2 = input().upper()

for i in range(len(a1)):
    if a1[i] != a2[i]:
        if a1[i] < a2[i]:
            anser = -1
            break
        elif a2[i] < a1[i]:
            anser = 1
            break
print(anser)