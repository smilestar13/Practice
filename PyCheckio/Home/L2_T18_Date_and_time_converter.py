import calendar


def date_time(time: str) -> str:
    x = 'minute' if int(time[14:]) == 1 else 'minutes'
    y = 'hour' if int(time[11:13]) == 1 else 'hours'
    return f"{int(time[:2])} {calendar.month_name[int(time[3:5])]} {time[6:10]} year {int(time[11:13])} {y} {int(time[14:])} {x}"


print("Example:")
print(date_time("01.01.2000 00:00"))

assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
assert date_time("09.05.1945 06:07") == "9 May 1945 year 6 hours 7 minutes"

print("The mission is done! Click 'Check Solution' to earn rewards!")
