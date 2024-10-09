age=int(input("What is your Age: "))
if age>=0 and age<150:
    member=input("Are you a Member? Yes or No: ")
    if age<18 and member=="Yes":
        print("The Fee is 450.00 Pesos.")
    elif age<18 and member=="No":
        print("The Fee is 650.00 Pesos.")
    if 65>age>=18 and member=="Yes":
        print("The Fee is 550.00 Pesos")
    elif 65>age>=18 and member=="No":
        print("The Fee is 750.00 Pesos")
    if age>65 and member=="Yes":
        print("The Fee is 400.00 Pesos")
    elif age>65 and member=="No":
        print("The Fee is 600.00 Pesos")
else:
    if age>150:
        print("Age is Invalid")
