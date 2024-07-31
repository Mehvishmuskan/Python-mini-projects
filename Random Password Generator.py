import random
import string
password_length=8
Values=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(password_length):
    password+=random.choice(Values)
print("Your Random Password is:",password)