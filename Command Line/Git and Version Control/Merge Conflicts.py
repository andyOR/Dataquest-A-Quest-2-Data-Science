## In this script, we will learn conflict of git merges 


## Merge Conflicts

cd ~
git clone /dataquest/user/git/chatbot
cd chatbot
git checkout -b feature/king-bot
printf "\nprint('King Kong')" >> bot.py
git add .
git commit -m "Make more kinglike"
git checkout master
git checkout -b feature/queen-bot
printf "\nprint('I am the queen)" >> bot.py
git add .
git commit -m "Make more queenlike"
git checkout master
git merge feature/king-bot
git merge feature/queen-bot


## Aborting A Merge. One way to resolve a conflict is to abort the merge altogether. We can do this with git merge --abort

git merge --abort master feature/quuen-bot


## Resolving Conflicts

cd /home/dq/chatbot
git merge feature/queen-bot
echo "print('I am the queen')" > bot.py
git add .
git commit -m "Fixed conflicts"
git push origin master
