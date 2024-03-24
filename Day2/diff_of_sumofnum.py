##calculate the diff of sum of num that are div by 6 and not div by 6
##on the range of first 30 num's
sum=0
s=0
for i in range(1,31):
    if i%6==0:
        sum+=i
    else:
        s+=i
print("div by 6:",sum)
print("not div by 6:",s)
diff=s-sum
print("Difference:",diff)
  
