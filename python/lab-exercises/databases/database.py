
from turtle import update
import pyodbc

def executeQuery(sql_query):
    try:
        connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
        conn = pyodbc.connect(connectionString)
        cur = conn.cursor()
        cur.execute(sql_query)
        conn.commit()
        conn.close()
    except Exception as ex:
        print("executeQuery - ERROR - ", ex)
        return None

# Part 1 – Check whether the Students table already exists:
check_query = """ IF EXISTS(SELECT TABLE_NAME,TABLE_SCHEMA FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Student' AND TABLE_SCHEMA = 'dbo') BEGIN DROP TABLE Student END"""
executeQuery(check_query)

# Part 1 – Create the Students table:
create_query = "CREATE TABLE Student ( StudentID int NOT NULL, FirstName nvarchar(40) NOT NULL, Surname nvarchar(30) NULL, Course nvarchar(30) NULL, City nvarchar(15) NULL )"
executeQuery(create_query)

# Part 2 – Practice Executing Insert Commands
students_object = open("python/lab-exercises/databases/students.csv")
students_data = students_object.readlines()

for row in students_data:
    data_split = row.split(",")
    insert_query = "INSERT INTO [Student] ([StudentID], [FirstName], [Surname], [Course], [City]) VALUES ({}, '{}', '{}', '{}', '{}')".format(data_split[0], data_split[1], data_split[2], data_split[3], data_split[4])
    executeQuery(insert_query)

# Part 3 – Practice Executing an Update Command
    # Update the record of one of the students.
    # Check that it has worked by reading the data in the Management Studio.

update_query = "UPDATE [Student] SET [Course] = 'Pro Wrestling' WHERE [StudentID] = 1"
executeQuery(update_query)
