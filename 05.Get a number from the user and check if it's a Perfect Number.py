n = int(input("Enter number: "))
i = 1
l = []

while i <= n:
    if n % i == 0:
        l.append(i)
    i += 1

print("Divisors =", l)

if sum(l) - n == n:
    print("This is a Perfect Number ✔")
else:
    print("This isn't a Perfect Number ❌")