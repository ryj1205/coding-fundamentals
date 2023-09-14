
import pyodbc

def executeQuery(sql_query):
    # This function can be used things such as for INSERT and UPDATE queries
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    cur.execute(sql_query)
    conn.commit()
    conn.close()

executeQuery("INSERT INTO [salesperson] ([emp_no], [first_name], [last_name], [dept_no], [salary], [sales_target], [county], [post_code], [tel], [notes]) VALUES (120, 'Ryan', 'Jackson', 4, 1000000, 250000, 'Derbyshire', 'S458HZ', '01246 266605', 'These are notes')")
