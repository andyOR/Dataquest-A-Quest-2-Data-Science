## In this scripts, We'll delve into how to use the errors Python returns to debug our code


## Overview.

f = open("story.txt", 'r')
story_string = f.read()
vocabulary = open("dictionary.txt", "r").read()

def clean_text(text_string, special_characters):
        for string in special_characters:
            cleaned_string = text_string.replace(string, "")
            cleaned_string = cleaned_string.lower()
            return(cleaned_string)

def tokenize(text_string, special_characters):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)

misspelled_words = []
clean_chars = [",", ".", "'", ";", "\n"]
tokenized_story = tokenize(story_string, clean_chars)
tokenized_vocabulary = tokenize(vocabulary, clean_chars)

for ts in tokenized_story:
    if ts not in tokenized_vocabulary:
        misspelled_words.append(ts)
print(misspelled_words)


## Multiple Return Paths


## Optional Arguments
# Default code
def tokenize(text_string, special_characters, clean=False):
    if (clean==True): # only argument clean = True will clean the file
        cleaned_story = clean_text(text_string, special_characters)
        story_tokens = cleaned_story.split(" ")
        return(story_tokens)
    else:
        story_tokens = text_string.split(" ")
        return(story_tokens)

tokenized_story = []
tokenized_vocabulary = []
misspelled_words = []
tokenized_story = tokenize(story_string, clean_chars, True)
tokenized_vocabulary = tokenize(vocabulary, clean_chars)
for i in tokenized_story:
    if i not in tokenized_vocabulary:
        misspelled_words.append(i)


## Named Arguments. The Python interpreter allows us to pass in named arguments in any order

# All three of these statements assign the same values to the function arguments.
tokenized_story = tokenize(clean=False, text_string = story_string, special_characters = clean_chars)
tokenized_story = tokenize(text_string = story_string, clean=False, special_characters = clean_chars)
tokenized_story = tokenize(special_characters = clean_chars, text_string = story_string, clean=False)

clean_chars = [",", ".", "'", ";", "\n"]

# These three lines represent different ways of expressing the same function call.
#tokenized_story = tokenize(clean=False, text_string = story_string, special_characters = clean_chars)
tokenized_story = tokenize(text_string = story_string, clean=False, special_characters = clean_chars)
# tokenized_story = tokenize(special_characters = clean_chars, text_string = story_string, clean=False)

# These two lines represent different ways of expressing the same function call.
tokenized_vocabulary = tokenize(text_string=vocabulary, special_characters=clean_chars)
# tokenized_vocabulary = tokenize(special_characters=clean_chars, text_string=vocabulary)


## Practice: Creating A More Compact Spell Checker


## Types Of Errors. The two main types of errors are: Syntax errors and Runtime errors


## Syntax Errors.

# Missing ending quotes or starting quotes
# Using improper indentation
# Using improper keywords


## Runtime Errors.

# Calling a function before it's defined
# Calling a method or attribute that the object doesn't contain
# Attempting to convert a value to an incompatible data type


## TypeError And ValueError


## IndexError And AttributeError


## Traceback


## In this mission, we customized functions in new ways,
## practiced using these techniques to create a compact spell checker function, and learned how to identify and debug common errors


## END



