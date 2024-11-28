#Marksheet
name=(input("Enter your name:"))
roll=eval(input("Enter your Roll number:"))
for i in range(1,6):
    print("Enter marks of subject",i,"=",end="")
    sub=eval(input())
def stu(name, roll, sub1, sub2, sub3, sub4, sub5):
    total=sub1+sub2+sub3+sub4+sub5
    print("Total Marks=",total)
    per=total/(500)*100
    print("Percentage=",per)
    if per>=90:
        print("A1 Grade")
    elif per>=80:
        print("A Grade")
    elif per>=70:
        print("B Grade")
    elif per>=60:
        print("C Grade")
    elif per>=50:
        print("D Grade")
    elif per>=40:
        print("E Grade")
    else:
        print("FAIL!!")
stu(name, roll, sub, sub, sub, sub, sub)