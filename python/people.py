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

def writeJson(info, list):
    with open(path, 'w') as file:
        list.append(info.dict)
        if clearFile and len(list) == peopleToAppend:
            json.dump(list, file, indent=4, separators=(',',': '))
        elif not clearFile and len(list) == peopleToAppend + originalNumberOfPeopleInFile:
            json.dump(list, file, indent=4, separators=(',',': '))


path = 'people.json'
newFile = []


if os.path.exists(path):
    if os.stat(path).st_size: # Checks if json file is empty
        addPeople = bool(int(input('If you only want to list already registered people, press "0"\nPossible answers: 0 and 1\nDo you wish to add more people? : ')))
    else:
        addPeople = True
    if addPeople:
        if os.stat(path).st_size: # Checks if json file is empty
            clearFile = bool(int(input("Possible answers: 0 and 1\nDo you wish to clear existing file? : ")))
            if not clearFile:
                    with open(path, 'r') as file:
                        newFile = json.load(file)
                        originalNumberOfPeopleInFile = len(newFile)
        else:
            clearFile = True
        peopleToAppend = int(input("Possible answers: Interger\nHow many people do you wish to add? : "))
        for i in range(peopleToAppend):
            personName = str(input(f"Name of person {i + 1} : "))
            personAge = int(input(f"Age of {personName} : "))
            personPhone = int(input(f"Phone number of {personName} : "))
            personEmail = str(input(f"Email of {personName} : "))
            personInfo = PersonalInformation(personName, personAge, personPhone, personEmail)
            writeJson(personInfo, newFile)
    else:
        with open(path, 'r') as file:
            jsonContents = json.load(file)
            for person in jsonContents:
                print(f"\nPerson : {person['name']}\nAge : {person['age']}\nPhone : {person['phone']}\nEmail : {person['email']}\n")
else:
    with open(path, 'w') as file:
        pass