from random import choice

coin = ["shir", "khat"]

sh = 0
kh = 0

for _ in range(1000):
    r = choice(coin)
    if r == "shir":
        sh += 1
    else:
        kh += 1

print("shir:", sh, "\t", "khat:", kh)