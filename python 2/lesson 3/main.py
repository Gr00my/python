# классная👍 работа

# def nazvanie(name):
#     return name.upper()
#     # pass = затычка
#
# print(nazvanie("Нэйм"))

# def nazvanie(name):
#     return name
#     # pass = затычка
#
# print(nazvanie("Нэйм"))

# def nazvanie(name: str = "bogdan") -> str:  # type hint
#     """возвращает чиселко"""
#     return name
#     # pass = затычка


#  наведись внутрь скобки и посмотри в низ подсказки внимательней, что выло в ковычках то в подсказке ==> """"""
#            __
#            ||
#            ||
#            ||
#            \/
# print(nazvanie())
# print(nazvanie(1111))

# ================= за дачей 1 =================

# def functia(a:list) -> tuple:
#     return (max(a), min(a))
# print(functia([52, 2, 3, -1, 0]))

# ================= за дачей 2 =================

# def functia(x: list) -> list:
#     for nomber in x:
#         if x.count(nomber) > 1:
#             x.remove(nomber)
#     return sorted(x)[::-1]
#
# print(functia([1, 0, 2, 1]))

# ================= за дачей 3 =================

# def functia(lst: list) -> dict:
#     d = {"int" : 0,
#          "float" : 0,
#          "str" : 0,
#          "bool" : 0,}
#     for i in lst:
#         if type(i) == int:
#             d["int"] += 1
#         elif type(i) == float:
#             d["float"] += 1
#         elif type(i) == str:
#             d["str"] += 1
#         elif type(i) == bool:
#             d["bool"] += 1
#     return d
#
# print(functia([1, "Два", True, 3.14, False, "Четыре"]))

# ================= за дачей 4 =================

# def functia(s: int) -> list:
#     ktoto = [0, 1]
#     while ktoto[-1] < s:
#         ktoto.append(ktoto[-1]+ktoto[-2])
#     return ktoto[:-1]
#
# print(functia(355))

# ================= за дачей 5 =================

# def func(s: list, ss:list):
#     return sorted(s + ss)
#
# print(func([1, 5, 8, 11], [2, 6]))

#  ================= за дачей 6 =================

# odd
# minus 10
# div 2
# mul 6

# zero
# result
# exit

# d = {
#     "add": lambda x: c + x,
#     "minus": lambda x: c - x,
#     "div": lambda x: c // x,
#     "mul": lambda x: c * x,
# }
#
# c = 0
# while True:
#     zapros = input().split()
#     if len(zapros) == 1:
#         zapros = zapros[0] # ["zero"] -> "zero"
#         if zapros == "exit":
#             break
#         elif zapros == "result":
#             print(c)
#         elif zapros == "zero":
#             c = 0
#     else:
#         c = d[zapros[0]](int(zapros[1]))

#  ================= за дачей 7 =================

# def is_sorted(x: list) -> bool:
#     return x == sorted(x)
#
# print(is_sorted([1, 7, 1]))
# print(is_sorted([2, 3, 10]))

#  ================= за дачей 8 =================










































































































































































































































































































































































































































































































































































































































































































































































































































































































































