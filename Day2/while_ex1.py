n=12345
count=0
add=0
mul=1
while n>0:
    a=n%10
    print(a)
    add+=a
    mul*=a
    n=n//10
    count+=1
print("Sum of digits:",add)
print("Mul of digits:",mul)
print("No of digits:",count)
