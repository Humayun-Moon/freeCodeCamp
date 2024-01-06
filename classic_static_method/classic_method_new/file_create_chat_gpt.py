import os
import io

current_dir = os.getcwd()
print(current_dir)

data_dir = os.path.join(current_dir, "data")

if not os.path.exists(data_dir):
    os.mkdir(data_dir)

file_path = os.path.join(data_dir, "my_file.txt")

with open(file_path, "w") as f:
    f.write("This is my file")