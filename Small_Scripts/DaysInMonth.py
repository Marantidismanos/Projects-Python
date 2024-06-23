def is_leap(year):
    """ Taking a Year and trying to find out,if it's a leap year or not."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    return False

def days_in_month(year,month):
    """ Taking year and month and giving back  the days of the given month. """
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    
    if is_leap(year) and month==2:
        return 29
    else:
        month_days[month-1]

year=int(input("Enter a year : "))
month=int(input("Enter a month : "))
days=days_in_month(year,month)
print(days)
