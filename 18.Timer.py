import time
from os import system, name

while True:
    choice_time = input("Do you Want to start? (y/n): ")
    if "y" in choice_time.lower():
        hours = int(input("Enter Amount Of Hours: "))
        minutes = int(input("Enter Amount Of minutes: "))
        Seconds = int(input("Enter Amount Of Seconds: "))
        total = hours * 60 * 60 + minutes * 60 + Seconds

        print("Timer Start Now ...")
        time.sleep(1)
        if name == "nt":
            system("cls")
        else:
            system("clear")
        while total >= 0:
            print(total)
            total -= 1
            time.sleep(1)
            if name == "nt":
                system("cls")
            else:
                system("clear")
        print("\nFinished!\n")

    elif "n" in choice_time.lower():
        print("\nHope to meet\n" + "*" * 12 + "\n")
        break

    else:
        print("\nYour Choice Is Wrong!\nTry Again...\n")
