# write a function that determines whether a year is a leap year

def is_leap_year(year):
    if year % 4 == 0 | year % 100 != 0 | year % 400 == 0:
        return year

    else:
        return "not leap year"


leap_year = 2012
result = is_leap_year(leap_year)
print(f"The year {leap_year} is {result}")
