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