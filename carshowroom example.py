##toyota,mahedra,mercedes
##1st func:take the i/p from user for car company name and in i/p msg give user 3 options of companies
##this user i/p company name goes as the i/p /arg to model name func,
##which welcomes the user accordingly to the cmpyname.ask user to enter the specific model name for that cmpy
##2nd func: whose name is variant accd to the company name and car model the user should be asked to
##enter the variant he would like to chose from petrol and diesel
##3rd func:display func accd to the car cmpy,car modelname and car variant
##first its ex-showroom price should be displayed and thenits onroad price should be dispalyed,
##which is calculated as ex-SR price+CGST+SGST+ins
##the SGST,CGSTand Ins all the 3 have Common value througout the carshowroom
class CarShowRoom:
    def __init__(self,a):
        a=a.lower()
        if a=='1'or a=='toyota':
            self.a='toyota'
            print("Welcome to Toyota family")
        elif  a=='2'or a=='mahindra':
            self.a='mahindra'
            print("Welcome to Mahindra family")
        elif  a=='3'or a=='mercedes':
            self.a='mercedes'
            print("Welcome to Mercedes family")
    def toyota(self):
        while True:
            t=input("enter one of the given options for car model 1.Glanza 2.Innova:")
            t=t.lower()
            if t=='glanza'or t=='1':
                self.t='glanza'
                break
       
            elif t=='innova'or t=='2':
                self.t='innova'
                break
            else:
                print("please try again")
    def mahindra(self):
        while True:
            m=input("enter one of the given options for car model 1.SUV700 2.Scorpio:")
            m=m.lower()
            if m=='suv700'or m=='1':
                self.m='suv700'
                break
            elif m=='scorpio'or m=='2':
                self.m='scorpio'
                break
            else:
                print("please try again")
    def mercedes(self):
        while True:
            me=input("enter one of the given options for car model 1.SUV 2.AMG:")
            me=me.lower()
            if me=='suv'or me=='1':
                self.me='suv'
                break
            elif me=='amg'or me=='2':
                self.me='amg'
                break
            else:
                print("please try again")
    def variant(self):
        while True:
            k=input("enter one of the given options for car variant 1.Petrol 2.Diesel:")
            k=k.lower()
            if k=='petrol'or k=='1':
                self.k='petrol'
                break
            elif k=='diesel'or k=='2':
                self.k='diesel'
                break
            else:
                print("please try again")
    def display(self):
        if self.a=='toyota' and self.t=='glanza' and self.k=='petrol':
            print("Your car Company is:",self.a,"Car Model is:",self.t,"Vaariant is:",self.k)
            x=200000
            print("VAG ShowRoomPrice is:",x)
            onroadprice=x+3*(x*10/100)
            print("onroad price is:",onroadprice)
        if self.a=='toyota' and self.t=='glanza' and self.k=='diesel':
            print("Your car Company is:",self.a,"Car Model is:",self.t,"Vaariant is:",self.k)
            x=300000
            print("VAG ShowRoomPrice is:",x)
            onroadprice=x+3*(x*11/100)
            print("onroad price is:",onroadprice)
        elif self.a=='toyota' and self.t=='innova' and self.k=='petrol':
            print("Your car Company is:",self.a,"Car Model is:",self.t,"Vaariant is:",self.k)
            x=210000
            print("VAG ShowRoomPrice is:",x)
            onroadprice=x+3*(x*12/100)
            print("onroad price is:",onroadprice)
        elif self.a=='toyota' and self.t=='innova' and self.k=='diesel':
            print("Your car Company is:",self.a,"Car Model is:",self.t,"Vaariant is:",self.k)
            x=220000
            print("VAG ShowRoomPrice is:",x)
            onroadprice=x+3*(x*13/100)
            print("onroad price is:",onroadprice)
        elif self.a=='mahindra' and self.m=='scorpio' and self.k=='petrol':
            print("Your car Company is:",self.a,"Car Model is:",self.m,"Vaariant is:",self.k)
            x=250005
            print("VAG ShowRoomPrice is:",x)
            onroadprice=x+3*(x*14/100)
            print("onroad price is:",onroadprice)
        elif self.a=='mahindra' and self.m=='scorpio' and self.k=='diesel':
            print("Your car Company is:",self.a,"Car Model is:",self.m,"Vaariant is:",self.k)
            x=280007
            print("VAG ShowRoomPrice is:",x)
            onroadprice=x+3*(x*12/100)
            print("onroad price is:",onroadprice)
        elif self.a=='mahindra' and self.m=='suv700' and self.k=='petrol':
            print("Your car Company is:",self.a,"Car Model is:",self.m,"Vaariant is:",self.k)
            x=250000
            print("VAG ShowRoomPrice is:",x)
            onroadprice=x+3*(x*10/100)
            print("onroad price is:",onroadprice)
        elif self.a=='mahindra' and self.m=='suv700' and self.k=='diesel':
            print("Your car Company is:",self.a,"Car Model is:",self.m,"Vaariant is:",self.k)
            x=280000
            print("VAG ShowRoomPrice is:",x)
            onroadprice=x+3*(x*11/100)
            print("onroad price is:",onroadprice)
        elif self.a=='mercedes' and self.me=='suv' and self.k=='petrol':
            print("Your car Company is:",self.a,"Car Model is:",self.me,"Vaariant is:",self.k)
            x=750000
            print("VAG ShowRoomPrice is:",x)
            onroadprice=x+3*(x*13/100)
            print("onroad price is:",onroadprice)
        elif self.a=='mercedes' and self.me=='suv' and self.k=='diesel':
            print("Your car Company is:",self.a,"Car Model is:",self.me,"Vaariant is:",self.k)
            x=780001
            print("VAG ShowRoomPrice is:",x)
            onroadprice=x+3*(x*15/100)
            print("onroad price is:",onroadprice)
        elif self.a=='mercedes' and self.me=='amg' and self.k=='petrol':
            print("Your car Company is:",self.a,"Car Model is:",self.me,"Vaariant is:",self.k)
            x=550002
            print("VAG ShowRoomPrice is:",x)
            onroadprice=x+3*(x*12/100)
            print("onroad price is:",onroadprice)
        elif self.a=='mercedes' and self.me=='amg' and self.k=='diesel':
            print("Your car Company is:",self.a,"Car Model is:",self.me,"Vaariant is:",self.k)
            x=580003
            print("VAG ShowRoomPrice is:",x)
            onroadprice=x+3*(x*20/100)
            print("onroad price is:",onroadprice)
while(True):
    i=input("enter one of the given options for car companies 1.Toyota 2.Mahindra 3.Mercedes:")
    if i=='Toyota'or i=='1'or i=='toyota' or i=='Mahindra'or i=='2' or i=='mahindra'or i=='Mercedes' or i=='3'or i=='mercedes':
        break
    else:
        print("please try again")
obj=CarShowRoom(i)
if i== 'Toyota'or i=='1'or i=='toyota':
    obj.toyota()
    obj.variant()
    obj.display()
elif i== 'Mahindra'or i=='2' or i=='mahindra':
    obj.mahindra()
    obj.variant()
    obj.display()
else:
    obj.mercedes()
    obj.variant()
    obj.display()


