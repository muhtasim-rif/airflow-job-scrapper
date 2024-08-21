import git
import json
import os

REPO_PATH = 'https://github.com/muhtasim-rif/portfolio-save.git'
COMMIT_MESSAGE = 'Added new job listings'

def upload_to_git(data, file_name):
    file_path = os.path.join(REPO_PATH, file_name)

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

        repo = git.Repo(REPO_PATH)
        repo.index.add([file_path])
        repo.index.commit(COMMIT_MESSAGE)
        origin= repo.remote(name='origin')
        origin.push()

        print(f'Data upload to {file_path} and pushed to Git repository')
