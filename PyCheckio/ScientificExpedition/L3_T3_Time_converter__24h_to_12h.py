import datetime


def time_converter(time: str) -> str:
    dt = datetime.datetime.strptime(time, '%H:%M')
    return dt.strftime('%-I:%M %p').replace('AM', 'a.m.').replace('PM', 'p.m.')


print("Example:")
print(time_converter("09:00"))

assert time_converter("12:30") == "12:30 p.m."
assert time_converter("09:00") == "9:00 a.m."

print("The mission is done! Click 'Check Solution' to earn rewards!")

