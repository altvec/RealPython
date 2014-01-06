'''
Task description:
=================

Write a script "high_scores.py" that will read in a CSV file of users'
scores and display the highest score for each person. The file you will
read in is named "scores.csv" and is located in the chapter 7 practice
files folder. You should store the high scores as values in a dictionary
with the associated names as dictionary keys. This way, as you read in
each row of data, if the name already has a score associated with it in
the dictionary, you can compare these two scores and decide whether or
not to replace the "current" high score in the dictionary.

Use the sorted() function on the dictionary's keys in order to display
an ordered list of high scores, which should match this output:

    Empiro 23
    L33tH4x 42
    LLCoolDave 27
    MaxxT 25
    Misha46 25
    O_O 22
    johnsmith 30
    red 12
    tom123 26
'''

import os, csv

_Path = "/Users/srg/practice_files"

top_scores = {}
with open(os.path.join(_Path, "scores.csv"), "rb") as _File:
    _FileReader = csv.reader(_File)
    for k, v in _FileReader:
        v = int(v)
        if k in top_scores:
            if v > top_scores[k]:
                top_scores[k] = v
        else:
            top_scores[k] = v

_sorted = sorted(top_scores.keys())

for i in _sorted:
    print i, top_scores[i]
