import requests
from googletrans import Translator
from requests.exceptions import RequestException


def request_get():
    url = "https://last-airbender-api.fly.dev/api/v1/characters"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
         raise Exception(f"Failed to fetch data: {e}")


def translate_text():
    data=request_get()
    translator = Translator()
    result = []
    n=0

    name = [character.get("name", "") for character in data]
    affiliation = [character.get("affiliation", "") for character in data]

    try:
        name = translator.translate("\n".join(name), dest="pt").text.split("\n")
        affiliation = translator.translate("\n".join(affiliation), dest="pt").text.split("\n")
        while n<len(data):
            result.append([name[n],affiliation[n]])
            n+=1
    except Exception as e:
        raise Exception(f"Translation error: {e}")
    
    return result


if __name__ == "__main__":
    print(request_get())
    print(translate_text())


