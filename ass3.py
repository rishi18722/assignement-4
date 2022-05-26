#Q1
m=float(input("Enter marks scored"))
print("grade")
if (m<25):
  print("F")
elif (25<=m<45):
  print("E")
elif (45<=m<50):
  print("D")
elif (50<=m<60):
  print("C")
elif (60<=m<=80):
  print("B")
else:
  print("A")
  
  
#Q2
y=int(input("Enter year"))

if (y%4==0):
  if (y%100!=0):
    if (y%400==0):
      print("The year is a leapyear")
    else:
      print("The year is not a leapyear")
  else:
    print("The year is not a leapyear")
else:
  print("The year is not a leapyear")
  
#Q3
import random
a=random.randint(0,9)
b=random.randint(0,9)
print(a,"x",b,"=")
c=int(input())

if c==(a*b):
  print("Right")
else:
  print("Wrong. The answer is",a*b)


#Q4
n=int(input("Enter the no of candy"))
if n<200:
  if n%5==2:
    if n%6==3:
      if n%7==2:
        print("Your guess is correct")
      else:
        print("Try again")
    else:
      print("Try again")
  else:
    print("Try again")
else:
  print("Try again")
