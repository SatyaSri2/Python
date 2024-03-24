##create a cls ticket which will be the abstract class
##inside that create a func  book ticket which will be abstract method and have nothing in it
##create a cls makemytrip which will use the book ticket func from ticket cls to take the details such as name,phnno,emailid,journey date and 
##displayes a msg saying thank you for booking from makemytrip.
##create a cls irctc which uses the book tickect of ticket cls and takes the same details as makemytrip but in the end it'll give an optiin to user to select whether it is one way or round trip
##if the user option is round trip it again asks the user to enter the return date as well and then print the msg thank you for chosing irctc else it prints thank you for chosing irctc.
##create a cls indigo which takes all the details as irctc and just asks which mode of transport you are to going train,flightor bus and display thank you for chosing indigo
from abc import ABC,abstractmethod
class ticket(ABC):
    @abstractmethod
    def bookticket(self):
        pass
class makemytrip(ticket):
    def bookticket(self):
        name=input("enter your name:")
        phoneno=int(input("Enter your 10 digit phone number:"))
        emailid=input("Enter your email ID:")
        journeydate=int(input("Enter the journey date:"))
        print("Thank you for booking from makemytrip")
class irctc(ticket):
    def bookticket(self):
        name=input("enter your name:")
        phoneno=int(input("Enter your 10 digit phone number:"))
        emailid=input("Enter your email ID:")
        journeydate=int(input("Enter the journey date:"))
        
        print("please select you way of trip: 1.one way trip 2.round trip")
        trip=input("Enter your choice 1 or 2:")
        trip=trip.lower()
        if trip=='2' or trip=="round trip":
            returndate=input("Please enter your return date:")
        print("Thank you for chosing irctc")
        else:
            print("Thank you for chosing irctc")
class indigo(irctc):
    def bookticket(self):
        name=input("enter your name:")
        phoneno=int(input("Enter your 10 digit phone number:"))
        emailid=input("Enter your email ID:")
        journeydate=int(input("Enter the journey date:"))
        print("please select you way of trip: 1.one-way trip 2.round trip")
        trip=input("Enter your choice 1 or 2:")
        trip=trip.lower()
        if trip=='2' or trip=="round trip":
            returndate=input("Please enter your return date:")
        elif trip=='1' or trip=="one way":
            pass
        elif 
            
            
        
            
        
