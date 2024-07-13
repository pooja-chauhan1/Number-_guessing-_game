import random
Cnumber=random.randrange(1,101)
userinput=int(input("enter your number  "))

if userinput>Cnumber:
    print("computer number=",Cnumber)
    print("Your number is greater than computer number ")

elif userinput<Cnumber:
    print("computer number=",Cnumber)
    print("Your number is smaller than computer number ")
    
else:
    print("computer number=",Cnumber)
    print("Your number is equal to computer number ")    
        