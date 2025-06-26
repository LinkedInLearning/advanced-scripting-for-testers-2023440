with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("This is the second line.\n")

with open("example.txt", "a") as file:
    file.write("This line is appended to the file.\n")
    file.write("This is the last line.\n")

with open("example.txt", "r") as file:
    content = file.readlines()
    print("File content:")
    for line in content:
        print(line.strip())

with open(
    "/Users/dwesterveld/personal/Advanced_Scripting_For_Testers/tests/example.txt", "w"
) as file:
    file.write("This is a test file in the tests directory.\n")
    file.write("This is the second line in the tests directory.\n")
