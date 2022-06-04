def raise_to_the_degrees(number):
    i = 0
    while True:
        yield number**i
        i += 1
res = raise_to_the_degrees(12)
print(res)
for _ in range(100):
    print(next(res))