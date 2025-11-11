import psycopg2

ASTERISK_STRING = "**********************"

# Create the db connection
DB_CONN = psycopg2.connect("host=localhost dbname=postgres user=postgres password=assignment-password")

# Create a db cursor object for executing commands
DB_CURS = DB_CONN.cursor()

"""
Helper function used to facilitate the execution of commands on the psql server
"""
def executeQuery(db_query):
    DB_CURS.execute(db_query)

"""
Retrieves and displays all records from the students table.
"""
def getAllStudents():
    executeQuery("SELECT * FROM students;")

"""
Inserts a new student record into the students table.
"""
def addStudent(first_name, last_name, email, enrollment_date):
    # Format the query string
    db_query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('" + first_name + "', '" + last_name + "', '" + email + "', '" + enrollment_date + "');"
    
    # Execute the query
    executeQuery(db_query)

"""
Updates the email address for a student with the specified student_id.
"""
def updateStudentEmail(student_id, new_email):
    # Format the query string
    db_query = "UPDATE students SET email = '" + new_email + "' WHERE student_id = '" + student_id + "';"

    # Execute the query
    executeQuery(db_query)

"""
Deletes the record of the student with the specified student_id.
"""
def deleteStudent(student_id):
    # Format the query string
    db_query = "DELETE FROM students WHERE student_id = '" + student_id + "';"

"""
Helper function used to prompt a user for function argument values.
"""
def promptArguments(argumentList):
    print("You have chosen an option that calls a function requiring arguments.")
    print("Please enter the desired values for each argument\n")

    outputList = []
    for argument in argumentList:
        outputList += input(argument + ": ")
    
    print("All arguments have been collected. Continuing...")
    print(ASTERISK_STRING)

    return outputList

# Main Code
if __name__ == '__main__':
    user_has_quit = False
    while (not user_has_quit):
        print(ASTERISK_STRING)
        print("COMP 3005 Assignment 3")
        print("\nOptions:")
        
        print("\t1) getAllStudents()")
        print("\t2) addStudent(first_name, last_name, email, enrollment_date)")
        print("\t3) updateStudentEmail(student_id, new_email)")
        print("\t4) deleteStudent(student_id)")
        print("\tq) Quit")
        print(ASTERISK_STRING)

        user_input = input()

        if user_input is "1":
            getAllStudents()

            print(ASTERISK_STRING)
        elif user_input is "2":
            input_arguments = promptArguments(["first_name", "last_name", "email", "enrollment_date"])
            addStudent(input_arguments[0], input_arguments[1], input_arguments[2], input_arguments[3])

            print(ASTERISK_STRING)
        elif user_input is "3":
            input_arguments = promptArguments(["student_id", "new_email"])
            updateStudentEmail(input_arguments[0], input_arguments[1])

            print(ASTERISK_STRING)
        elif user_input is "4":
            input_arguments = promptArguments(["student_id"])
            deleteStudent(input_arguments[0])

            print(ASTERISK_STRING)
        elif user_input is "q":
            print("Quitting program...")
            user_has_quit = True

            print(ASTERISK_STRING)
        else:
            print(ASTERISK_STRING)

            print("Entered option is not known. Try again.")
            print(ASTERISK_STRING)

# Close the connection to the database
DB_CURS.close()
DB_CONN.close()