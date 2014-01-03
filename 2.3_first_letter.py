'''
Task description:
=================

Write a script named "first_letter.py" that first prompts the user for
input by using the string:
    Tell me your password:
The script should then determine the first letter of the user's input,
convert that letter to upper-case, and display it back.
As an example, if the user input was "no" then the program should
respond like this:
    The first letter you entered was: N
For now, it's okay if your program crashes when the user enters nothing
as input (just hitting ENTER instead).
'''

user_prompt = raw_input("Tell me your password: ")
print "The first letter you entered was:", user_prompt[0].upper()
