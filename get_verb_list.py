import requests
import json

SIZE = 10000


def save_list_to_json(lst, filename):
    with open(filename, 'w') as f:
        json.dump(lst, f)

def get_wiktionary_category(category, cmcontinue=None):
    params = {
        "action": "query",
        "format": "json",
        "list": "categorymembers",
        "cmtitle": f"Category:{category}",
        "cmlimit": "500",
        "cmtype": "page",
    }
    if cmcontinue is not None:
        params["cmcontinue"] = cmcontinue

    response = requests.get(
        "https://en.wiktionary.org/w/api.php",
        params=params
    )

    if response.status_code == 200:
        return response.json()
    else:
        return None

verbs = []
cmcontinue = None
while len(verbs) < SIZE:
    response = get_wiktionary_category("Spanish verbs", cmcontinue)
    if response is not None:
        verbs += [page["title"] for page in response["query"]["categorymembers"]]
        if "continue" in response:
            cmcontinue = response["continue"]["cmcontinue"]
        else:
            break
    else:
        break

def clean_list(verb_list):
    cleaned_list = [verb for verb in verb_list if ' ' not in verb and 'ä' not in verb and 'ë' not in verb and 'ï' not in verb and 'ü' not in verb and 'ö' not in verb]
    return cleaned_list

my_clean_list = clean_list(verbs)

print(my_clean_list)
print(len(my_clean_list))

cleaned_verbs = clean_list(verbs)
save_list_to_json(cleaned_verbs[:SIZE], 'cleaned_spanish_verbs.json')
