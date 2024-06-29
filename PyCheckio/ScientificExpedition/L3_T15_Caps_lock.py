def caps_lock(text: str) -> str:
    real_txt = ''
    checker = 0
    for el in text:
        if checker % 2 == 0 and el != 'a':
            real_txt += el
        elif checker % 2 == 1 and el != 'a':
            real_txt += el.upper()
        if el == 'a':
            checker += 1
    return real_txt


if __name__ == "__main__":
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
    print("Coding complete? Click 'Check' to earn cool rewards!")

