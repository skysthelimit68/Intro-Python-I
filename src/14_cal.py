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

input_prompt = input("Please enter a month (1 to 12) and a year (4 digits, optional) seperating by a space: ")
today = datetime.now()

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
    if len(mo) <= 2 and isinstance(int(mo), int) and int(mo) in range(1, 13):
      return True
    else: 
      return False
  except:
    return False

input_prompt = input_prompt.split(' ')

if len(input_prompt) == 1 and isMonth(input_prompt[0]):
  print(calendar.TextCalendar(6).prmonth(today.year, int(input_prompt[0])))
elif len(input_prompt) == 2 and isYear(input_prompt[1]) and isMonth(input_prompt[0]):
  print(calendar.TextCalendar(6).prmonth(int(input_prompt[1]), int(input_prompt[0])))
elif input_prompt == ['']:
  print(calendar.TextCalendar(6).prmonth(today.year, today.month))
else:
  print("Invalid input. Exiting the program now")
