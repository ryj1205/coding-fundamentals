
import pyodbc

connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
conn = pyodbc.connect(connectionString)
cur = conn.cursor()

''' SELECT QUERY '''

''' INSERT QUERY '''
sql_query = "INSERT INTO [salesperson] ([emp_no], [first_name],[last_name],[dept_no],[salary],[sales_target],[county],[post_code],[tel],[notes]) VALUES (120, 'Ryan','Jackson',4,1000000,250000,'Derbyshire','S458HZ','01246 266605','These are notes')"
cur.execute(sql_query)
conn.commit()

''' UPDATE QUERY '''


conn.close()