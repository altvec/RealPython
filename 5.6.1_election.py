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

