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
