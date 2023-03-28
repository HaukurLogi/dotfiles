import json
from random import randint

path = '5-letter-words.json'

with open(path, 'rb') as file:
    contents = json.load(file)["words"]
    
    random_word = contents[randint(0, len(contents))]
    print(random_word)
