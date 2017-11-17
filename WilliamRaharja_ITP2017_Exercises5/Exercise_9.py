def generator(n):
    while n > 0:
        yield n
        n -= 1
for a in generator(20):
    print(a)


