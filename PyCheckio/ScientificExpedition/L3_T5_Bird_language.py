def translate(text: str) -> str:
    res = ''
    vowels = 'aeiouy'
    text = list(text)
    for el in text:
        if el.lower() in vowels:
            del (text[text.index(el) + 1])
            del (text[text.index(el) + 1])
        elif el != ' ':
            del (text[text.index(el) + 1])
        res += el
    return res

# or
#
# VOWELS = "aeiouy"
#
#
# def translate(phrase):
#     output = ""
#     c = 0
#
#     while c < len(phrase):
#         output += phrase[c]
#         if phrase[c] in VOWELS:
#             c = c + 3
#         elif phrase[c] == ' ':
#             c = c + 1
#         else:
#             c = c + 2
#
#     return output


print("Example:")
print(translate("hoooowe yyyooouuu duoooiiine"))

# These "asserts" are used for self-checking
assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")

