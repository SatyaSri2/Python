##creation of dict
##atleast 4 key value pairs
##accessing the whole dict using for loops
## add duplicate values and keys and check
## change an exisiting value and keys
## remove an key value pair
dict={'a1':43,'a2':45,'a3':"Satya",'a4':"sri"}
print(dict)
print("accessing the dict:",dict["a3"])
for i,j in dict.items():
    print(i,j)
dict1={1:14,2:45,3:78,1:16}
print(dict1)
dict["a1"]=46
print("Changing Existing value",dict)
print("removing key value pair:",dict.pop('a4'))
print(dict)
