import re

def main():
    print(convert(input("Enter working hours: ")))

def convert(s):
    time_format_regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    match = re.search(r"^" + time_format_regex + " to " + time_format_regex + "$", s)
    if match:
        from_time = standardize_time(match.group(1), match.group(2), match.group(3))
        to_time = standardize_time(match.group(4), match.group(5), match.group(6))
        return f"{from_time} to {to_time}"
    else:
        raise ValueError("Invalid time format")

def standardize_time(hour, minute, period):
    if hour == "12":
        if period == "AM":
            hour = "00"
        else:
            hour = "12"
    else:
        if period == "AM":
            hour = f"{int(hour):02}"
        else:
            hour = f"{int(hour) + 12:02}"

    if minute is None:
        minute = "00"
    else:
        minute = f"{int(minute):02}"

    return f"{hour}:{minute}"

if __name__ == "__main__":
    main()
