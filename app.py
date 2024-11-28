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
    