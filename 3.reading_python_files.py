import os
from tqdm import tqdm

MAX_CHAR_LEN = 600

# Collecting full paths of .py files
full_paths = []
for dirpath, dirnames, files in tqdm(os.walk("repos")):
    for file_name in files:
        full_path = os.path.join(dirpath, file_name)
        if full_path.endswith(".py"):
            full_paths.append(full_path)

print(len(full_paths))

# Writing the content of .py files to the output file
with open("python_code_text_data.txt", "a", encoding="utf-8") as output_file:
    for fpath in tqdm(full_paths, desc="Processing files"):
        try:
            with open(fpath, "r", encoding="utf-8") as input_file:
                data = input_file.read().replace('\n', '<N>')  # Replace newlines with spaces
                if 100<= len(data) <= MAX_CHAR_LEN:
                    output_file.write(data + "\n")  # Write as a single line
        except (UnicodeDecodeError, FileNotFoundError, PermissionError) as e:
            print(f"Error reading {fpath}: {e}")
            with open("error_log.txt", "a", encoding="utf-8") as log_file:
                log_file.write(f"Error reading {fpath}: {e}\n")
