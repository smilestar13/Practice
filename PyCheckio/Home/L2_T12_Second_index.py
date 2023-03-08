def second_index(text: str, symbol: str) -> [int, None]:
    if text.count(symbol) > 1:
        str_fin = text.find(symbol)
        str_fin = text.find(symbol, str_fin + 1)
        return str_fin
    else:
        str_fin = None
        return str_fin


print("Example:")
print(second_index("sims", "s"))

assert second_index("sims", "s") == 3
assert second_index("find the river", "e") == 12
assert second_index("hi", " ") == None
assert second_index("hi mayor", " ") == None
assert second_index("hi mr Mayor", " ") == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")

