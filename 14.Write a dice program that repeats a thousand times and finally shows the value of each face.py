from random import randint

tas = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for _ in range(1000):
    tas[randint(1, 6)] += 1

print(tas)