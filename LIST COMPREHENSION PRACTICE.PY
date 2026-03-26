num=int(input("ENTER THE NUMBER:"))
num1=[]
odd_num=[i for i in range(1,num) if i%2!=0]
print("odd nos.:",list(odd_num))

list=list(odd_num)
print("New list:",list)


list=["apple","banana","grapes","cherry","orange"]
print("ORIGINAAL LIST:",list)
string=[ list.capitalize() for list in list]
print("updated list:",string)
