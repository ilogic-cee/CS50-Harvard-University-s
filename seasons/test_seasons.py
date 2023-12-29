from datetime import date
from seasons import convert_days_to_minutes

def test_recent_date():
    # Assuming today's date is 2023-01-01, testing with a date from 2020-01-01
    days_since_2020 = (date(2023, 1, 1) - date(2020, 1, 1)).days
    expected_output = "One million, five hundred eighty-four thousand, eight hundred eighty minutes"
    assert convert_days_to_minutes(days_since_2020) == expected_output
