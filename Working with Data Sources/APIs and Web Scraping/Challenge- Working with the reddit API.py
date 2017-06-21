## In this script, we'll pull APIs concepts learnt till now to explore trending posts and comments on reddit.

#In this challenge, you'll practice:

# Retrieving a list of trending posts on a particular subreddit
# Exploring the comments on a single article
# Posting our own comment on an article


## Authenticating With The API

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t":"day"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params=params)
python_top = response.json()


##

python_top_articles = python_top["data"]["children"]
highest = 0 
most_upvoted = ""
for i in python_top_articles:
    ir = i["data"] # data key
    if ir["ups"] >= highest:
        highest = ir["ups"] # data key includes upvotes
        most_upvoted = ir["id"]


## Getting Post Comments

params = {"t":"day"}
response = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u", headers=headers)
comments= response.json()


##  Getting The Most Upvoted Comment

comments_list = comments[1]["data"]["children"]

highest = 0
most_upvoted_comment = ""

for i in comments_list:
    ir = i["data"]
    if ir["ups"] >= highest:
        highest = ir["ups"]
        most_upvoted_commen



## Upvoting A Comment

payload = {"dir":1, "id":"d16y4ry"}
response = requests.post("https://oauth.reddit.com/api/vote", json=payload, headers=headers)
status = response.status_code


## END







        t = ir["id"]
        
