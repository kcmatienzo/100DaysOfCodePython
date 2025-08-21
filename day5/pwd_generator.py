import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input(f"How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# generated_pwd = []

# while len(generated_pwd) < nr_letters:
#     generated_pwd.append(random.choice(letters))
    
# while len(generated_pwd) < (nr_letters + nr_numbers):
#     generated_pwd.append(random.choice(numbers))
    
# while len(generated_pwd) < (nr_letters + nr_numbers + nr_symbols):
#     generated_pwd.append(random.choice(symbols))

# print(generated_pwd)

 

### SOLUTION FROM ANGELA ###

# password = ""

# # ex. nr_letters = 4

# for char in range(0, nr_letters):
#     password += random.choice(letters)

# for char in range(0, nr_letters):
#     password += random.choice(numbers)

# for char in range(0, nr_letters):
#     password += random.choice(symbols)

# print(password)

# text = password
# letters = list(password)
# random.shuffle(letters)
# shuffled = "".join(letters)
# print(shuffled)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []

for char in range(0, nr_letters):
    password_list += random.choice(letters)

for char in range(0, nr_letters):
    password_list += random.choice(numbers)

for char in range(0, nr_letters):
    password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)
# shuffled = "".join(letters)
print(password_list)
shuffled = "".join(password_list)
print(shuffled)
