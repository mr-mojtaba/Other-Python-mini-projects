m = float("inf")

while True:
    n = float(input("Enter Number: "))
    if n < m:
        m = n

    s = input("Do You Continue?")
    if s.lower() == "no":
        break

print(m, "is smallest number !")
