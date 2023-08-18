from bs4 import BeautifulSoup
import googlesearch
import re
import requests


object = str(input("What object would you like to get the dimensions of? : "))
unitsOfMeasurement = ['cm', 'centimeters', 'mm', 'millimeters', 'm', 'meters', 'ft', 'feet', 'in', 'inches']


for url in googlesearch.search(f"{object} size", stop=20):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    
    text = soup.get_text()
    text.encode('utf-8')
    numbers = [int(i) for i in text.split() if i.isdigit()]

    for number in text.split():
        if number.isdigit(): # if the word is an interger then it looks for the word after the interger, if the word after the interger is one of the units of measurement then it prints it in the terminal
            wordAfterNumber = text.partition(number)[2].split(' ')[1]
            for unit in unitsOfMeasurement:
                if wordAfterNumber == unit:
                    print(f"{number} {unit}")

