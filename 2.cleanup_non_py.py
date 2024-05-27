import os
from colorama import Fore, Style
import time

directory_to_walk = "repos"

for dirpath, dirnames, filenames in os.walk(directory_to_walk):
    for filename in filenames:
        full_path = os.path.join(dirpath, filename)
        
        # Skip.git directories
        if full_path.endswith(".git"):
            continue
        
        # Check if the file is a Python file
        if full_path.endswith(".py"):
            print(Fore.GREEN + f"Keeping {full_path}" + Style.RESET_ALL)
            pass
        else:
            print(Fore.RED + f"Deleting {full_path}" + Style.RESET_ALL)
            try:
                os.remove(full_path)
                print(Fore.YELLOW + "File deleted successfully." + Style.RESET_ALL)
            except Exception as e:
                print(Fore.YELLOW + f"Error deleting {full_path}: {e}" + Style.RESET_ALL)
                #time.sleep(1)  # Wait for a second before continuing
