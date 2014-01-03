'''
Task description:
=================

Write a script "exponent.py" that receives two numbers from the user and
displays the result of taking the first number to the power of the second
number.
A sample run of the program should look like this (with example input
that has been provided by the user highlighted in bold):

>>>
Enter a base: 1.2
Enter an exponent: 3
1.2 to the power of 3 = 1.728
>>>

Keep the following in mind:
- In Python, x^y is calculated by using the expression x ** y
- Before you can do anything with the user's input, you will have to store
the results of both calls to raw_input() in new objects
- The raw_input() function returns a string object, so you will need to
convert the user's input into numbers in order to do arithmetic on them
- You should use the string format() method to print the result
- You can assume that the user will enter actual numbers as input
'''

base = raw_input("Enter a base: ")
expo = raw_input("Enter an exponent: ")

print "{} to the power of {} =".format(base, expo), float(base) ** float(expo)

'''
I thinkg better to do calculations in separate statements.
For example:

base = raw_input("Enter a base: ")
expo = raw_input("Enter an exponent: ")
result = float(base) ** float(expo)
print "{} to the power of {} = {}".format(base, expo, result)
'''
