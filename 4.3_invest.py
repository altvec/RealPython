'''
Task description:
=================

Write a script "invest.py" that will track the growing amount of an
investment over time. This script includes an invest() function that
takes three inputs: the initial investment amount, the annual compounding
rate, and the total number of years to invest.
So, the first line of the function will look like this:

def invest(amount, rate, time):

The function then prints out the amount of the investment for every year
of the time period. In the main body of the script (after defining the
function), use the following code to test your function:

invest(100, .05, 8)
invest(2000, .025, 5)

Running this test code should produce the following output exactly:

principal amount: $100
annual rate of return: 0.05
year 1: $105.0
year 2: $110.25
year 3: $115.7625
year 4: $121.550625
year 5: $127.62815625
year 6: $134.009564063
year 7: $140.710042266
year 8: $147.745544379

principal amount: $2000
annual rate of return: 0.025
year 1: $2050.0
year 2: $2101.25
year 3: $2153.78125
year 4: $2207.62578125
year 5: $2262.81642578

Hint: Although functions usually return output values, this is entirely
optional in Python. Functions themselves can print output directly as well.
You can print as much as you like from inside a function, and the
function will continue running until you reach its end.
'''


def invest(amount, rate, time):
    '''
    The function prints out the amount of the investment for every year
    of the time period.
    '''
    print "principal amount: ${}".format(amount)
    print "annual rate of return: {}".format(rate)
    for year in range(1, time + 1):
        amount = amount * (1 + rate)
        print "year {}: ${}".format(year, amount)
    print


invest(100, .05, 8)
invest(2000, .025, 5)
