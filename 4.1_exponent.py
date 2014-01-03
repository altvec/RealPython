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
