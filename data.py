import requests

question_data = []
response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&type=boolean")
response.raise_for_status()
data = response.json()
for i in range(len(data["results"])):
    question_data.append(data["results"][i])
