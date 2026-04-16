def read_lines(filename):
    with open(filename, 'r') as file:
        for index, line in enumerate(file, start=1):
            print(f"{index}: {line.strip()}")

# Just call it directly
read_lines('data.txt')