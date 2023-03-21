import requests
import json

user = int(input("Введіть id користувача: "))
balance = int(input("Введіть balance користувача: "))


url = f"https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=setbalance&user={user}&balance={balance}"
res = requests.get(url)

json = res.json()
print(json)

id = f"https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=getdata&user={user}"
res2 = requests.get(id)

json = res2.json()
#print(json)

for q in range(len(json)):
   if json[q]["id"] is None:
      print("Error")
   else:
      print(
        "id", "=", json[q]["id"], "\n"+
        "name", "=", json[q]["name"], "\n"+
        "surname", "=", json[q]["surname"], "\n"+
        "email", "=", json[q]["email"], "\n"+
        "school_group", "=", json[q]["school_group"], "\n"+
        "status", "=", json[q]["status"], "\n"+
        "balance", "=", json[q]["balance"], "\n")



#if json == None:
#    print("id not found")
#else: print("dobra")
