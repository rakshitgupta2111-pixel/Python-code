try:
    age = int(input("Enter your age: "))

    if age == int(age):
       print("Valid age entered.")
    else:
        raise ValueError

    if age % 2 == 0:
        print("The age is EVEN.")
    else:
        print("The age is ODD.")

except ValueError:
    print("Error: Please enter a valid integer age")
