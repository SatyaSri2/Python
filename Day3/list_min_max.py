##addition of the min values and max values
#replace the sum with  max value
#replace the subtraction value with min value
replace the max with addition num and min with subtraction  num
list=[12,42,23,96,7,18,10,133]
min=list[0]
max=list[0]
for i in range(1,len(list)):
   if min>list[i]:
       min=list[i]
       minid=i
    if max<list[i]:
       max=list[i]
       maxid=i
print(min,minid)
