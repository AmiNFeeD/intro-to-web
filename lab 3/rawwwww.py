import json
import requests

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Title", data["title"])
        print("Body", data["body"])
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_data()