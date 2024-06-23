print("Thank you for choosing Python Pizza Deliveries!!")

size=input("What size pizza do you want ? S,M or L      : ")
add_pepperoni=input("Do you want pepperoni ? Yy or Nn   : ")
extra_cheese=input("Do you want extra cheese ? Yy or Nn : ")

Smallpizza=15
Mediumpizza=20
Largepizze=30
sum=0
if size=='S' or size=='s':
    sum+=15
elif size=='M' or size=='m':   
    sum+=20
elif size=='L' or size=='l':   
    sum+=25
else:
    print("You didn't choose size !")
    add_pepperoni=0
    extra_cheese=0
if add_pepperoni==0:
    print("Your didnt choose pepperoni")
else:
    if add_pepperoni=='Y' or add_pepperoni=='y':
        if size=='S' or size=='s':
            sum+=2
        else:
            sum+=3
if extra_cheese==0:
    print("Your didnt choose size of cheese")
else:
    if extra_cheese=='Y' or extra_cheese=='y':
        sum+=1

    print("Thank you for choosing Python Pizza Deliveries !")
    print(f"Your final bill is :${sum}")