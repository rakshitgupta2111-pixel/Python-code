Medical_cause=input("Did you have any health cause Y or N: ") 
atten=int(input("The attendance of student is: "))

if Medical_cause == "Y":
    print("You are eligible for exam")
else:
    if atten >= 75:
        print("You are eligible for exam")
    else:
        print("You are not eligible for exam")
        