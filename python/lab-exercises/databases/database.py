
import pyodbc

def executeQuery(sql_query):

    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'

    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()

    cur.execute(sql_query)
    conn.commit()

    conn.close()

# Part 1 – Create Table
    # Use the slide code to create a table called Student for storing student data. Check that the table is created using the SQL Management Studio.

create_query = "CREATE TABLE Student ( StudentID int NOT NULL, FirstName nvarchar(40) NOT NULL, Surname nvarchar(30) NULL, Course nvarchar(30) NULL, City nvarchar(15) NULL )"
executeQuery(create_query)

# Part 2 – Practice Executing Insert Commands
    # Insert a few students' records into the Student table.
    # Be inventive! You can store the records in a CSV file. Read the data and then insert the data into the database.
    # You can use the names of the students in the class and details of their course and the city they live in.
    # Check the records are inserted using the Database Management Studio.



# Part 3 – Practice Executing an Update Command
    # Update the record of one of the students.
    # Check that it has worked by reading the data in the Management Studio.

