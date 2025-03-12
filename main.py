import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input(f"How many symbols would you like?\n"))
n_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

# select n_letters of random letter
for letter in range(n_letters):
    password_list.append(random.choice(letters))

# select n_symbol of random symbol
for symbol in range(n_symbols):
    password_list.append(random.choice(symbols))

# select n_number of random number
for number in range(n_numbers):
    password_list.append(random.choice(numbers))

# print password list
print(f"Password = {password_list}")

# shuffle the password inplace
random.shuffle(password_list)

# convert a list into a str
print("PW = ", "".join(password_list))




