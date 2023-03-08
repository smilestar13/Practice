def checkio(text: str) -> str:
    work_lst = []

    for el in text:
        if el.isalpha():
            work_lst.append(el.lower())
    work_lst = sorted(work_lst)
    res = sorted(work_lst, key=lambda x: work_lst.count(x), reverse=True)
    return res[0]

# or
#
# import string
#
# def checkio(text):
#     """
#     We iterate through latyn alphabet and count each letter in the text.
#     Then 'max' selects the most frequent letter.
#     For the case when we have several equal letter,
#     'max' selects the first from they.
#     """
#     text = text.lower()
#     return max(string.ascii_lowercase, key=text.count)


print("Example:")
print(checkio('One'))

# These "asserts" are used for self-checking
assert checkio("Hello World!") == "l"
assert checkio("How do you do?") == "o"
assert checkio("One") == "e"
assert checkio("Oops!") == "o"
assert checkio("AAaooo!!!!") == "a"
assert checkio("abe") == "a"

print("The mission is done! Click 'Check Solution' to earn rewards!")

