def nearest_value(values: set[int], one: int) -> int:
    if one in values:  # Если число уже есть в искомом диапазоне:
        return one

    elif one not in values:  # Если числа нет в искомом диапазоне, нужно его туда интегрировать:
        values.add(one)
        values = sorted(values)

        ind_y = values.index(one)
        ind_z = ind_y + 1
        ind_s = ind_y - 1

        if ind_y != 0 and one != values[-1]:  # Если число не выпадает на крайнюю позицию:
            if values[ind_z] - values[ind_y] < values[ind_y] - values[ind_s]:
                return values[ind_z]
            else:
                return values[ind_s]
        elif ind_y == 0:  # Если число выпадает на край списка:
            return values[ind_y + 1]
        else:
            return values[ind_y - 1]


print("Example:")
print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

assert nearest_value({17, 4, 7, 10, 11, 12}, 9) == 10
assert nearest_value({17, 4, 7, 10, 11, 12}, 8) == 7
assert nearest_value({17, 4, 8, 10, 11, 12}, 9) == 8
assert nearest_value({17, 4, 9, 10, 11, 12}, 9) == 9
assert nearest_value({17, 4, 7, 10, 11, 12}, 0) == 4
assert nearest_value({17, 4, 7, 10, 11, 12}, 100) == 17
assert nearest_value({100, 5, 8, 89, 10, 12}, 7) == 8
assert nearest_value({2, 3, -1}, 0) == -1
assert nearest_value({5}, 5) == 5
assert nearest_value({5}, 7) == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")
