name = ""
while name != "Amy":
    print("Please input a name.input stop to quit:")
    name = input()
    if name == "stop":
        break

password = 13656572713
while True:
    useInput = input("Please input your password:")
    if useInput == password:
        print("open your browser")
        break
    else:
        print("your password is correct please try again")

number = 0
while number < 10:
    number = number + 1
    if number % 3 == 0:
        continue
    print("The current number is :" + str(number))

animals = ["Tiger", "Lion", "Panda", "Bear", "Wolf"]
for animal in animals:
    print("This zoo contains a"+ animal + ".")
