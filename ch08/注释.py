"""
功能:记录某人的成绩单
作者:Emma
编写日期：2024年7月14号
"""
studentList = []
isError = False
student = {}
student["name"] = input("请输入姓名：")
student["ID"] = input("请输入学号:")
score1 = float(input("请输入语文成绩："))
if score1 <= 100 and score1 > 0:
    student["score1"] = score1
else:
    print("输入的语文成绩有误！")
    isError = True

score2 = float(input("请输入数学成绩："))
if score2 <= 100 and score2 > 0:
    student["score2"] = score2
else:
    print("输入的数学成绩有误！")
isError = True

score3 = float(input("请输入英语成绩："))
if score3 <= 100 and score3 > 0:
    student["score3"] = score3
else:
    print("输入的英语成绩有误！")
    score2 = float(input("请输入英语成绩："))
    isError = True

if isError == False:
    student["total"] = student["score1"] + student["score2"] + student["score3"]
    studentList.append(student)
    print(student["name"] + "的成绩单加载成功了！")
else:
    print("输入有误, 成绩无法显示！")