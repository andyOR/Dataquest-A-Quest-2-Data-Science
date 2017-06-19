## In this script, we will learn about git branch
# Git enables smooth collaboration between many programmers who are all making changes to a repo at the same time
# We can create a branch with the git branch command to do this


## Introduction To Git Branches

git clone /dataquest/user/git/chatbot # clone the remote repo

cd chatbot

git branch more-speech # will make new branch

git checkout more-speech # will navigate to new branch


## Switching Branches


## Pushing A Branch To A Remote

git branch -r #to show all of the branches on the remote and head branch

git branch -a # will show all of the branches available locally

git remote origin more-speech


## Merging Branches

# Merging allows us to copy commits from one branch into another. This enables us to efficiently develop features
# for projects on their own branches without conflicts, then merge them into master so that end users will have access to them
# In order to merge branch b into branch a, we first have to switch to branch a, then run git merge

git checkout master
git merge more-speech
git push origin master


## Deleting Branches

# To delete a branch once we've merged all of its commits into another branch, we use the git branch -d command

git branch -d more-speech


## Checking Out Branches From The Remote

~$ cd /home/dq
~$ git clone /dataquest/user/git/chatbot chatbot2
~$ cd chatbot2
~$ git checkout -b happy-bot
~$ printf "\nprint('Happiness level: 120')" >> bot.py
~$ git add .
~$ git commit -m "Made the bot 20% happier!"
~$ git push origin happy-bot
~$ cd ..
~$ cd chatbot
~$ git fetch
~$ git checkout happy-bot
~$ python bot.py


## Finding Differences Across Branches

##The typical Git workflow looks like this:
##
##Create a branch off of master with the name of your feature. Let's say feature/better-algo.
##Make your changes on the branch and create commits.
##Push the branch to the remote repo.
##Ask others to review and evaluate your branch.
##Merge the branch into master once everyone thinks it looks okay.
##Delete the branch.

git diff master happy-bot


## Branch Naming Conventions


## 
