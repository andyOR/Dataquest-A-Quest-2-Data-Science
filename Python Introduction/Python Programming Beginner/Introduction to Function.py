## In this scripts, We will learn the concept of functions.
# We will use "dictionary.txt" having correctly spell words and create function for spell checking other files


## Overview. Reading dictionary file of correctly spell words

p = open("dictionary.txt", "r")
vocabulary = p.read()
print(vocabulary)


## Tokenizing The Vocabulary

# The goal of tokenization is to convert a large body of text into smaller tokens, or components, that we can work with.
# In this case, each token is a word in the vocabulary

vocabulary = open("dictionary.txt", "r").read()
tokenized_vocabulary = vocabulary.split(" ") # splitting the file and forming a list of words
print(tokenized_vocabulary[0:5])


## Replacing Special Characters. "replace()" method

f = open("story.txt", 'r')
story_string = f.read()
print(story_string)

#print(story_string)
story_string = story_string.replace(".","")
story_string = story_string.replace(",","")
story_string = story_string.replace("'", "")
story_string = story_string.replace(";", "")
story_string = story_string.replace("\n", "")
print(story_string)


## Functions.

# Functions play a few key roles when writing code:
# information hiding
# modularity
#  abstraction


## Practice: Creating A Function That Cleans Text

f = open("story.txt", 'r')
story_string = f.read()

def clean_text(text_string): # function to clean the file with punc, commas, etc
    cleaned_string = text_string.replace(".","")
    cleaned_string = cleaned_string.replace(",","")
    cleaned_string = cleaned_string.replace("'","")
    cleaned_string = cleaned_string.replace(";","")
    cleaned_string = cleaned_string.replace("\n","")
    return(cleaned_string)


## Changing Word Case.  we will use string method "lower()"

def clean_text(text_string):
    cleaned_string = text_string.replace(",","")
    cleaned_string = cleaned_string.replace(".","")
    cleaned_string = cleaned_string.replace("'", "")
    cleaned_string = cleaned_string.replace(";", "")
    cleaned_string = cleaned_string.replace("\n", "")
    cleaned_string = cleaned_string.lower() # words in file are lowered
    return(cleaned_string)
cleaned_story = clean_text(story_string)


## Multiple Arguments

def strip_text(text_string, strip_string, replacement_string):
    cleaned_string = text_string.replace(strip_string, replacement_string)
    return(cleaned_string)
howdy_1 = strip_text("Howdy!", "!", "")
howdy_2 = strip_text("Howdy...", ".", "")


f = open("story.txt", 'r')
story_string = f.read()
clean_chars = [",", ".", "'", ";", "\n"]

# Previous code for clean_text().
def clean_text(text_string, special_characters):
    cleaned_string =  text_string
    for i in special_characters:
        cleaned_string = cleaned_string.replace(i, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)
    
#cleaned_story = ""
cleaned_story = clean_text(story_string, clean_chars) #using clean_chars for all spl characters
print(cleaned_story)


## Tokenizing The Story
def clean_text(text_string, special_characters):
     cleaned_string = text_string
     for string in special_characters:
         cleaned_string = cleaned_string.replace(string, "")
     cleaned_string = cleaned_string.lower()
     return(cleaned_string)

def tokensize(text_string, special_characters):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ") # forming a list of all words
    return(story_tokens)
clean_chars = [",", ".", "'", ";", "\n"]
tokenized_story = tokensize(story_string, clean_chars)
print(tokenized_story)

#practice -  finding the number of occurrences of a word in the file
clean_dict = {}

for cr in tokenized_story:
    if cr in clean_dict:
        clean_dict[cr] = clean_dict[cr] + 1
    else:
        clean_dict[cr] = 1
        
print(clean_dict)


## Finding Misspelled Words

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
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

for i in tokenized_story:
    if i not in tokenized_vocabulary: # will find misspelled words
        misspelled_words.append(i)
print(misspelled_words)


## END
