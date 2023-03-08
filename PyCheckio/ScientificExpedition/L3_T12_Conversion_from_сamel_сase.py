def from_camel_case(name: str) -> str:
    res_str = ''
    for el in name:
        if el.islower():
            res_str += el
        else:
            res_str += '_'
            res_str += el.lower()
    return res_str.strip('_')


print("Example:")
print(from_camel_case("MyFunctionName"))

# These "asserts" are used for self-checking
# assert from_camel_case("MyFunctionName") == "my_function_name"
# assert from_camel_case("IPhone") == "i_phone"

print("The mission is done! Click 'Check Solution' to earn rewards!")

