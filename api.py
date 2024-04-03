#curl http://localhost:11434/api/generate -d '{ "model": "tinyllama", "prompt": "Your prompt here" }'


import requests
import json

# The URL you want to send the POST request to
url = 'http://localhost:11434/api/generate'

# The data you want to send with the POST request
data = {
    "model": "gemma",
    "prompt": "why sky is blue",
    "stream": False,
}

# Convert the data to a JSON format
json_data = json.dumps(data)

# Send the POST request
response = requests.post(url, data=json_data)

# Print the response text (the content of the response)
print(response.text['response'])

