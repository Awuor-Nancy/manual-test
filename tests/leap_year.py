# write a function that determines whether a year is a leap year
"""
    Check if a given year is a leap year.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.

    Raises:
        ValueError: If the year is negative or zero.
    """


def is_leap_year(year):
    if year <= 0:
        raise ValueError("year must not be non-negative!")
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


year = int(input("enter a year: "))
if is_leap_year(year):
    print(f"the year {year} is a leap year")
else:
    print(f"the year {year} is not a leap year")
