if 3 > 2:
    print("Three is greater then two")

letter = input("please input:")

if letter == "S":
    print("please input second letter")
    letter = input("please input :")
    if letter == "a":
        print("Saturday")
    elif letter == "u":
        print("Sunday")
    else:
        print("data error")

elif letter == "F":
    print("Friday")

elif letter == "M":
    print("Monday")

elif letter == "T":
    print("Tuesday")
    letter = input("please input:")
    if letter == "u":
        print("Tuesday")
    elif letter == "h":
        print("Thursday")
    else:
        print("Wednesday")
elif letter == "W":
    print("Wednesday")
else:
    print("data error")

