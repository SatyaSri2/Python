#palindrome Number
n=1441
num1=n
rev=0
while n>0:
    num=n%10
    rev=rev*10+num
    n=n//10
print("Palindrome",rev)
if rev==num1:
    print("palindrome")
else:
    print("NOT A PALINDROME")
 
 
