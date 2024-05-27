from datetime import datetime
import time
from github import Github
import os
from colorama import Fore, Style

ACCESS_TOKEN = open("token.txt", "r").read()
g = Github(ACCESS_TOKEN)
print(g.get_user())

end_time = 1712244965.6639817
start_time = end_time - 86400

for i in range(50):
    try:
        start_time_str = datetime.utcfromtimestamp(start_time).strftime("%Y-%m-%d")
        end_time_str = datetime.utcfromtimestamp(end_time).strftime("%Y-%m-%d")
        query = f"language:python created:{start_time_str}..{end_time_str}"
        print(query)
        end_time -= 86400
        start_time -= 86400
        result = g.search_repositories(query)
        print(Fore.GREEN + f"Total count: {result.totalCount}" + Style.RESET_ALL)
        for repository in result:
            print(Fore.BLUE + f"Repository clone URL: {repository.clone_url}" + Style.RESET_ALL)
            print(Fore.BLUE + f"Repository _clone_url: {repository._clone_url}" + Style.RESET_ALL)
            os.system(f"git clone {repository.clone_url} repos/{repository.owner.login}/{repository.name}")
            print(Fore.CYAN + Style.BRIGHT + f"Current start time: {start_time}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"Error: {str(e)}" + Style.RESET_ALL)
        print(Fore.RED + Style.BRIGHT + "Broke for some reason" + Style.RESET_ALL)
        time.sleep(120)
print(Fore.GREEN + "Finished, new end time should be:" + Style.RESET_ALL + f" {start_time}")
