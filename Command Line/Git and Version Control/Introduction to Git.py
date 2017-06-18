## In this script, we will learn about git version control system.
## Git is a command-line tool we can access by typing git in the shell. The first step in using Git is to initialize a folder as a repository
## A repository (or "repo") tracks multiple versions of the files in the folder, enabling collaboration.


## Introduction To Version Control Systems

git init # initialize a repository


## The .Git Folder

ls -al # check the contents of the folder


## Creating Files In The Repository

echo -e "Random number generator" > README.md


## Checking File Status

git status

git add script.py


## Configuring Identity In Git

git config --global user.email "your.email@domain.com" # add email

git config --global user.name "Your name" # add username


## Committing Changes

git commit -m "Initial commit. Added script.py and README.md"


## Viewing File Differences

echo -e 'import random\nif __name__ == "__main__":\n    print(random.randint(0,10))' > script.py

git diff


## Making A Second Commit

git commit -m "Added random file access to script.py"


## Reviewing The Commit History

git log


## Viewing Commit Differences

git log --stat


## END















