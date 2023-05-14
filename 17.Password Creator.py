import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
sim = "!@#$%^&*()_+-={}[]?><,/\|"
num = "012345789"
all = lower + upper + sim + num


while True:
    print("Choose an Option:\n\t1) Create a Password\n\t2) Exit")
    choice = int(input("Enter: "))

    if choice == 1:
        length = int(input("Length of Password: "))
        cp = "".join(random.sample(all, length))
        print("\nYour password is:", cp, "\n", "*" * 15, "\n")

    elif choice == 2:
        print("\nHope to meet\n" + "*" * 12 + "\n")
        break

    else:
        print("\nYour Option Is Wrong!\nTry Again...\n" + "*" * 21 + "\n")
