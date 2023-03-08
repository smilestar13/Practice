def popular_words(text: str, words: list) -> dict:
    start_str = text.lower().split()
    f_dict = {}
    for el in words:
        if el in start_str:
            f_dict[el] = start_str.count(el)
        else:
            f_dict[el] = 0
    return f_dict


print("Example:")
print(
    popular_words(
        """
When I was One
I had just begun
When I was Two
I was nearly new
""",
        ["i", "was", "three", "near"],
    )
)

assert popular_words(
    "\nWhen I was One\nI had just begun\nWhen I was Two\nI was nearly new\n",
    ["i", "was", "three", "near"],
) == {"i": 4, "was": 3, "three": 0, "near": 0}

print("The mission is done! Click 'Check Solution' to earn rewards!")
