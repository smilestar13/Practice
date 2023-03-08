def is_even(num: int) -> bool:
    res = True
    if num % 2:
        res = False
    return res


print("Example:")
print(is_even(0))
