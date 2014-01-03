

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

