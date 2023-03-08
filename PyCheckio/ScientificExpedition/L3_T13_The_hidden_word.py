def checkio(text, word):
    text = text.replace(' ', '').lower()
    if text.find(word) != -1:
        text = text.split('\n')
        for el in text:
            if el.find(word) != -1:
                start_inx = el.find(word) + 1
                finish_inx = start_inx + len(word) - 1
                row = text.index(el) + 1
                return [row, start_inx, row, finish_inx]
    else:
        text = text.split('\n')
        max_len = max(len(syb) for syb in text)  # Получаем максимальную длину строки
        result = [[] for i in range(max_len)]  # Создаем список с подсписками
        work_lst = []

        for c in text:  # Заполняем подсписки
            for i, char in enumerate(c):
                result[i].append(char)
        for el in result:  # Сливаем отдельные символы в строки
            fin_str = ''.join(el)
            work_lst.append(fin_str)

        for u in work_lst:
            if word in u:
                start_inx = work_lst.index(u) + 1
                start_row = u.find(word) + 1
                finish_row = start_row + len(word) - 1
                return [start_row, start_inx, finish_row, start_inx]


print(checkio(
            "Hi all!\nAnd all goodbye!\nOf course goodbye.\nor not","haoo",
        ))

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert (
        checkio(
            """DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""",
            "ten",
        )
        == [2, 14, 2, 16]
    )
    assert (
        checkio(
            """He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""",
            "noir",
        )
        == [4, 16, 7, 16]
    )
print("Coding complete? Click 'Check' to earn cool rewards!")
