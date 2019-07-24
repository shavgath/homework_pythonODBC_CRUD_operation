from Python_ODBC import *


def main():
    choice = input("Would you like to create a table?  Y = Yes, N = No \n")
    if choice.upper().strip() == 'Y':
        table = Northwind()
        table.create()

    if choice.upper().strip() == 'N':
        print('Please select an option: C = Create/Insert, R = Read, U = Update, D = Delete ')
        choice = input('Choose your option = ')

        if choice.upper().strip() == 'C':
            createDb = Northwind()
            createDb.write()

        if choice.upper().strip() == 'R':
            readDb = Northwind()
            readDb.read()

        if choice.upper().strip() == 'U':
            updateDb = Northwind()
            updateDb.update()

        if choice.upper().strip() == 'D':
            deleteDb = Northwind()
            deleteDb.delete()



main()
