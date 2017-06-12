## In this script, we will learn using jupyter for data science projects
## We will work with dataset of "birth.csv" containing information on births in US
## on specific date and day of the week

## Reading and splitting dataset into list
f = open("births.csv", 'r')
text = f.read()
text_split = []
text_split = text.split("\n")
text_string = []
for i in text_split:
    it = i.split(",")
    text_string.append(it)
print(text_string)



## Making a dictionary for number of births on days of the week
for i in text_string:
    it = i[3]
    #text_dic[it] = int(i[4])
    r = int(i[4])
    if it in text_dic:
        text_dic[it] = text_dic[it] + r
    else:
        text_dic[it] = r

text_dic
        
        
        
        
        


#Superstition around Birthday among Parents
##We have compile the number of births on each day of the week to check this notion around ppl

## END




