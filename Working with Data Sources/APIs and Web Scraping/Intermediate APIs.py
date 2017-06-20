## In this script, we'll explore the GitHub API and use it to pull some interesting data on repositories and users. GitHub is a site for hosting code


## API Authentication

# Create a dictionary of headers containing our Authorization header.
headers = {"Authorization": "token 1f36137fbbe1602f779300dad26e4c1b7fbab631"}

# Make a GET request to the GitHub API with our headers.
# This API endpoint will give us details about Vik Paruchuri.
response = requests.get("https://api.github.com/users/VikParuchuri", headers=headers)

# Print the content of the response.  As you can see, this token corresponds to the account of Vik Paruchuri.
print(response.json())

response1 = requests.get('https://api.github.com/users/VikParuchuri/orgs', headers=headers)
orgs = response1.json()
print(orgs)


## Endpoints And Objects

# We've loaded headers in.
response = requests.get("https://api.github.com/users/torvalds", headers=headers)
torvalds = response.json()
print(torvalds)


## Other Objects

response = requests.get("https://api.github.com/repos/octocat/Hello-World", headers = headers)
hello_world = response.json()
print(hello_world)


## Pagination

params = {"per_page": 50, "page": 1}
response = requests.get("https://api.github.com/users/VikParuchuri/starred", headers=headers, params=params)
page1_repos = response.json()

params1 = {"per_page": 50, "page": 2}
response1 = requests.get("https://api.github.com/users/VikParuchuri/starred", headers=headers, params=params1)
page2_repos = response1.json()


## User-Level Endpoints

# Enter your code here.
response = requests.get("https://api.github.com/user", headers=headers)
user = response.json()


## POST Requests

# Create the data we'll pass into the API endpoint.  While this endpoint only requires the "name" key, there are other optional keys.
payload = {"name": "test"}

# We need to pass in our authentication headers!
response = requests.post("https://api.github.com/user/repos", json=payload, headers=headers)
print(response.status_code)

payload1 = {"name":"learning-about-apis"}
response1  = requests.post("https://api.github.com/user/repos", json=payload1, headers=headers)
status = response1.status_code


## PUT/PATCH Requests

payload = {"description": "The best repository ever!", "name": "test"}
response = requests.patch("https://api.github.com/repos/VikParuchuri/test", json=payload, headers=headers)
print(response.status_code)


payload1 = {"description": "Learning about requests!","name":"learning-about-apis"}
response1  = requests.patch("https://api.github.com/repos/VikParuchuri/learning-about-apis", json=payload1, headers=headers)
status = response1.status_code


## DELETE Requests

response = requests.delete("https://api.github.com/repos/VikParuchuri/test", headers=headers)
print(response.status_code)

response1 = requests.delete("https://api.github.com/repos/VikParuchuri/learning-about-apis", headers=headers)
status = response1.status_code


## END


