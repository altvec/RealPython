'''
Task desctiption:
=================

Write a script "election.py" that will simulate an election between two
candidates, A and B. One of the candidates wins the overall election by
a majority based on the outcomes of three regional elections.
(In other words, a candidate wins the overall election by winning
at least two regional elections.)
Candidate A has the following odds:
- 87% chance of winning region 1
- 65% chance of winning region 2
- 17% chance of winning region 3

Import and use the random() function from the random module to simulate
events based on probabilities; this function doesn't take any arguments
(meaning you don't pass it any input variables) and returns a random
value somewhere between 0 and 1.

Simulate 10,000 such elections, then (based on the average results)
display the probability that Candidate A will win and the probability
that Candidate B will win.

If you want to check your work without looking at the sample script,
the answer is in this (Candidate A has approximately a 63% chance of
  winning; Candidate B has roughly a 37% chance.)

Hint: To do this, you'll probably need to use a for loop with a lot of
if/else statements to check the results of each regional election.
'''

from __future__ import division
from random import random

total_A_wins = 0
total_B_wins = 0

trials = 10000

for trial in xrange(0, trials):
  A_win = 0
  B_win = 0

  if random() < .87:
    A_win += 1
  else:
    B_win += 1

  if random() < .65:
    A_win += 1
  else:
    B_win += 1

  if random() < .17:
    A_win += 1
  else:
    B_win += 1

  if A_win > B_win:
    total_A_wins += 1
  else:
    total_B_wins += 1

print "A wins in {}% of cases".format(total_A_wins / trials * 100)
print "B wins in {}% of cases".format(total_B_wins / trials * 100)
