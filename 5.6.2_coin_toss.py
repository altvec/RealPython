'''
Task description:
=================

Write a script "coin_toss.py" that uses coin toss simulations
to determine the answer to this slightly more complex probability puzzle:

I keep flipping a fair coin until I've seen it land on both heads and
tails at least once each - in other words, after I flip the coin the
first time, I continue to flip it until I get a different result.
On average, how many times will I have to flip the coin total?

Again, the actual probability could be worked out, but the point here is
to simulate the event using randint(). To get the expected average
number of tosses, you should set a variable trials = 10000 and
a variable flip = 0, then add 1 to your flips variable every time a
coin toss is made. Then you can print flips / trials at the end of the
code to see what the average number of flips was.

This one is tricky to structure correctly. Try writing out the logic
before you start coding. Some additional pointers if you're stuck:
- You will need to use a for loop over a range of trials.
- For each trial, first you should check the outcome of the first flip.
- Make sure you add the first flip to the total number of flips.
- After the first toss, you'll need another loop to keep flipping while
you get the same result as the first flip.
- If you just want to check whether or not your final answer is correct
without looking at the sample code -- result is 3.
'''

from __future__ import division
from random import randint

trials = 10000
flip = 0

for i in xrange(0, trials):
    flip += 1
    if randint(0, 1) == 1:
        while randint(0, 1) == 1:
            flip += 1
        flip += 1
    else:
        while randint(0, 1) == 0:
            flip += 1
        flip += 1

print flip / trials
