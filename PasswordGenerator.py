import random
import string

#user input
length = int(input("Enter desired password length: "))

#character sets
all_chars = string.ascii_letters + string.digits + string.punctuation

#generate password
password = ''.join(random.choice(all_chars) for _ in range(length))

print("Generated password: ", password)