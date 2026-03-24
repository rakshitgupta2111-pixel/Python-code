s1=[1,2,3]
s2=['b','a','c']
s3=list(zip(s1,s2))
print(s3)

list1=[10,20,30,40]
list2=[100,200,300,400]
list3=list(zip(list1,list2[::-1]))
print(list3)

stock=['reliance','infosys','tcs']
price=[2175,1127,2750]
new_dict={stock: price for stock, price in zip(stock,price)}
print('{}'.format(new_dict))
