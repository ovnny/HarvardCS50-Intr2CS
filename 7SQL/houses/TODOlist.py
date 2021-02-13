TODO LIST - PSET7(HOUSES)

To create and use database of to maintain information of all 
the students in the Harry Potter universe and their subsequent houses.

IMPORT.PY
    'run python import.py characters.csv'
    from cs50 import SQL
    db = SQL("sqlite:///students.db") --> give acess to database and allow us to do
    the following:

        db.execute("QUERY") --> include a SQL query that manipulate the "students" 
        table.


    1) open CSV file containing "name", "house" and "birth"
    2) import the csv file data into a SQlite database table called "students"
    3) parse the students names to put then on the right columns of the table 
        "students"
        3 names == first, middle and last / 2 names == first, (//N or null) and 
            last
    
        . Check command-line arguments
        . Open CSV file given by command-line argument
        . For each row, parse name
        . Insert each student into the "students" table of 'students.db'
        . from sys import argv
        . split() to parse the names
________________________________________________________________________________________________


ROSTER.PY
    'run python roster.py Gryffindor'
    output == list of all students in that house based on the database data.
        
        (i.e) Hermione Jean Granger, born 1979
        'the roster must be sorted by last name and later by first name'

        . Check command-line arguments
        . Query database for all students in house
        . Print out each student''s full name and birth year
        . Students should be sorted alphabetically by last name, then first name.
