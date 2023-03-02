import json
import requests
# writeF = open("file.json", "w", encoding = "utf-8")
# # writeF.write("True")  # записываем в файл
# content = [None, True, (1, 2, 3), [1, 2, 3], "hello", "приффки"]
# json.dump(content, writeF, ensure_ascii = False)
# print(json.dumps(content))  # в json (но не в файл)
# writeF.close()

# readF = open("file.json", "r", encoding = "utf-8")
# # print(readF.read())
# print(json.load(readF))
# readF.close()

# за дачей 1

# readF = open("file.txt.py", "r", encoding="utf-8")
# content = readF.readlines()
#
# readF.close()
#
# print(content)
#
# d = {}
# for record in content:
#     splited = record.split(": ")
#     d[splited[0]] = splited[1].rstrip()
# print(d)
#
# f = open("file.json", "w", encoding="utf-8")
# json.dump(d, f, ensure_ascii=False)
# f.close()


response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()["iss_position"]
print(f"Широта:{data['latitude']}. Долго, да: {data['longitude']}")
