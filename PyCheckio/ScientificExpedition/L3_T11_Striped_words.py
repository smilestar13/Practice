def checkio(line: str) -> int:
    vowels_abc = 'aeiouy'

    work_str = ''
    for el in line:
        if el.isalpha() or el.isdigit():
            work_str += el.lower()
        else:
            work_str += ' '
    work_lst = work_str.split()

    fin_lst = []
    for el in work_lst:
        fin_true = []
        for c in el:
            if c.isdigit():
                fin_true.append(False)
                break
            else:
                fin_true.append(True)
        if all(fin_true) and len(el) > 1:
            fin_lst.append(el)

    counter_zebras = 0
    for el in fin_lst:
        if el[0] in vowels_abc:
            even = el[::2]
            odd = el[1::2]
        else:
            even = el[1::2]
            odd = el[::2]
        vowels_true = []

        for c in even:
            if c in vowels_abc:
                vowels_true.append(True)
            else:
                vowels_true.append(False)
                break
        for c in odd:
            if c not in vowels_abc:
                vowels_true.append(True)
            else:
                vowels_true.append(False)
                break
        if all(vowels_true):
            counter_zebras += 1
    return counter_zebras


if __name__ == "__main__":
    print("Example:")
    print(checkio("A quantity of striped words."))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio("My name is ...") == 3
    assert checkio("Hello world") == 0
    assert checkio("A quantity of striped words.") == 1
    assert checkio("Dog,cat,mouse,bird.Human.") == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")

