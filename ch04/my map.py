person = {"name": "Emma", "age": 10, "gender": "male", ":height": "143cm"}
print(person)

print(person["name"])
print(person["gender"])

# print(person["grade"])

fruits = {-100: "apple", 150: "banana", 8: "orange", -100: "cherry"}
print(fruits)

person = {}
person["name"] = "Emma"
person["age"] = 10
person["gender"] = "male"
print(person)

person["age"] = 9
print(person)

person["grade"] = 5
print(person)

del person["age"]
print(person)

# person.clear()
print(person)

print(person.get("name"))

print(person.get("weight", "no"))

if person.get("weight", "no") == "no":
    print("oh no value, sorry")
else:
    print("hihi")

print(person.keys())
list1 = list(person.keys())
print(list1)
list2 = list(person.values())
print(list2)
list3 = list(person.items())
print(list3)


scoreDict = {"John": 82, "Christina": 95, "James": 76, "Jessica": 100}
list4 = list(scoreDict.items())
list4.sort(key=lambda item: item[1], reverse=True)
print(list4)

list5 = [["John", 82], ["Christina", 95], ["James", 76], ["Jessica", 100]]
dict1 = dict(list5)
print(dict1)
