import json
import requests
from typing import List
from googletrans import Translator
from requests.exceptions import RequestException


def request_get() -> dict:
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
    for character in data:
        try:
            name = translator.translate(character.get("name", ""), dest="pt").text
            affiliation = translator.translate(character.get("affiliation", "N"), dest="pt").text
            result.append([name, affiliation])
        except Exception as e:
            raise Exception(f"Translation error: {e}")
    return result


if __name__ == "__main__":
    print(request_get())
    print(translate_text())


