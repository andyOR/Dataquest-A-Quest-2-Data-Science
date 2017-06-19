## In this script, we will learn about git, Github and interaction between them


## Introduction To Remote Repositories

git clone /dataquest/user/git/chatbot # This will clone the repository from /dataquest/user/git/chatbot, a path on our local computer,
#to our current folder, and place it in a subfolder named chatbot

git clone /dataquest/user/git/chatbot silentbot # This command will place the chatbot repository in a folder called silentbot


## Making Changes To Cloned Repositories


## Overview Of The Master Branch

# The master branch is usually the most up-to-date shared version of any code project

git branch # to see all of the branches that exist in the repo


## Pushing Changes To The Remote

git push origin master

git remote -v # provides the origin details


## Viewing Individual Commits

git log # this gives you status of every commit and unique identifier

git show "identifier# Commit number" # will show changes done in the commit


## Commits And The Working Directory

#  the Git commit workflow has three main components:

# >The working directory
# >The staging area
# >Commits

git diff 327e19f3f05 7aceb91665801b # just first few numbers will give diiference between both commits


## Switching To A Specific Commit

# If we type git reset --hard repo, Git switches back to the commit with the hash c12,
# and changes all of the files in the working directory so that they're exactly the same as the files in the commit

git reset --hard 327e19f3f053487bf90bbdf5f9bfda172998445e


## Pulling From A Remote Repo

git pull # updates local repo with remote repo


## Referring To The Most Recent Commit

# We can use the HEAD variable to switch to the most recent commit more easily
# using HEAD will revert the working directory to the state of the most recent commit
# We can also use shortcuts to get older commit hashes. HEAD~1 will get the second newest commit in the local repo,
# HEAD~2 will get the third newest commit, and so on

git reset --hard HEAD~1

git reset --hard HEAD~1 # commit hash of the most recent commit


## END 












