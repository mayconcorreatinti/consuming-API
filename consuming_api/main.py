import requests
import json
from googletrans import Translator


def request_get() -> str:
    url = "https://last-airbender-api.fly.dev/api/v1/characters"
    response = requests.get(url)

    if response.status_code == 200:
        return json.dumps(response.json(),indent=4)
    else:
        return f"error {response.status_code}"
    

def translate_text() -> list:
    name_affiliation_translated=[]

    translator = Translator()

    json_data=json.loads(request_get())

    for a in json_data:
        name_translated = translator.translate(a.get("name"),dest="pt")
        affiliation_translated = translator.translate(a.get("affiliation") if "affiliation" in a else 'N',dest="pt")
        name_affiliation_translated.append([name_translated.text,affiliation_translated.text])

    return name_affiliation_translated


if __name__ == "__main__":
    print(request_get())
    print(translate_text())