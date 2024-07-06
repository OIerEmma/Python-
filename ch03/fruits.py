fruits = []
fruits.append("apple")
fruits.append("banana")
fruits.append("orange")
fruits.append("grape")
fruits.insert(1, "cherry")
print(fruits)
print("fruits")
#
# del fruits[1]
# print(fruits)
# fruits.remove("orange")
# print(fruits)
# poped = fruits.pop()
# print(fruits)
# print(poped)
poped = fruits.pop(2)
print(poped)
fruits = ["cherry", "apple", "banana", "orange"]
len(fruits)
print(len(fruits))
print(fruits)
print(fruits[len(fruits)-1])
print(fruits.index("banana"))
print(fruits.index("cherry"))
# fruits.sort(reverse=True)
print(fruits)
fruits.reverse()
print(fruits)
strFruits = "@".join(fruits)
print(strFruits)

strName = "朱晓宇,李晓璇,张小腿,李晓艺"
nameList = strName.split(",")
print(strName)
jidjid