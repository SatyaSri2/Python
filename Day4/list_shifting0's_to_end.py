##shift all the zeros to the end
list1=[2,0,1024,0,40,230,0]
n=0
for i in range(len(list1)):
    if list1[i]!=0:
        list1[i],list1[n]=list1[n],list1[i]
        n+=1
print(list1)
#another method 
l2=[]
for i in list1:
    if i!=0:
        l2.append(i)
