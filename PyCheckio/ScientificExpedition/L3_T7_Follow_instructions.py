# def follow(instructions: str) -> tuple[int, int] | list[int]:
#     x = 0
#     y = 0
#     for el in instructions:
#         if el == 'f':
#             y += 1
#         elif el == 'b':
#             y -= 1
#         elif el == 'l':
#             x -= 1
#         elif el == 'r':
#             x += 1
#     return (x, y)
#
# # or
# #
def follow(instructions):
    c = instructions.count
    return c('r') - c('l'), c('f') - c('b')


print("Example:")
print(list(follow("fflff")))

# These "asserts" are used for self-checking
assert list(follow("fflff")) == [-1, 4]
assert list(follow("ffrff")) == [1, 4]
assert list(follow("fblr")) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")

