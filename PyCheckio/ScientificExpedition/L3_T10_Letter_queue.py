from typing import List


def letter_queue(commands: List[str]) -> str:
    work_lst = []
    for el in commands:
        if 'PUSH' in el:
            work_lst.append(el[-1])
        elif el == 'POP' and work_lst:
            del (work_lst[0])
    return ''.join(work_lst)


if __name__ == '__main__':
    print("Example:")
    print(letter_queue(['PUSH A',
        'POP',
        'POP',
        'PUSH Z',
        'PUSH D',
        'PUSH O',
        'POP',
        'PUSH T']))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert letter_queue(['PUSH A',
    #     'POP',
    #     'POP',
    #     'PUSH Z',
    #     'PUSH D',
    #     'PUSH O',
    #     'POP',
    #     'PUSH T']) == 'DOT'
    # assert letter_queue(['POP', 'POP']) == ''
    # assert letter_queue(['PUSH H', 'PUSH I']) == 'HI'
    # assert letter_queue([]) == ''
    print("Coding complete? Click 'Check' to earn cool rewards!")

