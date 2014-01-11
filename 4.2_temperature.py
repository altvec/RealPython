'''
Task description:
=================

Write a script "temperature.py" that includes two functions.
One function takes a Celsius temperature as its input, converts that
number into the equivalent Fahrenheit temperature and returns that value.
The second function takes a Fahrenheit temperature and returns the
equivalent Celsius temperature.
Test your functions by passing input values to them and printing the
output results.

For testing your functions, example output should look like:
  72 degrees F = 22.2222222222 degrees C
  37 degrees C = 98.6 degrees F
In case you didn't want to spend a minute searching the web or doing
algebra (the horror!), the relevant conversion formulas are:
F = C * 9/5 + 32
C = (F – 32) * 5/9
'''

from __future__ import division


def cels_to_fahr(cels):
    ''' Converts temp in celsius to fahrenheit '''
    result = cels * 9 / 5 + 32
    return result


def fahr_to_cels(fahr):
    ''' Converts temp in fahrenheit to celsius '''
    result = (fahr - 32) * 5 / 9
    return result


print "{} degrees F = {} degrees C".format(72, fahr_to_cels(72))
print "{} degress C = {} degrees F".format(37, cels_to_fahr(37))
