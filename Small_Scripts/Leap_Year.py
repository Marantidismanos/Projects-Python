# A normal year has 365 days,Leap year have 366 ,with an extra day in February .
year=int(input("Which year do you want to check ? "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("This year is Leap !")
        else:
            print("This year isn't Leap")
    else:
        print("This year is Leap !")
else:
    print("This year isn't Leap !")
    