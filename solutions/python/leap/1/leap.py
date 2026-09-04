def leap_year(year):
    """
    This function determines whether a given year is a leap year.

    Parameter:
    year (int) - a given year

    Output:
    Bool - whetehr or not the year is a leap year
    """
    if year%100 ==0:
        return year%400 == 0
    return year%4 == 0 
