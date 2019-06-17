# Write a Python script to display the various Date Time formats.

# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week

import datetime
import time

# a
print('Current date and time is :' ,datetime.datetime.now())

# b
print('Current Year', datetime.date.today())
print('Current Year', datetime.date.today().strftime("%y"))
print('Current Year', datetime.date.today().strftime("%Y"))
print('Current Year', datetime.date.today().strftime("%D"))
print('Current Year', datetime.date.today().strftime("%d"))
print('Current Year', datetime.date.today().strftime("%m"))
print('Current Year', datetime.date.today().strftime("%B"))



# d) Week number of the year
print('Number of weeks passed this year till now', datetime.date.today().strftime('%W'))


# E weekday of the week
print('Weekday of the week: ', datetime.date.today().