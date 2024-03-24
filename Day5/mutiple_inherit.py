class placements:
    def info(self):
        print("we have 623 selects and still counting")


class department:
    def display(self):
        departments=["CSE","DS","IT","MECH","CIVIL","AI","AIML"]
        print("The names of Departments are:",departments)

class pragati(department,placements):
    def welcome(self):
        print("welcome to Pragati we have glad to have you on board")
obj3=pragati()
obj3.welcome()
obj3.display()
obj3.info()
