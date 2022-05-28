result = []


def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a / b

try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
    for key in data:
        res = divider(key, data[result])
        result.append(res)
except BaseException as error:
    print(type(error).__name__+": "+str(error))
print(result)