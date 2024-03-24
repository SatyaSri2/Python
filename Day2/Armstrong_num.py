#Armstrong Number
n=153
temp=n
temp1=n
count=0
sum=0
while n>0:
    n=n//10
    count+=1
    print(count)
while temp>0:
    num=temp%10
    sum=sum+(num**count)
    temp=temp//10
print(sum)
if temp1==sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
