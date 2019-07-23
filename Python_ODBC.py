import pyodbc

class Northwind_Products():
    def __init__(self):
        self.server = "localhost,1433"
        self.database = "Northwind"
        self.username = "sa"
        self.password = "Passw0rd2018"
        self.docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.docker_Northwind.cursor()

my_db = Northwind_Products()

result = my_db.cursor.execute("SELECT * FROM Customers")
rows = result.fetchall()
for row in rows:
    print(row.CustomerID)
    print(row.ContactName + ' is a ' + row.ContactTitle + ' at ' + row.CompanyName)