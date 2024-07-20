numberEight = 8
stringEight = "8"
# print(numberEight + stringEight)
try:
    numberEight = 8
    # numberEight = "8"
    # print(numberEight + stringEight)
    print("没有出现异常，一切顺利")
except:
    print("出现了异常")

try:
    numberEight = 8
    # numberEight = "8"
    print(numberEight + numberEight)
    print("没有出现异常，一切顺利")
except:
    print("出现了异常")

try:
    numberEight = 8
    print(numberEight/0)
    print("没有出现异常")
except ZeroDivisionError:
    print("这是一个除零错误")

