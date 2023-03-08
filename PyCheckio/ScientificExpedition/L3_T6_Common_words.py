def checkio(line1: str, line2: str) -> str:
    res_set = sorted(set(line1.split(',')).intersection(set(line2.split(','))))
    return ','.join(res_set)


print("Example:")
print(checkio("one,two,three", "four,five,one,two,six,three"))

assert checkio("hello,world", "hello,earth") == "hello"
assert checkio("one,two,three", "four,five,six") == ""
assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

print("The mission is done! Click 'Check Solution' to earn rewards!")

