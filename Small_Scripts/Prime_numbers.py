def paint_calc(height,width,cover):
    num_of_can=round((height*width)/cover)
    print(f"You'll need {num_of_can} cans of paint.")


#test_h=int(input("Height of wall is : "))
#test_w=int(input("Width of wall is : "))

coverage=5
#paint_calc(height=test_h,width=test_w,cover=coverage)



def primecheck(num):
    is_prime=True
    for i in range(2,num):
        
        if num%i==0:
            is_prime=False
    if is_prime:
        print("ITS A PRIME NUMBER !")
    else:
        print("ITS NOT A PRIME NUMBER !")

number=int(input("Give a number "))
primecheck(number)