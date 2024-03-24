##write the code of armstrong num using recursion
def count(num):
   if num==0:
       return 0
   return 1+count(num//10)
c=count(153)
print("Count:",c)
def armstrong(n,count):
     if n==0:
         return 0
     return n%10**count+armstrong(n//10,count)
armstrong(153,a)
