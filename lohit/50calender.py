# Write a Python script to display the various Date Time formats.

# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week

import time
import datetime


print('_________________a  Current date and time____________')
print('Current date and time', datetime.datetime.now())

print('_________________Current year____________')
print('Current Year', datetime.date.today().strftime('%y'))
print('Current Year', datetime.date.today().strftime('%Y'))


print('_________________Month of year____________')

print('Current Year', datetime.date.today().strftime('%b'))
print('Current Year', datetime.date.today().strftime('%B'))

print('_________________Week number of the year___________')
print('Week number of the year', datetime.date.today().strftime('%w'))

print('Weekday of the week', datetime.date.today().strftime('%W'))


print('')