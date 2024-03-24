##write a program in which you taken integer input from user
##if that integer is divisible by 3 and 6 print good number
##if that integer is divisible by 2 and 7 print avg number
##if that integer is divisible by 4 or 9 print awesome number
##else print bad number
a=int(input("enterb a number:"))
if a%3==0 and a%6==0:
    print("Good Number")
elif a%2==0 and a%7==0:
    print("avg number")
elif a%4==0 or a%9==0:
    print("awesome number")
else:
    print("bad number")
