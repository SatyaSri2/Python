##write a login func which accepts the user only when the user name and PW are same
##and displays a msg log in successful
##otherwise it keeps asking the user to enter the credentials until they are correct
def func():
    while True:
        user=input("Enter user name:")
        password=input("Enter Password:")
        if user==password:
          print("Log in successful")
          break
        else:
            print("login credentials are wrong please try again")
func()
    
##using recursion
def login():
        user=input("Enter user name:")
        password=input("Enter Password:")
        if user==password:
          print("Log in successful")
          break
        else:
            print("login credentials are wrong please try again")
            login()
login()
    
