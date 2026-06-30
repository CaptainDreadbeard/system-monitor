import random
print("random password generator")
# ask the user how long theyre password is 
length = int(input("how long is your password?: "))

# possible options of password characters
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbol = "`~!@#$%^&*()_-+={|}:;,<?/>"

# list of characters in password
password_chars = []

# how to guarantee one character from each list
password_chars.append(random.choice(lowercase))
password_chars.append(random.choice(uppercase))
password_chars.append(random.choice(numbers))
password_chars.append(random.choice(symbol))
# -4 length
all_chars = lowercase + uppercase + numbers + symbol

random.shuffle(password_chars)

password = "".join(password_chars)

for i in range(length - 4):
    password += random.choice(all_chars)

print("Your strong password is: ", password)
