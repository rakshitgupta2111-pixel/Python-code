import array as arr

array_num=arr.array('i',[1,3,2,4,6,3,9])
print("original array:" +str(array_num))

print("number of occurences of num 3 in array: " +str(array_num.count(3)))

array_num.reverse()
print("Array num after reverse:" ,(array_num))