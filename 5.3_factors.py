'''
Task description:
=================

Write a script "factors.py" that includes a function to find all of the
integers that divide evenly into an integer provided by the user.
A sample run of the program should look like this:

>>>
Enter an integer: 12
1 is a divisor of 12
2 is a divisor of 12
3 is a divisor of 12
4 is a divisor of 12
6 is a divisor of 12
12 is a divisor of 12
>>>

You should use the % operator to check divisibility. This is called the
“modulus operator” and is represented by a percent symbol in Python.
It returns the remainder of any division. For instance, 3 goes into 16
a total of 5 times with a remainder of 1, therefore 16 % 3 returns 1.
Meanwhile, since 15 is divisible by 3, 15 % 3 returns 0.

Also keep in mind that raw_input() returns a string, so you will need to
convert this value to an integer before using it in any calculations.
'''


def factor(num):
    for i in xrange(1, num + 1):
        if num % i == 0:
            print "{} is a divisor of {}".format(i, num)


num = int(raw_input("Enter an integer: "))
factor(num)
