'''
4. Write a Python program to calculate number of days between two dates.
'''

from datetime import date
Fdate = date(2020, 7, 31)
Ldate = date(2020, 9, 2)
delta = Ldate - Fdate
print(delta.days, " days")
