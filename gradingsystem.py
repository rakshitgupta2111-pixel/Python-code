print("Enter the Marks obtained in 5 subjects")
markone=int(input())
marktwo=int(input())
markthree=int(input())
markfour=int(input())
markfive=int(input())

total=markone+marktwo+markthree+markfour+markfive
avg=total/5

if avg>=91 and avg<=100:
    print("Your grade is A1")
    print("Your average is=" , avg)
elif avg>=81 and avg<=90:
    print("Your grade is A2")
    print("Your average is=" , avg)
elif avg>=71 and avg<=80:
    print("Your grade is B1")
    print("Your average is=" , avg)
elif avg>=61 and avg<=70:
    print("Your grade is B2")
    print("Your average is=" , avg)
elif avg>=51 and avg<=60:
    print("Your grade is C1")
    print("Your average is=" , avg)
elif avg>=41 and avg<=50:
    print("Your grade is C2")
    print("Your average is=" , avg)
elif avg>=33 and avg<=40:
    print("Your grade is D")
    print("Your average is=" , avg)
elif avg>=20 and avg<33:
    print("Your grade is E1")
    print("Your average is=" , avg)
elif avg<=19:
    print("Your grade is E2")
    print("Your average is=" , avg)
else:
    print("invalid input")