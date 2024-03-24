##write program to find the 2nd smallest neg num from list
list=[22,42,65,1,-4,6,-1]
print(list)
min0=list[0]
min1=list[0]
#method_1
for i in range(len(list)):
    if list[i]<min0:
        min0=list[i]
for i in range(len(list)):
    if list[i]<min1 and list[i]!=min0:
        min1=list[i]
        
print("The 2nd smallest neg num:",min1)
#method_2
for i in range(len(list)):
    if list[i]<min0:
        min1=min0
        min0=list[i]
    elif min1>list[i] and min1>min1:
        min1=list[i]
print("The 2nd smallest neg num:",min1)
