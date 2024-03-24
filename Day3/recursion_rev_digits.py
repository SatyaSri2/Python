##write a recursion program to print digits in a reverse order
def rev(num):
    if num==0:
        return
    print(num%10)
    return rev(num//10)
rev(159)
        
