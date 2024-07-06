foodList = []
foodList.append("cake")
foodList.append("bread")
foodList.append("fish")
foodList.append("meat")
foodList.append("rice")
print(foodList)

foodList.insert(len(foodList), "fruit")
foodList.insert(len(foodList), "icecream")
print(foodList)

print(len(foodList))

del foodList[0], foodList[0]
print(foodList)

foodList.sort()
print(foodList)
