#Time2.py
#Short Program to show how to get the current time in Python. 
#Program Written By: Alexander Parsan
#Under the GPL v3.0

import time

#Time can also be used to get the current date or time
#For example:

#print out the time in 24 hour format 
print time.strftime("%H:%M:%S")

# print out the time in 12 hour format 
print time.strftime("%I:%M:%S")

#Get the date in python 
print (time.strftime("%d/%m/%Y"))

#this can come in handy for later programs!
