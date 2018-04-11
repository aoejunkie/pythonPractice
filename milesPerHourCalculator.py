# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 20:49:08 2018

@author: Jeremy
"""

'''If you run a 10 kilometer race in 42 minutes and 42 seconds,
what is your average pace (time per mile in minutes and seconds)?
What is your average speed in miles per hour?'''

#function to turn kilometers into miles and save the value in milesTotal
def kmToM(kilometers):
    print('Kilometers converted to miles:')
    distanceTotal = kilometers / 1.61
    return distanceTotal

milesTotal = kmToM(kilometers = 10)
print('{:.2f}'.format(milesTotal))

#function to turn minutes into seconds and save the value in secondsTotal
def minutesToSeconds(minutes, seconds):
    print('Minutes converted to seconds: ')
    secondsTotal = minutes * 60 + seconds
    return secondsTotal

timeTotal = minutesToSeconds(minutes = 42, seconds = 42)
print(timeTotal)

#function to return the amount of seconds it takes to complete a mile
#based on the values in the previous functions
def milesInSeconds(miles, seconds):
    print('Seconds per mile: ')
    secondsInMilesTotal = seconds / miles
    return secondsInMilesTotal

final = milesInSeconds(milesTotal, timeTotal)
print(final)

#write a function to turn the seconds per mile into minutes