def checkio(words: str) -> bool:
    res = False
    bool_counter = 0
    for el in words.split():
        if el.isalpha():
            bool_counter += 1
            if bool_counter == 3:
                break
        else:
            bool_counter = 0
    if bool_counter == 3:
        res = True
    return res


print("Example:")
print(checkio("Hello World hello"))

# These "asserts" are used for self-checking
assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

