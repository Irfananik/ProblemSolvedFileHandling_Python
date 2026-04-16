# Create and Write to a File
def  create_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
filename = 'notes.txt'
content = "Hello, this is my first file."
create_file(filename, content)
print(f"File '{filename}' created with content: {content}")