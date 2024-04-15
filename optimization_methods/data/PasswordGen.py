import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

gen_password_list = []

def generate_password():

    # letters
    for _ in range(1, nr_letters + 1):
        gen_password_list.append(random.choice(letters))
    # Symbols
    for _ in range(1, nr_symbols + 1):
        gen_password_list.append(random.choice(symbols))
    # Numbers
    for _ in range(1, nr_numbers + 1):
        gen_password_list.append(random.choice(numbers))

    # Shuffle the list to generate complex password
    random.shuffle(gen_password_list)

    # Create a password string
    gen_password = ""
    for char in gen_password_list:
        gen_password += char

    return gen_password

