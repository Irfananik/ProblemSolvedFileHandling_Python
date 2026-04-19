#Read from a Specific File Pointer Position
#Write a function read_from_position(filename, position) that uses the file pointer to start reading a file from a given byte position and prints the remaining content.
def read_from_position(filename, position):
    with open(filename, 'r') as file:
        file.seek(position)
        content = file.read()
        print(content)
# Example usage
read_from_position('notes.txt', 10)