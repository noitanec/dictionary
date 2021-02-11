#!/usr/bin/env python3
import sys
import pprint
import requests

baseURL = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"

key = str(sys.argv[1])
URL = baseURL + key

response = requests.get(url=URL)

if response:
    data = response.json()

    print("\n\t", key, ": ", data[0]['meanings'][0]['definitions'][0]
          ['definition'])
    fields = data[0]['meanings'][0]['definitions'][0].keys()
    if 'synonyms' in fields:
        print("\n\tSynonyms: ", data[0]['meanings'][0]['definitions'][0]['synonyms'], "\n")
else:
    print("Try another word")
