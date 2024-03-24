##write a program to check the on road price for a bike under then conditions
##if the price is >than 72000 then  tax is 10%  insurance will be 15% 
##if the price is > than 150000 and < 200000 then tax would be 25%,ins willbe 20%
##if the price is above 200000 then tax will be 35% and ins will 28%
##otherwise print enter a valid price
price=int(input("Enter the price:"))
if price>=72000 and price<=150000:
    tax=price*(10/100)
    ins=price*(15/100)
    onroadprice=price+tax+ins
    print("On road price of bike:",onroadprice)
elif price>150000 and price<=200000:
    tax=price*(25/100)
    ins=price*(20/100)
    onroadprice=price+tax+ins
    print("On road price of bike:",onroadprice)
elif price>200000:
    tax=price*(35/100)
    ins=price*(28/100)
    onroadprice=price+tax+ins
    print("On road price of bike:",onroadprice)
else:
    print("please Enter a valid price")
    
