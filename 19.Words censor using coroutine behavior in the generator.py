def cen_gn(words):
    print("start!")
    w = None
    while True:
        word = yield w
        if word not in words:
            w = word
        else:
            w = "*" * len(word)


g = cen_gn(["khar", "asb", "gav"])

next(g)
print(g.send("mamad"))
print(g.send("khar"))
print(g.send("reza"))
print(g.send("asb"))
print(g.send("gav"))