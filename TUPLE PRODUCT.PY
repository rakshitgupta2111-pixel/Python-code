tuple1=(4,3,2,2,-1,18)
tuple2=(2,4,8,8,3,2,9)

def tuple_product(t):
    product=1
    for num in t:
        product=product*num
    return product


print("Tup1",tuple_product(tuple1))
print("Tup2",tuple_product(tuple2))
    