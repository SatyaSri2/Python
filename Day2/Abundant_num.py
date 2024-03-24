##take a num input from user check
##if the sum of factors of that num is greater than the original num
##if yes  print yes or else no
n=int(input("Enter the Number"))
sum=0
for i in range(1,n//2+1):
    if n%i==0:
      sum=sum+i
print("Sum of Factors")
if n<sum:
    print("YES")
else:
    print("NO")    
    
