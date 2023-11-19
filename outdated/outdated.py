#!/usr/bin/env python
"""
This module solves the "Outdated" problem in CS50P 2022.
Slug: cs50/problems/2022/python/outdated
"""
import datetime
import string
import sys
import typing


def parse_date(date_string: str) -> datetime.date:
    """
    :param date_string: date in the form of a string.
    :return: date object.
    """
    # If it starts with an ASCII letter, let's assume that it's the name of the month. It can't possibly be anything else.
    if date_string.startswith(tuple(string.ascii_letters)):
        return parse_text_format(date_string)

    # It didn't start with ASCII letters so the last acceptable thing is the other format.
    return parse_stupid_format(date_string)


def parse_stupid_format(date_string: str) -> datetime.date:
    """
    :param date_string: date to parse.
    :return: date object.
    """
    # Split with "/" as the delimiter, but make sure that there's no leading or trailing spaces.
    month, day, year = [int(s.strip()) for s in date_string.split("/")]

    return datetime.date(year=year, month=month, day=day)


def parse_text_format(date_string: str) -> datetime.date:
    """
    :param date_string: string to parse.
    :return: date object.
    """

    months_en = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    # Split into multiple fields and strip each one.
    # Unpack and hope for the best.
    month_day, year_string = [s.strip() for s in date_string.split(",")]
    month_string, day_string = [s.strip() for s in month_day.split(" ")]

    # Months are title cased in the list so we better ensure that the month string is title cased.
    # The index + 1 is the month's number.
    month = months_en.index(month_string.title()) + 1

    # Convert year and day to integers.
    year, day = int(year_string), int(day_string)

    return datetime.date(year=year, month=month, day=day)


def read_date_input(prompt: str = "Date: ") -> typing.Iterable[str]:
    """
    Yields user input until interrupted or input is closed.
    :param prompt: String to print as the prompt.
    :return: A generator that yields input, and stops when user interrupts or closes the input.
    """

    # The infinite loop will keep on going and yield one input at a time.
    # Loop is broken by EOFError and KeyboardInterrupt.
    # By using yield, we turn this function into a generator. So we're only going to ask for input when the caller
    # iterates over the generator. We don't preemptively ask for input.
    while True:
        try:
            yield input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            # Stop the generator! Yield no more!
            break


def main() -> int:
    """
    Continuously asks the user for a date. Tries to parse the string and then print it in ISO 8601 format.
    Returns when a valid date has been parsed and printed.
    :return: exit code.
    """
    # Define a date object that can be None.
    # This is to avoid running into the situation where date is undefined. We don't want `NameError`.
    date: datetime.date | None = None

    # Continuously read user input.
    for date_string in read_date_input():
        try:
            date = parse_date(date_string)
            # Stop obtaining input, we have a valid date.
            break
        except ValueError:
            # User is acting weird, let's ask again.
            continue

    # date will be None if the user interrupted or closed the input. Let's just return!
    if date is None:
        return 0

    # Print date in ISO 8601 format.
    print(date.isoformat(), end="")

    return 0


if __name__ == "__main__":
    sys.exit(main())
