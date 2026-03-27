import random
import string

length = int(input("Enter the length of password: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits

ch = lower + upper + number

password = random.choices(ch, k=length)

random.shuffle(password)
password=string.join(password)

print("Generated Password:", password)


