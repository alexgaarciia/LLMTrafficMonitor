import time
import json
import requests
import urllib.parse

# Read the JSON lines from the file
with open('../data/test.jsonl', 'r') as file:
    questions = []
    for line in file:
        entry = json.loads(line)
        questions.append(entry['question'])


def querying_agent():
    counter = 1
    for question in questions[1:5]:
        query = str(question)
        # Create the URL with the encoded query
        url = f"http://127.0.0.1:3836/respond?query={urllib.parse.quote(query)}"

        # Print the size of the request
        request_size = len(url.encode('utf-8'))
        print(f"Request size (bytes): {request_size}")

        # Send the GET request and check if the response was successful
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error: {response.status_code}: {response.reason}")
            continue  # Skip this iteration and ask for another query

        # Mistral
        print("Model Name: Mistral")
        print(f"Question number: {counter} \n", response.content)
        content = response.content
        response_size = len(content.decode('utf-8'))
        print(f"Response size (bytes): {response_size}")
        time.sleep(5)

        # OpenAI
        # print("Model Name: OpenAI")
        # content = response.json()  # Parse the JSON response
        # print("Response:", content.get("response"))
        # response_size = len(response.text.encode('utf-8'))
        # print(f"Response size (bytes): {response_size}")

        counter += 1
        print()


# Run the querying agent
querying_agent()
