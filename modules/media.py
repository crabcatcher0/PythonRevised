import os
import random

p = '' #enter the path 
os.chdir(p) #ls

# list all items from p
items = os.listdir(p)

# filter out dir from the list
files = [f for f in items if os.path.isfile(os.path.join(p, f))]

if files:
    #  random file from the list
    file_name = random.choice(files)
    file_path = os.path.join(p, file_name)
    print(f"Playing: {file_name}")
    
    os.system(f'start "" "{file_path}"')
else:
    print(f"No files found in directory: {p}")
