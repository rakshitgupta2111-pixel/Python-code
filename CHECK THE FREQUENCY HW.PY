test_dictionary={'codingal':3,'is':2,'best':2,'for':2,'coding':1}
value=int(input("Enter the value for which you want frequency:"))

freq=0

for key in test_dictionary:
    if test_dictionary[key]==value:
        freq=freq+1

print("Frequency of a value is: ",freq)
