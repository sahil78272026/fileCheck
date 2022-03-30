def readFile(filename):
    try:
        with open(filename,'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"{filename} not found")

readFile("tables.txt") # will print
readFile("2.txt") # file name not found
readFile("3.txt") # file name not found
