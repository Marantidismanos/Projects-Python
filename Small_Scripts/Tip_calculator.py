print("Welcome to the Tip Calculator ! \n")
sum=float(input("What was the total bill ? : $"))
tip=float(input("How much tip would you like to give ? 10%,12%,15%? : \n"))
persons=int(input("How many people to split the bill? : \n"))
tip_per=tip/100
caltip_sum=sum*tip_per
Total_bill=sum+caltip_sum
print(f"The Total Price with Tip is : {Total_bill} \n")
PerToPay= round((Total_bill/persons),2)
print(f"Each Person should pay : ${PerToPay}")