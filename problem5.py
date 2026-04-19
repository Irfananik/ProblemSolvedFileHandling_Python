#Safe File Read with Full Exception Handling
# Write a function safe_read(filename) that tries to open and read a file. Use try, except, else, and finally blocks:
# Print file content if successful (else block)
# Handle the case where file does not exist (except block)
# Always print "Operation complete." at the end (finally block)

def safe_read(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    else:
        print(content)
    finally:
        print("Operation complete.")
# Example usage
safe_read('notes1.txt')
