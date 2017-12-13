## In this mission, we'll dive into string manipulation, which is essential to working with data that's represented as text.

## Introduction to String manipulation

hello = "hello world"[0:5]
foo = "some string"
password = "password"

print(foo[5:11])
fifth = password[4]
last_four = password[4:]


## Omitting starting and ending indices

hello = "hello world"[:5]
foo = "some string"
print(foo[5:])

my_string = "string slicing is fun!"
# Your code goes here
first_nine = my_string[:9]
remainder = my_string[9:]


## Slicing indices with steps

hlo = "hello world"[:5:2]

my_string = "string slicing is fun!"
# Your code goes here
gibberish = my_string[::2]
worse_gibberish = my_string[7::3]


## Negative indexing

olleh = "hello world"[4::-1]
able_string = "able was I ere I saw elba"

# Your code goes here
def is_palindrome(my_string):
    return my_string == my_string[::-1]
        
phrase_palindrome = is_palindrome(able_string)


## Searching for substrings

theres_no = "I" in "team"

# Your code goes here
def easy_patterns(string):
    count = 0
    for r in passwords:
        if string in r:
            count+=1
    return count

countup_passwords = easy_patterns("1234")


## First class function

ints = list(map(int, [1.5, 2.4, 199.7, 56.0]))
print(ints)

# Your code goes here

floats = list(map(float, not_floats))


## Average Password lengths

# Your code goes here
password_lengths = list(map(len , passwords))

avg_password_length = sum(password_lengths) / len(passwords)


## More uses of first class functions

def is_palindrome(my_string):
    return my_string == my_string[::-1]

# Your code goes here
palindrome_passwords = list(filter(is_palindrome, passwords))


## Lambda Functions

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x : x % 2 == 0, numbers))
print(evens)

# Your code goes here
palindrome_passwords = list(filter(lambda x: x==x[::-1], passwords))


## Passwords strength

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x : x % 2 == 0, numbers))
print(evens)

# Your code goes here
weak_passwords = list(filter(lambda x: len(x)<6, passwords))
medium_passwords = list(filter(lambda x: len(x)>=6 and len(x)<=10 , passwords))
strong_passwords = list(filter(lambda x: len(x)>10, passwords))


## END
