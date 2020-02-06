'''We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into account to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.Source'''
#int(input('enter the yyear'))
#def year_fun(year):
 #   return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
print("********************************************************************")
def testyear(year):
    if year%4==0:
        return True
    elif year%100==0:
        return True
    elif year%400==0:
        return True

year=int(input("enter the year = "))
print(testyear(year))

print("**********************************************************")

def is_leap(year):
    leap = False
    
    # Write your logic here
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    return leap

year = int(input())
print(is_leap(year))


