# Python IO or Input Output for File Handling

try:
    file = open(".Order.txt", "a")#If file exists then it will find it however if it doesn't then it will create the file
    file.write("dwadwadwad")
except FileExistsError as errmsg:
    print("Error: file exists already", errmsg)

except FileNotFoundError as errmsg:
    print("Error: can't find the file", errmsg)

else:
    print("File found successfully")