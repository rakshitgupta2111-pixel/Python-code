units=int(input("Enter the units you consumed: "))

if (units < 50):
    amount= units* 2.60
    surcharged=25

elif (units <= 100):
    amount= 130 + ((units-50) * 3.25)
    surcharged= 35

elif (units <= 200):
    amount= 130 + 162.50 + ((units-100) * 5.26)
    surcharged= 45

else:
    amount= 130 + 162.50 + 526 + ((units-200) * 8.54)
    surcharged= 75

total=amount+surcharged
 
print("Your electricity bill is:" , total)
