##create a cls of name placements which has a func infowhich displays we have 623 selects and still counting.
##create another cls name dept withfunc display which will display the names of depts present in the clg
##create a cls pragati with a func welcome which displays the msg welcome to pec we have glad to have u on board
##pragati cls should also display the details about depts and the placements
class placements:
    def info(self):
        print("we have 623 selects and still counting")


class department(placements):
    def display(self):
        departments=["CSE","DS","IT","MECH","CIVIL","AI","AIML"]
        print("The names of Departments are:",departments)

class pragati(department):
    def welcome(self):
        print("welcome to Pragati we have glad to have you on board")
obj3=pragati()
obj3.welcome()
obj3.display()
obj3.info()

