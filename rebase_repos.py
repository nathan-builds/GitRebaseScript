import git
import os
from dotenv import load_dotenv
from git import GitError
from colorama import init, Fore

# Load environment file that contains the repo root directory path
load_dotenv()
init()
repo_root_directory = os.getenv('REPOS')
repo_iterator = os.listdir(repo_root_directory)


# get all the sub-directories under the root repo, ignores .idea files
def getRepoDirectories():
    for repo_name in repo_iterator:
        if repo_name != '.idea':
            repo_path = repo_root_directory + "\\" + repo_name
            createGitRepo(repo_path, repo_name)

# create a Repo object and perform pull-rebase, catches common errors
# such as un-staged changes and displays failure
def createGitRepo(repo_path, repo_name):
    try:
        current_repo = git.Repo(repo_path)
        current_repo.remote().pull('--rebase')
        current_operation = f"Pull rebase completed on: {repo_name}"
        print(Fore.GREEN + current_operation)
    except GitError as error:
        repo_name = repo_name.upper()
        repo_name_with_color = Fore.YELLOW + repo_name
        error_message = f"PULL REBASE FAILED FOR {repo_name_with_color}" + " "
        with_issue = Fore.RED + "WITH THE FOLLOWING ISSUE:"
        print(Fore.RED + f" {error_message}" + f"{with_issue}")
        print(error.args)


def rebaseRepos():
    getRepoDirectories()


rebaseRepos()
