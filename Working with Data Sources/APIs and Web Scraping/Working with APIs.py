## In this script, we will learn about Application program interface
## An API is a set of methods and tools that allows different applications to interact with each other.
## Programmers use APIs to query and retrieve data dynamically. A client can retrieve information quickly and effectively through an API


# In this script, we'll query a basic API to retrieve data about the International Space Station (ISS)


## Introduction To API Requests


## Types Of Requests

# Make a get request to get the latest position of the ISS from the OpenNotify API.
response = requests.get("http://api.open-notify.org/iss-now.json")
status_code = response.status_code # status code of the response


## Understanding Status Codes
#200 - Everything went okay, and the server returned a result (if any).
#301 - The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint's name has changed.
#401 - The server thinks you're not authenticated. This happens when you don't send the right credentials to access an API (we'll talk about this in a later mission).
#400 - The server thinks you made a bad request. This can happen when you don't send the information the API requires to process your request, among other things.
#403 - The resource you're trying to access is forbidden; you don't have the right permissions to see it.
#404 - The server didn't find the resource you tried to access.

# Enter your answer below.
request = requests.get("http://api.open-notify.org/iss-pass")
status_code = request.status_code

# status_code = 404, .json missing


## Hitting The Right Endpoint

# Enter your answer below.
request = requests.get("http://api.open-notify.org/iss-pass.json")
status_code = request.status_code

# status_code = 400


## Adding Query Parameters

# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Print the content of the response (the data the server returned)
#print(response.content)

# This gets the same data as the command above
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
#print(response.content)

#my co-odinates
parameters = {"lat":37.78, "lon":-122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
print(response.content)
content = response.content


## JSON Format. JSON is the primary format for sending and receiving data through APIs.

# Make a list of fast food chains.
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
print(type(best_food_chains))

# Import the JSON library.
import json

# Use json.dumps to convert best_food_chains to a string.
best_food_chains_string = json.dumps(best_food_chains)
print(type(best_food_chains_string))

# Convert best_food_chains_string back to a list.
print(type(json.loads(best_food_chains_string)))

# Make a dictionary
fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

# We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
print(type(fast_food_franchise_string))

fast_food_franchise_2 = json.loads(fast_food_franchise_string)
print(type(fast_food_franchise_2))


## Getting JSON From A Request

# Make the same request we did two screens ago.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a Python object.  Verify that it's a dictionary.
json_data = response.json()
print(type(json_data))
print(json_data)

first_pass_duration = json_data["response"][0]["duration"]


## Content Type

# Headers is a dictionary
print(response.headers)

content_type = response.headers["content-type"]


## Finding The Number Of People In Space

# Call the API here.
request=requests.get('http://api.open-notify.org/astros.json')
json_data = request.json()
in_space_count = json_data["number"]


## END









