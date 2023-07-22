import os 
import json

class PersonalInformation:
    def __init__(self, name: str, age: int, phone: int, email: str):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email
        self.dict = {"name": self.name,
                    "age": self.age,
                    "phone": self.phone,
                    "email": self.email}


# Arrays
newFile = []

# Inputs
createNewFile = bool(int(input("Possible answers: 0 and 1\nDo you wish to create a new file? : ")))
peopleToAppend = int(input("Possible answers: Interger\nHow many people do you wish to add? : "))

# Strings
path = 'people.json'


if os.path.exists(path) and not createNewFile:
    with open(path, 'r') as file:
        newFile = json.load(file)
        originalNumberOfPeopleInFile = len(newFile)

def writeJson(info, list):
    with open(path, 'w') as file:
        list.append(info.dict)
        if createNewFile and len(list) == peopleToAppend:
            json.dump(list, file, indent=4, separators=(',',': '))
        elif not createNewFile and len(list) == peopleToAppend + originalNumberOfPeopleInFile:
            json.dump(list, file, indent=4, separators=(',',': '))

for i in range(peopleToAppend):
    personName = str(input(f"Name of person {i + 1} : "))
    personAge = int(input(f"Age of {personName} : "))
    personPhone = int(input(f"Phone number of {personName} : "))
    personEmail = str(input(f"Email of {personName} : "))
    personInfo = PersonalInformation(personName, personAge, personPhone, personEmail)
    writeJson(personInfo, newFile)