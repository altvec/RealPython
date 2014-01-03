'''
Task desctiption:
=================

Write a script "translate.py" that asks the user for some input with the
following prompt:
    Enter some text:

You should then use the replace() method to convert the text entered by
the user into "leetspeak" by making the following changes to lower-case
letters:
    The letter: a           becomes: 4
    The letter: b           becomes: 8
    The letter: e           becomes: 3
    The letter: l           becomes: 1
    The letter: o           becomes: 0
    The letter: s           becomes: 5
    The letter: t           becomes: 7

Your program should then display the resulting output.
A sample run of the program, with the user input in bold, is shown below:

>>> Enter some text: I like to eat eggs and spam.
I 1ik3 70 347 3gg5 4nd 5p4m.
>>>
'''

user_input = raw_input("Enter some text: ")
translated = user_input.replace("a", "4")
translated = translated.replace("b", "8")
translated = translated.replace("e", "3")
translated = translated.replace("l", "1")
translated = translated.replace("o", "0")
translated = translated.replace("s", "5")
translated = translated.replace("t", "7")
print translated
