class placements:
    def info(self):
        print("we have 623 selects and still counting")


class department(placements):
    def display(self):
        departments=["CSE","DS","IT","MECH","CIVIL","AI","AIML"]
        print("The names of Departments are:",departments)
obj2=department()
class pragati(placements):
    def welcome(self):
        print("welcome to Pragati we have glad to have you on board")
obj3=pragati()
obj3.welcome()
obj2.display()
obj3.info()
