####write a recursive func to count the num of digits of a num
##write the recursive func to calculate the sum of digits of a num
def count(num):
    if num==0:
        return 0
    return num%10+count(num//10)#return 1+count(num//10)
print(count(1234))

    
