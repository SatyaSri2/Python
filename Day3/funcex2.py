def func(a=7,b=8):
    print("The values of a and b:",a, b)
func()
func(10,15)
func(b=35,a=45)
def func(**a):
   print("The value of b:",a["value2"])
func(value1=40,value2=89)
