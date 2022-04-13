def leap_year(year):
    """
    - Add code in the defined function to figure out whether or not the given year is a leap year or not. 
    
    - Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400. For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are. - Wikipedia
    
    - Take in a parameter called year and return “Is a leap year” or “Not a leap year”
    """
    # Write your code here. 

year = int(input("Enter a year: "))

if year % 100 == 0 and year % 100 == 0:
    print("Is a leap year")
elif (year % 4 ==0) and (year % 100 != 0):
    print ("Is a leap year")
else:
    print ("Not a leap year")




