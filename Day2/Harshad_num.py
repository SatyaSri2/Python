##taken an int as input from user and
##check whether if the num is divi by its sum of digits or not
num=int(input("Enter the Number:"))
n1=num
add=0
while num>0:
    a=num%10
    add+=a
    num=num//10
print("Sum of digits:",add)
if (n1%add)==0:
    print("It is divisiable")
else:
    print("Not divisiable")
