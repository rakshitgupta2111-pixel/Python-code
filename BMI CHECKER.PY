height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height / 100) ** 2

print("Your BMI is", BMI)

if BMI <= 18.4:
    print("You are underweight.")
    print("BMI=" , BMI)
elif BMI <= 24.9:
    print("You are healthy.")
    print("BMI=" , BMI)
elif BMI <= 29.9:
    print("You are overweight.")
    print("BMI=" , BMI)
elif BMI <= 34.9:
    print("You are severely overweight.")
    print("BMI=" , BMI)
elif BMI <= 39.9:
    print("You are obese.")
    print("BMI=" , BMI)
else:
    print("You are severely obese.")
    print("BMI=" , BMI)
