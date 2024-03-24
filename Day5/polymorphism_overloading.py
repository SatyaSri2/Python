#polymorphism
##overloading means same name diff parameters
class arthematic:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
obj=arthematic()
obj.add(10)
obj.add(10,20)
obj.add(1,2,4)
#python doesn't support function overloading       
