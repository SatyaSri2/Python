##write a prog to check the type of triangle where you take the input from user for 3 sides and
##classify it into acc equilateral,isoceles,scalene
a=int(input("enter the side a:"))
b=int(input("enter the side b:"))
c=int(input("enter the side c:"))
if a==b==c:
    print("Equilateral Triangle")#all sides are equal
elif a==b or b==c or a==c:
    print("Isoceles Triangle")#2 sides are equal
elif a!=b!=c:
    print("Scalene Triangle")#no 2 sides are equal
