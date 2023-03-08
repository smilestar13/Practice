def safe_pawns(pawns: set) -> int:
    abc = ['OutOfRange', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'OutOfRange']

    defend_count = 0
    for el in pawns:
        pos_1 = abc[abc.index(el[0]) - 1] + str(int(el[1]) - 1)
        pos_2 = abc[abc.index(el[0]) + 1] + str(int(el[1]) - 1)
        if pos_1 in pawns or pos_2 in pawns:
            defend_count += 1
    return defend_count


print("Example:")
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

assert safe_pawns({"d2", "f4", "d4", "b4", "e3", "g5", "c3"}) == 6
assert safe_pawns({"f4", "g4", "d4", "b4", "e4", "e5", "c4"}) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")

