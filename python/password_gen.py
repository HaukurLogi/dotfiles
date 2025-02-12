import random
import os
import json

path = 'account_info.json'

first_name = input("First name : ").lower()
last_name = input("Last name : ").lower()

username = first_name[:1]+last_name
password = random.randint(0, 9999)

def writeFile(info, list):
    with open(path, 'w') as file:
        list.append(info.dict)
        if clear_file and len(list) == people_to_append:
            json.dump(list, file, indent=4, separators=(',',': '))
        elif not clear_file and len(list) == people_to_append + original_number_of_people_in_file:
            json.dump(list, file, indent=4, separators=(',',': '))

def writeJson(info, list):
    with open(path, 'w') as file:
        list.append(info.dict)
        if clear_file and len(list) == people_to_append:
            json.dump(list, file, indent=4, separators=(',',': '))
        elif not clear_file and len(list) == people_to_append + original_number_of_people_in_file:
            json.dump(list, file, indent=4, separators=(',',': '))


path = 'people.json'
new_file = []


if os.path.exists(path):
    if os.stat(path).st_size: # Checks if json file is empty
        add_people = bool(int(input("If you only want to list already registered people, press 0\nPossible answers: 0 and 1\nDo you wish to add more people? : ")))
    else:
        add_people = True
    if add_people:
        if os.stat(path).st_size: # Checks if json file is empty
            clear_file = bool(int(input("Possible answers: 0 and 1\nDo you wish to clear existing file? : ")))
            if not clear_file:
                    with open(path, 'r') as file:
                        new_file = json.load(file)
                        original_number_of_people_in_file = len(new_file)
        else:
            clear_file = True
        people_to_append = int(input("Possible answers: Interger\nHow many people do you wish to add? : "))
        for i in range(people_to_append):
            person_name = str(input(f"Name of person {i + 1} : "))
            person_age = int(input(f"Age of {person_name} : "))
            person_phone = int(input(f"Phone number of {person_name} : "))
            person_email = str(input(f"Email of {person_name} : "))
            person_info = PersonalInformation(person_name, person_age, person_phone, person_email)
            writeJson(person_info, new_file)
    else:
        with open(path, 'r') as file:
            json_contents = json.load(file)
            for person in json_contents:
                print(f"\nPerson : {person['name']}\nAge : {person['age']}\nPhone : {person['phone']}\nEmail : {person['email']}\n")
else:
    with open(path, 'w') as file:
        pass

print(username, password)