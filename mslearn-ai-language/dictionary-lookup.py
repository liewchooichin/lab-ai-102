# Dictionary lookup
import os
import requests, uuid
import json

# Add your key and endpoint
key = os.getenv("TRANSLATOR_KEY")
endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = "eastus"

# dictionary lookup
path = '/dictionary/lookup'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['zh-Hans'],
}

# location required if you're using a multi-service or regional (not global) resource.
headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4()),
}


# Function to post and get the request and response. 
# Then, print the json response.
def do_rest_api(constructed_url, params, headers, body):
    request = requests.post(url=constructed_url, params=params, headers=headers, json=body)
    # response is in json dictinary
    response = request.json()
    # the response is turned into a string for printing
    response_str = json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
    print(response_str)
    return response # return dictionary obj


# You can pass more than one object in body.
body = [{
    'text': 'aeroplane',
}]

# Call the rest api
response_dict = do_rest_api(constructed_url=constructed_url, params=params, headers=headers, body=body)

# get total number of translation
len_translation = len(response_dict[0]["translations"])
print(f'Number of translation: {len_translation}');
print("Translated to: ")
for i in range(len_translation):
    print(response_dict[0]["translations"][i]["normalizedTarget"])


# dictionary examples
# Text: A string specifying the term to look up. This property should be the value of a normalizedText 
# field from the back-translations of a previous Dictionary lookup request. It can also be the value of 
# the normalizedSource field.
# Translation: A string specifying the translated text previously returned by the Dictionary lookup 
# operation. This property should be the value from the normalizedTarget field in the translations 
# list of the Dictionary lookup response. The service returns examples for the specific source-target 
# word-pair.

# Normalized text for dictionary examples
path = "/dictionary/examples"
constructed_url = endpoint + path

# Get the information from the response from the dictionary lookup
text = response_dict[0]["normalizedSource"]
# Get only the first response["translations"][0] for brevity.
# For complete set of possible translation, we can iterate through the list
# of translation.
translation = response_dict[0]["translations"][0]["normalizedTarget"]

body = [
    {"Text":text, "Translation":translation}
]
# dictionary example
response_dict = do_rest_api(constructed_url=constructed_url, params=params, headers=headers, body=body)

# print the example sentence pairs
len_translation = len(response_dict[0]["examples"])
for i in range(len_translation):
    source_sentence = response_dict[0]["examples"][i]["sourcePrefix"] \
                + response_dict[0]["examples"][i]["sourceTerm"] \
                + response_dict[0]["examples"][i]["sourceSuffix"]
    target_sentence = response_dict[0]["examples"][i]["targetPrefix"] \
                + response_dict[0]["examples"][i]["targetTerm"] \
                + response_dict[0]["examples"][i]["targetSuffix"]
    print(f"Source sentence: \n{source_sentence}")
    print(f"Target sentence: \n{target_sentence}")




