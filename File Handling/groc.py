import csv

file_path = '/home/ghost/PythonRevised/File Handling/gro.csv'

def find_item():
    user_input = input("Enter the words to search (comma separated): ")
    search_words = user_input.split(', ')  # split input into individual words
    
    found_lines = []
    
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                line = ' '.join(row)  #convert row list to a single string
                line_words = line.split()  # split line into words
                
                #check if all search words are in the current line
                if all(word in line_words for word in search_words):
                    found_lines.append(line)
    
        if found_lines:
            with open("output.txt", "w") as output_file:
                output_file.write("\n".join(found_lines))
            return f"Lines containing all words '{user_input}' were written to output.txt."
        else:
            return f"No lines containing all words '{user_input}' were found."
    
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    except PermissionError:
        return f"Error: Permission denied to open file '{file_path}'."

print(find_item())
