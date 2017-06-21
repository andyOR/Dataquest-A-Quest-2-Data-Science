## In this script, we will learn about web scraping
# One way to access the data without waiting for the provider to create an API is to use a technique called Web scraping


## Web Page Structure.

# Web pages use HyperText Markup Language (HTML). HTML isn't a programming language like Python. It's a markup language with its own syntax and rules.
# When a Web browser like Chrome or Firefox downloads a Web page, it reads the HTML to determine how to render it and display it to you

response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
content = response.content # content is the same as the HTML above


## Retrieving Elements From A Page

from bs4 import BeautifulSoup

# Initialize the parser, and pass in the content we grabbed earlier.
parser = BeautifulSoup(content, 'html.parser')

# Get the body tag from the document.
# Since we passed in the top level of the document to the parser, we need to pick a branch off of the root.
# With BeautifulSoup, we can access branches by using tag types as attributes.
body = parser.body

# Get the p tag from the body.
p = body.p

# Print the text inside the p tag.
# Text is a property that gets the inside text of a tag.
print(p.text)

head = parser.head
title = head.title
title_text = title.text


## Using Find All

parser = BeautifulSoup(content, 'html.parser')

# Get a list of all occurrences of the body tag in the element.
body = parser.find_all("body")

# Get the paragraph tag.
p = body[0].find_all("p")

# Get the text.
print(p[0].text)

head = parser.find_all("head")
title = head[0].find_all("title")
title_text = title[0].text


## Element IDs

# Get the page content and set up a new parser.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_ids.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Pass in the ID attribute to only get the element with that specific ID.
first_paragraph = parser.find_all("p", id="first")[0]
print(first_paragraph.text)
second_paragraph = parser.find_all("p", id="second")[0]
second_paragraph_text = second_paragraph.text


## Element Classes

# Get the website that contains classes.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Get the first inner paragraph.
# Find all the paragraph tags with the class inner-text.
# Then, take the first element in that list.
first_inner_paragraph = parser.find_all("p", class_="inner-text")[0]
print(first_inner_paragraph.text)

second_inner_paragraph = parser.find_all("p", class_="inner-text")[1]
second_inner_paragraph_text = second_inner_paragraph.text

first_outer_paragraph = parser.find_all("p", class_="outer-text")[0]
first_outer_paragraph_text = first_outer_paragraph.text


## Using CSS Selectors

# Get the website that contains classes and IDs.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Select all of the elements that have the first-item class.
first_items = parser.select(".first-item")

# Print the text of the first paragraph (the first element with the first-item class).
print(first_items[0].text)


first_outer_text = parser.select(".outer-text")[0].text

second_text = parser.select("#second")[0].text

