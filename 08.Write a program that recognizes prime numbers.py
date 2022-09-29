n = int(input("Enter Number: "))

i = 2

if n > 1:
    while i < n:
        if n % i == 0:
            print(n, "is not a prime number!")
            break
        i += 1
    else:
        print(n, "is a prime number!")
else:
    print(n, "is not a prime number!")