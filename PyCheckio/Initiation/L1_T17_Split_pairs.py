def split_pairs(text: str):
    res = []
    if len(text) > 0:
        while len(text) > 0:
            res.append(text[0:2])
            text = text[2:]
        if len(res[-1]) == 1:
            res[-1] += '_'
    return res


print("Example:")
print(list(split_pairs("abcd")))

assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]
assert list(split_pairs("")) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")