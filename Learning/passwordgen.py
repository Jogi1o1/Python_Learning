import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

char = []
symb = []
nums = []
passw = []
password = ""
for let in range(0,nr_letters):
    random_char = random.choice(letters)
    char.append(random_char)
for sym in range(0,nr_symbols):
    random_sym = random.choice(symbols)
    symb.append(random_sym)
for num in range(0,nr_numbers):
    random_num = random.choice(numbers)
    nums.append(random_num)
passw = char + symb + nums

random.shuffle(passw)
for i in passw:
    password += str(i) 
print(password)
