##check in if the give yr is leap yr or not
##if yr is divis by 4 and not divis by 100 or if it div by 400 then it is leap yr
yr=int(input("enter the year:"))
if yr%4==0 and yr%100!=0 or yr%400==0:
    print(yr," is leap year")
else:
    print("this is not a leap year")
    
