#single inheritance
class faculty:#parent class
    def __init__(self,f_name,dept,f_id):
     self.f_name=f_name
     self.dept=dept
     self.f_id=f_id
    def print_info(self):
        print('faculty info=',self.f_name,self.dept,self.f_id)
obj=faculty("ayuish","CSE",1001)
obj.print_info()
class cse(faculty):#child class
    pass
obj=cse("jyothi","DS",1002)
obj.print_info()
