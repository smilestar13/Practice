def left_join(phrases: tuple[str]) -> str:
    res = ''
    for el in phrases:
        res += str(el) + ','

    return res.replace('right', 'left')[:-1]


print("Example:")
print(left_join(("bright aright", "ok")))

# These "asserts" are used for self-checking
assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
# assert left_join(("brightness wright",)) == "bleftness wleft"
# assert left_join(("enough", "jokes")) == "enough,jokes"

print("The mission is done! Click 'Check Solution' to earn rewards!")

