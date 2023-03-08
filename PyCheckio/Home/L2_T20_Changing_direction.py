def changing_direction(elements: list[int]) -> int:
    if len(elements) > 1:
        trend_change = 0
        i = 0
        j = 0
        x = 0
        while True:
            if elements[x] > elements[x+1]:
                j += 1
                break
            elif elements[x] == elements[x+1]:
                x += 1
                continue
            else:
                break

        while i < len(elements) - 1:
            current = elements[i]
            step = elements[i + 1]
            if current < step and trend_change % 2 != 0:
                trend_change += 1
            elif current > step and trend_change % 2 == 0:
                trend_change += 1
            i += 1
        return trend_change - j
    else:
        return 0


print("Example:")
print(changing_direction([6, 6, 6, 4, 1, 2, 5, 9, 7, 8, 5, 9, 4, 2, 6]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")

