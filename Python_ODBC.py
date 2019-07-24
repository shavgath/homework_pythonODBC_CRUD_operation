import pyodbc
import sys
import time

class Northwind():
    def __init__(self):
        self.server = "localhost,1433"
        self.database = "Northwind"
        self.username = "sa"
        self.password = "Passw0rd2018"
        self.docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.docker_Northwind.cursor()

    def create(self):
        #Get Connection
        my_db = Northwind()
        table_name = input("Name your table: ")
        try:
            my_db.cursor.execute("CREATE TABLE" + " " + table_name + " "
                                "(SpartanID int NOT NULL PRIMARY KEY, "
                                "SpartanTitle varchar(255), "
                                "SpartanFirstName varchar(255), "
                                "SpartanLastName varchar(255)"
                                ")")
        except:
            print("Something has gone wrong. Please check the code!")

        finally:
            # SAVE Changes
            my_db.docker_Northwind.commit()
            #Close the connection
            my_db.docker_Northwind.close()
            print("\n*" + table_name + " has been successfully created!* \n")
            time.sleep(2)
            return

    def write(self):
        my_db = Northwind()

        spartan_id = input("Enter Spartan ID: ")
        spartan_title = input("Enter Spartan Title: ")
        spartan_first_name = input("Enter Spartan First Name: ")
        spartan_last_name = input("Enter Spartan Last Name: ")

        try:
            my_db.cursor.execute("INSERT INTO Spartan(SpartanID, SpartanTitle, SpartanFirstName, SpartanLastName) VALUES (?, ?, ?, ?);", (int(spartan_id), spartan_title.lower().strip(), spartan_first_name.lower().strip(), spartan_last_name.lower().strip()))

        except:
            print("Something has gone wrong. Please check the code!")

        finally:
            #MUST Commit as the changes wont be saved otherwise
            my_db.docker_Northwind.commit()
            # Close the connection
            my_db.docker_Northwind.close()
            print("\n *Changes have been successfully made to the database* \n")
            time.sleep(2)


#             #TODO: check if the values have been successfully entered into the database
#             #TODO: Uncomment to check if values was inserted to table

    def read(self):
        my_db = Northwind()

        try:
            my_db.cursor.execute("SELECT * FROM Spartan")
            while True:
                row = my_db.cursor.fetchone()
                if not row:
                    break
                print(row)
        except:
            print("Something has gone wrong. Please check the code!")

        finally:
            my_db.docker_Northwind.close()
            print("\n *Data was found in the Sparta Table* \n")
            time.sleep(2)


    def update(self):
        my_db = Northwind()
        spartan_id = input("Enter the Spartan ID that you would like to UPDATE: ")

        try:
            my_db.cursor.execute("SELECT * FROM Spartan WHERE SpartanID = ?", spartan_id)
            while True:
                row = my_db.cursor.fetchone()
                col = my_db.cursor.description()
                if not row:
                    break
                print(row)
                print("\n *Data was found in the Sparta Table* \n")

            spartan_title = input("Update Spartan Title: ")
            spartan_first_name = input("Update Spartan First Name: ")
            spartan_last_name = input("Update Spartan Last Name: ")

            my_db.cursor.execute("UPDATE Spartan SET SpartanTitle = ?, SpartanFirstName = ?, SpartanLastName = ?", spartan_title, spartan_first_name, spartan_last_name)

        finally:
            my_db.docker_Northwind.commit()
            my_db.docker_Northwind.close()
            print("\n*Data was successfully UPDATED in the Sparta Table*")
            time.sleep(2)


    def delete(self):
        my_db = Northwind()
        spartan_id = input("Enter the Spartan ID that you would like to DELETE: ")

        try:
            my_db.cursor.execute("SELECT * FROM Spartan WHERE SpartanID = ?", spartan_id)
            while True:
                row = my_db.cursor.fetchone()
                if not row:
                    print("There was no data in the Sparta Table \n")
                    #run.delete()
                print(row)
                print("\n *Data was found in the Sparta Table* \n")
                choice = input("Are you sure you want to delete?    Y = Yes,  N = No \n")

                if choice.upper().strip() == 'Y':
                    my_db.cursor.execute("DELETE FROM Spartan WHERE SpartanID = ?", spartan_id)

                if choice.upper().strip() == 'N':
                    exit()
        finally:
            my_db.docker_Northwind.commit()
            my_db.docker_Northwind.close()
            print("\n*Data was successfully DELETED in the Sparta Table*")
            time.sleep(2)
            exit()

#TODO: DELETE
# run = Northwind()
# run.delete()

#TODO: UPDATE
# run = Northwind()
# run.update()

#TODO: READ
# run = Northwind()
# run.read()

#TODO: WRITE
# run = Northwind()
# run.write()

#TODO: CREATE TABLE
# Run = Northwind()
# Run.Create()

