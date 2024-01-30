import requests

params = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params)
response.raise_for_status()
data = response.json()
question_data = data["results"]