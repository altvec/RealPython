def factor(num):
    for i in xrange(1, num + 1):
        if num % i == 0:
            print "{} is a divisor of {}".format(i, num)

num = int(raw_input("Enter an integer: "))
factor(num)

