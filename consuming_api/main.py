import requests
import json

def request_get():
    url = "https://last-airbender-api.fly.dev/api/v1/characters"
    response = requests.get(url)
    if response.status_code == 200:
        return json.dumps(response.json(),indent=4)
    else:
        return f"error {response.status_code}"
    

if __name__ == "__main__":
    print(request_get())