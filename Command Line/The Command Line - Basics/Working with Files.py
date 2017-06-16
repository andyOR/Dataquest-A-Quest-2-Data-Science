## In this script, we'll learn abot files and learn how to interact with them on the command line.


## Making A File

touch text.txt


## Understanding Standard Streams. The standard streams are how programs show us output in the terminal, and how we enter input
# stdout and stderr usually display on the monitor, while stdin is the input from the keyboard.
# In this case, echo is taking a string from stdin, and printing that string to stdout. By default,
# we see the message that it prints to stdout, because it shows on the monitor

echo "All bears should juggle"


## Redirecting Standard Streams

echo "All bears should juggle" > test.txt # this sentence will br printed in file test.txt


## Editing A File. Nano is a command line text editor that lets us edit and save files directly from the terminal

nano test.txt # ctrl + x to quit


## Overview Of File Permissions

ls -l # this will display permission for owner, group and everyone (r, w, x)


## Octal Notation For File Permissions

##--- : No permissions; corresponds to 0
##--x : Execute only permission; corresponds to 1
##-w- : Write only permissions; corresponds to 2
##-wx : Write and execute permissions; corresponds to 3
##r-- : Read only permissions; corresponds to 4
##r-x : Read and execute permissions; corresponds to 5
##rw- : Read and write permissions; corresponds to 6
##rwx : Read, write, and execute permissions; corresponds to 7

stat test.txt


## Modifying File Permissions

chmod 0764 test.txt # owner -rwx, group - rw-, everyone - ---


## Moving Files

mv test.txt test


## Copying Files

cp /home/dq/test/test.txt /home/dq/test/test2.txt


## Overview Of File Extensions

mv /home/dq/test/test.txt /home/dq/test/test_no_extension


## Deleting A File

rm /home/dq/test/test2.txt


## Bypassing Permissions As The Root User

sudo *command* # this will change to root user for changing the commands and files.
#No one other than root user will have permission to change anything. It will ask for password


## END















