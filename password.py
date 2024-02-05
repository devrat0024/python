import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g',' h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A',' B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '<', '>', '?', '/', '+']
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

print("Welcome to the password generator!")

letter_generated = int(input("How many letters do you want?\n"))
symbol_generated = int(input("How many symbols do you want?\n"))
number_generated = int(input("How many numbers do you want?\n"))

total_length = letter_generated + symbol_generated + number_generated

if total_length == 0:
    print("You must specify at least one type of character.")
    exit()

password_list = []

for _ in range(letter_generated):
    char = random.choice(letters)
    password_list.append(char)

for _ in range(symbol_generated):
    char = random.choice(symbols)
    password_list.append(char)

for _ in range(number_generated):
    char = random.choice(numbers)
    password_list.append(char)

random.shuffle(password_list)

password = ''.join(password_list)
print("Generated password:", password)

