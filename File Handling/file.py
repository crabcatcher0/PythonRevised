#context manager

file_path = "/home/ghost/PythonRevised/File Handling/first.txt"

with open(file_path, "r") as file:
    print(file.read())

#write in file

with open("second.txt", "w") as file:
    file.write("This is second file.")


# csv : Ms Excel
# pandas 