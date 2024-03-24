##create a cls f15 with func lights,fan,AC
## when lights func is called prints color of the light which is taken as parameter to func
## when fan func is called,it prints regulator speed of the fan taken as para of func
## ac displays the room temp and the outside temp taken as para of func
## write a 4th func whose name is display which display outside temp and room of AC
## and also it displays the fan speed
#creation of constructor
class F15:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("this is a constructor")
        print("Start time is:",a,"o'clock")
        print("End time is:",b,"o'clock")
        
    def lights(self,color):
        print("The color of the light is",color)
        
    def fan(self,regulatorspeed):
        self.speed=regulatorspeed
        print("The regulator speed of the fan is:",regulatorspeed)
        
    def AC(self,roomtemp,outsidetemp):
        self.roomtemp=roomtemp
        self.otemp=outsidetemp
        print("The room temp and outside temp are:",roomtemp,outsidetemp)
        
    def display(self):
        print("The regulator speed of the fan is:",self.speed)
        print("The room temp and outside temp are:",self.roomtemp,self.otemp)
        print("Start time is:",self.a,"o'clock")
        print("End time is:",self.b,"o'clock")
    
obj=F15(9,4)
obj.lights("white")
obj.fan(4)
obj.AC(27,34)
obj.display()
