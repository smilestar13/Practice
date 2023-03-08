def correct_sentence(text: str) -> str:
    str_fin = text[0].upper() + text[1:]
    if text[-1] == '.':
        return str_fin
    else:
        str_fin = str_fin + '.'
        return str_fin


print("Example:")
print(correct_sentence("greetings, friends"))

# These "asserts" are used for self-checking
assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."

print("The mission is done! Click 'Check Solution' to earn rewards!")
