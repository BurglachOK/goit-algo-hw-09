'This code is an attempt to implement insertion sort on a linked list using index access. '
'It is not the most efficient way to do it, but it serves as a reminder of the approach I tried'
'it is less efficient'

def backtrax(res, target):
    result = coinification()
    index = 0
    a = res[-1]
    while not target <= 0:
        for i in res[::-1][1:]:
            index += 1
            if a - 1 == i:
                result[index] += 1
                target -= index
                a = i
                index = 0
    return result


def coinification():
    result = {}
    for coin in coins:
        result[coin] = 0
    return result