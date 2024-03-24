##calculate the sum of digits of a number taking input from a user
num=int(input("Enter the digit:"))
sum=0
while num!=0:
     n=num%10
     sum=sum+n
     num=n//10
print(sum)
