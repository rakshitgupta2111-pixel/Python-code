import random
playing=True
number=(random.randint(10,20))

print("I will generate a number 10-20 and you have to guess it one at a time.")

while playing:
    guess=int(input("Give me your best guess"))
    if number==guess:
        print("correct guess..great")
        break

    else:
        print("Your guess was not correct...try again")
        
