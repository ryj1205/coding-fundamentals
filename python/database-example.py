
import pyodbc

connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
conn = pyodbc.connect(connectionString)
cur = conn.cursor()

sql_query = "SELECT COUNT(*) AS 'No of Orders', [company].[company_name] FROM [QAStore].[dbo].[sale] INNER JOIN [company] ON [sale].[company_no] = [company].[company_no] WHERE [company].[company_name] LIKE 'Happy Heaters%' GROUP BY [company].[company_name]"

result = cur.execute(sql_query).fetchall()

conn.close()

for row in result:
    print(row)
