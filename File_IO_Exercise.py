class File():
    def Open(file):
        try:
            result = open(file, "r")  # If file exists then it will find it however if it doesn't then it will create the file
            for line in result.readlines():
                print(line)
            result.close()  # The result object is huge in size so have to close everytime we open it as the
        except ValueError as msg:
            print("Error: Only one operation able run.", msg)
        except FileExistsError as errmsg:
            print("Error: file exists already", errmsg)

        except FileNotFoundError as errmsg:
            print("Error: can't find the file", errmsg)

        else:
            print("File found successfully")

    def Write(file):
        try:
            result = open(file, "a")
            result.write("YAAASSS!")
            for line in result.readlines():
                print(line)
            result.close()
        except:
            pass
        else:
            print("Written on file successfully")
        print("File has been edited Successfully")


answer = input("What would you like to do?          1 = Read  2 = Write \n")
if answer == "1":
    File.Open(".Order.txt")
elif answer == "2":
    File.Write(".Order.txt")