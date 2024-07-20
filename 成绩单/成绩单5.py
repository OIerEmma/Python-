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
nameList = ["郭铭轩", "郭沛佳", "王小慧", "郭晓琪"]
IDList = ["1", "2", "3", "4"]
scoreList1 = [96, 98, 99, 96]
scoreList2 = [98, 96, 98, 97]
scoreList3 = [96, 99, 99, 98]
totalList = [scoreList1[0] + scoreList2[0] + scoreList3[0],
             scoreList1[1] + scoreList2[1] + scoreList3[1],
             scoreList1[2] + scoreList2[2] + scoreList3[2],
             scoreList1[3] + scoreList2[3] + scoreList3[3]
             ]

print("现在已经有" + str(len(nameList)) + "个朋友的成绩，他们的得分如下：")
print("学号     姓名     语文     数学     英语     总分")
print(IDList[0], "   ", nameList[0], "   ", scoreList1[0], "   ", scoreList2[0], "   ", scoreList3[0], "   "
      , totalList[0])
print(IDList[1], "   ", nameList[1], "   ", scoreList1[1], "   ", scoreList2[1], "   ", scoreList3[1], "   "
      , totalList[1])
print(IDList[2], "   ", nameList[2], "   ", scoreList1[2], "   ", scoreList2[2], "   ", scoreList3[2], "   "
      , totalList[2])
print(IDList[3], "   ", nameList[3], "   ", scoreList1[3], "   ", scoreList2[3], "   ", scoreList3[3], "   "
      , totalList[3])

print("----------------")

print("第二位同学的数学成绩记录好像有点问题...噢，应改成98分哦")
scoreList2[1] = 98
totalList[1] = scoreList1[1] + scoreList2[1] + scoreList3[1]

print("第二位同学修改后的如下：")

print("学号     姓名     语文     数学     英语     总分")
print(IDList[1], "   ", nameList[1], "   ", scoreList1[1], "   ", scoreList2[1], "   ", scoreList3[1], "   "
      , totalList[1])

print("----------------")

print("接下来我们要录取一名新同学 这是他的成绩")
nameList.append(input("请输入学生姓名:"))
IDList.append(input("请输入学生学号:"))
scoreList1.append(input("请输入学生语文成绩:"))
scoreList2.append(input("请输入学生数学成绩:"))
scoreList3.append(input("请输入学生英语成绩:"))
totalList.append(float(scoreList1[3]) + float(scoreList2[3]) + float(scoreList3[3]))

print("现在已经有" + str(len(nameList)) + "个朋友的成绩，他们的得分如下：")
print("学号     姓名     语文     数学     英语     总分")
print(IDList[0], "   ", nameList[0], "   ", scoreList1[0], "   ", scoreList2[0], "   ", scoreList3[0], "   "
      , totalList[0])
print(IDList[1], "   ", nameList[1], "   ", scoreList1[1], "   ", scoreList2[1], "   ", scoreList3[1], "   "
      , totalList[1])
print(IDList[2], "   ", nameList[2], "   ", scoreList1[2], "   ", scoreList2[2], "   ", scoreList3[2], "   "
      , totalList[2])
print(IDList[3], "   ", nameList[3], "   ", scoreList1[3], "   ", scoreList2[3], "   ", scoreList3[3], "   "
      , totalList[3])
print(IDList[4], "   ", nameList[4], "   ", scoreList1[4], "   ", scoreList2[4], "   ", scoreList3[4], "   "
      , totalList[4])

print("----------------")

print("陈炤宣同学转学了")
index = nameList.index("郭铭轩")

del nameList[index], IDList[index], scoreList1[index], scoreList2[index], scoreList3[index], totalList[index]

print("现在已经有" + str(len(nameList)) + "个朋友的成绩，他们的得分如下：")
print("学号     姓名     语文     数学     英语     总分")
print(IDList[0], "   ", nameList[0], "   ", scoreList1[0], "   ", scoreList2[0], "   ", scoreList3[0], "   "
      , totalList[0])
print(IDList[1], "   ", nameList[1], "   ", scoreList1[1], "   ", scoreList2[1], "   ", scoreList3[1], "   "
      , totalList[1])
print(IDList[2], "   ", nameList[2], "   ", scoreList1[2], "   ", scoreList2[2], "   ", scoreList3[2], "   "
      , totalList[2])
print(IDList[3], "   ", nameList[3], "   ", scoreList1[3], "   ", scoreList2[3], "   ", scoreList3[3], "   "
      , totalList[3])

print("----------------")

print("看看名次吧")
totalList.sort()
totalList.reverse()

print(totalList)
studentList = []
student = {"name": "郭铭轩", "ID": "1", "score1": 97, "score2": 99, "score3": 99, "total": 295}
studentList.append(student)
student = {"name": "郭沛佳",  "ID": "2", "score1": 98, "score2": 99, "score3": 100, "total": 297}
studentList.append(student)
student = {"name": "王晓慧", "ID": "3", "score1": 100, "score2": 98, "score3": 98, "total": 296}
studentList.append(student)
print("现在已经有" + str(len(studentList)) + "个朋友的成绩，他们的得分如下：")
print("学号     姓名     语文     数学     英语     总分")
print(studentList[0].get("ID"), "   ", studentList[0].get("name"), "   ", studentList[0].get("score1"), "   ",
studentList[0].get("score2"), "   ", studentList[0].get("score3"), "   ", studentList[0].get("total"))
print(studentList[1].get("ID"), "   ", studentList[1].get("name"), "   ", studentList[1].get("score1"), "   ",
studentList[1].get("score2"), "   ", studentList[1].get("score3"), "   ", studentList[1].get("total"))
print(studentList[2].get("ID"), "   ", studentList[2].get("name"), "   ", studentList[2].get("score1"), "   ",
studentList[2].get("score2"), "   ", studentList[2].get("score3"), "   ", studentList[2].get("total"))
studentList[0]["score2"] = 100
studentList[0]["total"] = studentList[1]["score2"] + studentList[1]["score2"] + studentList[1]["score3"]
print("第二位同学的数学成绩记录好像有点问题...噢，应改成98分哦")
print("第二位同学修改后的如下：")
print("学号     姓名     语文     数学     英语     总分")
print(studentList[0].get("ID"), "   ", studentList[0].get("name"), "   ", studentList[0].get("score1"), "   ",studentList[0].get("score2"), "   ", studentList[0].get("score3"), "   ", studentList[0].get("total"))
print("接下来我们要录取一名新同学 这是他的成绩")
student["name"] = input("请输入学生姓名:")
student["ID"] = input("请输入学生学号:")
student["score1"] = input("请输入学生语文成绩:")
student["score2"] = input("请输入学生数学成绩:")
student["score3"] = input("请输入学生英语成绩:")
student["total"] = float(student["score1"]) + float(student["score2"]) + float(student["score3"])
studentList.append(student)
print("现在已经有" + str(len(studentList)) + "个朋友的成绩，他们的得分如下：")
print("学号     姓名     语文     数学     英语     总分")
print(studentList[0].get("ID"), "   ", studentList[0].get("name"), "   ", studentList[0].get("score1"), "   ",
studentList[0].get("score2"), "   ", studentList[0].get("score3"), "   ", studentList[0].get("total"))
print(studentList[1].get("ID"), "   ", studentList[1].get("name"), "   ", studentList[1].get("score1"), "   ",
studentList[1].get("score2"), "   ", studentList[1].get("score3"), "   ", studentList[1].get("total"))
print(studentList[2].get("ID"), "   ", studentList[2].get("name"), "   ", studentList[2].get("score1"), "   ",
studentList[2].get("score2"), "   ", studentList[2].get("score3"), "   ", studentList[2].get("total"))
studentList[0]["score2"] = 100
print(studentList[3].get("ID"), "   ", studentList[3].get("name"), "   ", studentList[3].get("score1"), "   ",
studentList[3].get("score2"), "   ", studentList[3].get("score3"), "   ", studentList[3].get("total"))
studentList.sort(key=lambda x:x["total"])
print("看看名次吧")
print("学号     姓名     语文     数学     英语     总分")
print(studentList[0].get("ID"), "   ", studentList[0].get("name"), "   ", studentList[0].get("score1"), "   ",
studentList[0].get("score2"), "   ", studentList[0].get("score3"), "   ", studentList[0].get("total"))
print(studentList[1].get("ID"), "   ", studentList[1].get("name"), "   ", studentList[1].get("score1"), "   ",
studentList[1].get("score2"), "   ", studentList[1].get("score3"), "   ", studentList[1].get("total"))
print(studentList[2].get("ID"), "   ", studentList[2].get("name"), "   ", studentList[2].get("score1"), "   ",
studentList[2].get("score2"), "   ", studentList[2].get("score3"), "   ", studentList[2].get("total"))
studentList[0]["score2"] = 100
print(studentList[3].get("ID"), "   ", studentList[3].get("name"), "   ", studentList[3].get("score1"), "   ",
studentList[3].get("score2"), "   ", studentList[3].get("score3"), "   ", studentList[3].get("total"))
studentList.sort(key=lambda x:x["total"], reverse=True)
studentList.sort(key=lambda x: float(x["score1"]))