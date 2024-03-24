n=1578
temp=n
count=0
sum=0
while n>0:
    n=n//10
    count+=1
while temp>0:
    num=temp%10
    sum=sum+(num**count)
    temp=temp//10
    count=count-1
print(sum)
