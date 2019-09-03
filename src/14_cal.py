"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

today = datetime.now()
mons = [1,2,3,4,5,6,7,8,9,10,11,12]

def isYear(yr):
  try:
    if len(yr) == 4 and isinstance(int(yr), int): 
      return True
    else:
      return False
  except:
    return False 

def isMonth(mo):
  try:
    if len(mo) <= 2 and isinstance(int(mo), int) and int(mo) in mons:
      return True
    else: 
      return False
  except:
    return False


if len(sys.argv) == 2 and isMonth(sys.argv[1]):
  print(calendar.TextCalendar(6).prmonth(today.year, int(sys.argv[1])))
elif len(sys.argv) == 3 and isYear(sys.argv[2]) and isMonth(sys.argv[1]):
  print(calendar.TextCalendar(6).prmonth(int(sys.argv[2]), int(sys.argv[1])))
else:
  print("put month and year into the command line")

