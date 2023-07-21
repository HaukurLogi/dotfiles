import json


path = "words.json"


def backwards(string):
    for i in range(len(string)):
        if string[i] != string[len(string) -1 -i]:
            return False
        return True

#def backwards(string): 
  #  for i in range(len(string)):
   #     reverseString += string[-i + len(string) - 1]
    #return string == reverseString 

with open(path, 'rb') as file:
    contents = json.load(file)
    print(contents)
    for word in contents:
        if len(word) >= 3:
            if backwards(word):
                print(word)
