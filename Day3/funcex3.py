##write a func to calculate sum of 1st and last digit of a num
##the should be taken as argu
def func(num):
    n=num%10
    while num>10:
        num=num//10
    sum=num+n
    print("Sum  of digits:",sum)
func(118)
        
    
