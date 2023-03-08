from typing import Union


def sun_angle(time: str) -> Union[float, str]:
    h_el, s_el = int(time[:2]), int(time[3:])
    step_h, step_s = 15, 0.25

    if h_el in range(6, 18) or time == '18:00':
        return ((h_el - 6) * step_h) + s_el * step_s
    else:
        return "I don't see the sun!"


print("Example:")
print(sun_angle("07:00"))

assert sun_angle("07:00") == 15
assert sun_angle("12:15") == 93.75

print("The mission is done! Click 'Check Solution' to earn rewards!")

