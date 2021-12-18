import json

with open('user_data.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

#print(json_object)
#print(type(json_object))

if ("E005" in json_object["employee"]):
    print("yes")
else:
    print("no")
year = "2020"
#print(json_object["employee"]["E003"]["year"]["2020"]["leave"])
print(json_object["employee"]["E003"]["year"]["2020"]["basicPay"])
print(json_object["employee"]["E003"]["year"]["2020"]["overTime"])
print(json_object["employee"]["E003"]["year"]["2020"]["leave"])