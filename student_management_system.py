remain = 0
name = "Oguzhan Kilci"
while remain < 3:
    id = input("Name and Surname: ")
    if id == name:
        print('Welcome ', id)
        break
    else:
        print("incorrect id please try again:")
        remain += 1

derssayisi = int(input("How many lessons will you take: "))
dersler = []

if derssayisi <= 2 or derssayisi >= 5:
    print("You failed in class!")
else:
    for i in range(0, derssayisi):
        print("Enter the lessons")
        ders = input()
        dersler.append(ders)

j = input("Type the lesson you want to calculate ")
if j in dersler:
    midterm = int(input("Please enter midterm: "))
    final = int(input("Please enter final: "))
    project = int(input("Please enter Project: "))
    grade = midterm*0.3 + final*0.5 + project*0.2
    di = {"midterm":midterm, "final":final, "project":project}
    print(di)
else:
    print("Invalid Lesson")
if grade >= 90:
    print("your grade", grade , "AA")
elif grade >= 70:
    print("your grade", grade, "BB")
elif grade >= 50:
    print("your grade", grade, "CC")
elif grade >= 30:
    print("your grade", grade, "DD")
else:
    print("your grade", grade, "FF")