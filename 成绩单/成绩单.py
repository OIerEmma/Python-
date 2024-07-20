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
index = nameList.index("陈炤宣")

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
