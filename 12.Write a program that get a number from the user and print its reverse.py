e = input("Enter Number: ")
s = ""

for i in range(len(e)-1, -1, -1):
    s += e[i]

p = int(s)
print(p)