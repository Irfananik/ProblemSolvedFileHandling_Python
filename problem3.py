#Append Log Entries to a File
#Given a filename log.txt, use file append mode to add a new log entry each time the function add_log(message) is called. Each message should appear on a new line
from email.mime import message


def add_Log(message):
    with open('log.txt', 'a') as file:
        file.write(message + '\n')
add_Log("User logged in.")
add_Log("File uploaded.")
print("Log entries added to 'log.txt'.")