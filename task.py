import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# for el in range(0,nr_letters):
#     print(random.choice(letters),end="")
#
#
# for el in range(0,nr_symbols):
#     print(random.choice(symbols),end="")
#
# for el in range(0,nr_numbers):
#     print(random.choice(numbers),end="")

# hard way

passward_char = []
myPassward = ""

for el in range(0,nr_letters):
    passward_char.append(random.choice(letters))


for el in range(0,nr_symbols):
    passward_char.append(random.choice(symbols))

for el in range(0,nr_numbers):
    passward_char.append(random.choice(numbers))


number = nr_letters + nr_numbers + nr_symbols
for el in range(0,number) :
    variable = random.choice(passward_char)
    myPassward += variable
    passward_char.remove(variable)
    number = number - 1


print(myPassward)

