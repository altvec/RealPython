import sqlite3

connection = sqlite3.connect("newnum.db")
cursor = connection.cursor()

prompt = """
Select the operation that you want to perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""

# Loop waiting for user input
while True:
    inp = raw_input(prompt)

    # if user enters any choice from 1-4
    if inp in set(["1", "2", "3", "4"]):
        # parse the corresponding operation text
        operation = {
            1 : "avg",
            2 : "max",
            3 : "min",
            4 : "sum"
        }[int(inp)]

        # retrive data
        cursor.execute("SELECT {}(num) FROM numbers".format(operation))

        # fetchone() retrieves one record from the query
        get = cursor.fetchone()

        # output result to screen
        print operation + ": %f" % get[0]

    # if user enters 5
    elif inp == "5":
        print "Exit"

        # exit loop
        break
