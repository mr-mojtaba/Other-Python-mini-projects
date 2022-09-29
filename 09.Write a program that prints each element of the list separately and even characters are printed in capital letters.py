l = ["ali", "reza", "nader", "naser"]
i = 0

while i < len(l):
    s = l[i]
    j = 0
    while j < len(s):
        if j % 2 == 0:
            print(s[j].upper(), end="")
        else:
            print(s[j], end="")
        j += 1
    print()
    i += 1