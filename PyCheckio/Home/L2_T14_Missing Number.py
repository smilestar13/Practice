def missing_number(items: list[int]) -> int:
    items = sorted(items)
    start = items[0]
    finish = items[-1]
    difference = (items[-1] - items[0]) // len(items)
    res = []
    while finish != start:
        res.append(start)
        start += difference

    for el in res:
        if el not in items:
            return el


print("Example:")
print(missing_number([2, 4, 8]))

# These "asserts" are used for self-checking
assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")

