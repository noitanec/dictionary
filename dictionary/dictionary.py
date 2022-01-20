#!/usr/bin/env python3
import sys
import requests

baseURL = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"

key = ' '.join(sys.argv[1:])
URL = baseURL + key

response = requests.get(url=URL)

if response:
    data = response.json()

    print("\n\t", key.upper(), ": ", data[0]['meanings'][0]['definitions'][0]
          ['definition'])
    fields = data[0]['meanings'][0]['definitions'][0].keys()
    if 'synonyms' in fields:
        print("\n\t SYNONYMS: ", data[0]['meanings']
              [0]['definitions'][0]['synonyms'], "\n")
    if 'example' in fields:
        print("\n\t EXAMPLE: ", data[0]['meanings']
              [0]['definitions'][0]['example'], "\n")
else:
    print("Try another word")
