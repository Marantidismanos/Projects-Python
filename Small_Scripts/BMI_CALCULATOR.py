print("Welcome to a simple BMI calculator !! \n")
height = float(input("Give me your height in m.   (e.g. 1.75m) : \n"))
weight = float(input("Give me your weight in kg.  (e.g. 70.5)  : \n"))

BMI=weight/(height*height)


if BMI<18.5:
    print(f"Your BMI score is :{BMI} ,you are  Underweight !")
elif BMI>=18.5 and BMI<=24.9:
    print(f"Your BMI score is :{BMI} ,you are  Normal weight !")
elif BMI>25 and BMI<=29.9:
    print(f"Your BMI score is :{BMI} ,you are slightly Overweight !")
elif BMI>30 and BMI<35:
    print(f"Your BMI score is :{BMI} ,you are  Obese")
else:
    print(f"Your BMI score is :{BMI} ,you are  clinically Obese")


