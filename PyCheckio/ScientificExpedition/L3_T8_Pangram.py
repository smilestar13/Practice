def check_pangram(text: str) -> bool:
    checker_abc = "abcdefghijklmnopqrstuvwxyz"
    for el in checker_abc:
        if el in text.lower():
            res = True
        else:
            return False
    return res

# or
# from string import ascii_lowercase


# def check_pangram(text):
    # return set(ascii_lowercase).issubset(set(text.lower()))


print("Example:")
print(check_pangram("ABCDEF"))

# These "asserts" are used for self-checking
assert check_pangram("The quick brown fox jumps over the lazy dog.") == True
assert check_pangram("ABCDEF") == False
assert check_pangram("abcdefghijklmnopqrstuvwxyz") == True
assert check_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == True
assert check_pangram("abcdefghijklmnopqrstuvwxy") == False
assert (
    check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!")
    == True
)
assert check_pangram("As quirky joke, chefs won't pay devil magic zebra tax.") == True
assert check_pangram("Six big devils from Japan quickly forgot how to walt.") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

