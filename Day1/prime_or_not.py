##check whether the number is prime or not
n=34
flag=0
for i in range(2,n):#(2,n/2)
    if n%i==0:
        flag=1
        break
if flag==1:
    print("Not a prime")
else:
    print("Prime")
    
