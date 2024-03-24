##fibnocci series using for loop of first 10 numbers
prev2=0
prev1=1
print(prev2)
print(prev1)
for i in range (8): #for i in range(3,11)
    fibnoci=prev2+prev1
    prev2=prev1
    prev1=fibnoci
    print(fibnoci)
