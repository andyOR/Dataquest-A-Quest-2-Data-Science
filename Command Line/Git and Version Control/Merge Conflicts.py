


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
