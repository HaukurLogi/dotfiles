import os 
import json
import gc

class PersonalInformation:
    def __init__(self, name: str, age: int, phone: int):
        self.name = name
        self.age = age
        self.phone = phone
        self.dict = {"name": self.name,
                    "age": self.age,
                    "phone": self.phone}


# Arrays
listObj = []

# Inputs
newFile = bool(input("Possible answers: True or False\nDo you wish to create a new file? : "))
people = int(input("Possible answers: Interger\nHow many people do you wish to add? : "))

# Strings
jsonFile = 'people.json'


for i in range(people - 1):
    personName = str(input(f"Name of person {i + 1} : "))
    personAge = int(input(f"Age of {personName} : "))
    personPhone = int(input(f"Phone number of {personName} : "))
    globals()[personName] = PersonalInformation(personName, personAge, personPhone)

with open(jsonFile, 'w') as file:
    for obj in gc.get_objects():
        if isinstance(obj, PersonalInformation):
            listObj.append(obj.dict)
            if len(listObj) == people:
                json.dump(listObj, file, indent=4, separators=(',',': '))