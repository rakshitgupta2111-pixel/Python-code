amount=int(input("Enter the amount"))

notes_2000=amount//2000
notes_500=(amount%2000)//500
notes_100=((amount%2000)%500)//100
notes_50=(((amount%2000)%500)%100)//50
notes_10=((((amount%2000)%500)%100)%50)//10


print("The notes of 2000" , notes_2000)
print("\n The notes of 500" , notes_500)
print("\n The notes of 100" , notes_100)
print("\n The notes of 50" , notes_50)
print("\n The notes of 10" , notes_10)
