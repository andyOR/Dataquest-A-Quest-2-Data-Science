## In this script, we will learn how to make changes in existing files


## Appending

echo "99 bottles of beer on the wall" > beer.txt                      
echo "Take one down, pass it around, 98 bottles of beer on the wall..." >> beer.txt # >> will add changes to the file


## Redirecting From A File

sort < beer.txt                                                       
99 bottles of beer on the wall                                                  
Take one down, pass it around, 98 bottles of beer on the wall...                
sort -r < beer.txt # reverse sorting with -r                                                   
Take one down, pass it around, 98 bottles of beer on the wall...                
99 bottles of beer on the wall


## The Grep Command. If we want to search through the contents of a set of files to find a specific line of text, We can use the grep command for this

echo "Coffee is almost as good as beer," > coffee.txt                 
echo "But I could never drink 99 bottles of it" >> coffee.txt         
grep "bottles of" beer.txt coffee.txt                                 


## Special Characters

#? is used to represent a single, unknown character. We could perform the same search we did above like this:


grep "beer" beer?.txt # if beer1.txt and beer2.txt exist in the system


## The Star Wildcard

# We can use the * character to match any number of characters, including 0
grep "beer" *.txt

#The above command will search for the string beer in any file that has a name ending in .txt


## Piping Output

tail -n 10 logs.txt | grep "Error"

#The above command will search the last 10 lines of logs.txt for the string Error


## Chaining Commands. If we want to run two commands sequentially, but not pass output between them, we can use && to chain them

echo "All the beers are gone" >> beer.txt && cat beer.txt # This will first add the string All the beers are gone to the file beer.txt,
# then print the entire contents of beer.txt


## Escaping Characters. If We use a backslash (\) as an escape character or -- if you add a backslash before a special character, the special character is treated like plain text


echo "\"Sare jahan se achha Hindustan hamara,\" said Rakesh Sharma to then Indian Prime Minister Indira Gandhi after looking at earth from moon."


## END
