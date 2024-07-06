bestFriends = ["Jerry", "Mark ", "Justin", "Jonny"]
print(bestFriends)
# print(bestFriends[2])
print(bestFriends[-1])
print(bestFriends[-2])
print(bestFriends[-3])
print(bestFriends[-4])


mid = (len(bestFriends) + 1) // 2

print(bestFriends[mid - 1])

bestFriends[0] = "Amy"
print(bestFriends)
bestFriends.append("Geek")
print(bestFriends)
