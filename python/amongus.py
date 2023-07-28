import random
def main():

    
    astronauts = ['Red', 'Blue', 'Pink', 'Yellow', 'Black', 'Green', 'White', 'Cyan', 'Purple', 'Orange']
    everyone = ['Red', 'Blue', 'Pink', 'Yellow', 'Black', 'Green', 'White', 'Cyan', 'Purple', 'Orange']
    imposters = ['','','','','','','','']


    imposter1 = random.randint(0,9)
    imposter2 = random.randint(0,9)


    if imposter1 != imposter2:
        imposter = astronauts[imposter1]   
        other_imposter = astronauts[imposter2] 
        imposters.insert(imposter1, imposter)
        imposters.insert(imposter2, other_imposter)
        astronauts.remove(imposter)
        astronauts.insert(imposter1, '')
        astronauts.remove(other_imposter)
        astronauts.insert(imposter2, '')
    else:
        print("The imposters we're the same please try again :/")

    print(f"{imposter} and {other_imposter} are the imposters.")
    while True:
        vote = True
        person_to_vote = random.randint(0,len(everyone) - 1)
        kill = random.randint(0,1)
        person_to_kill = random.randint(0,len(astronauts) - 1)

        if kill == 0:
            if astronauts[person_to_kill] != '':
                print(f"{astronauts[person_to_kill]} got killed!")
                astronauts[person_to_kill] = ''
                everyone[person_to_kill] = ''

        if vote == True:
            if everyone[person_to_vote] != '':
                print(f"{everyone[person_to_vote]} got voted out!")
                astronauts[person_to_vote] = ''
                everyone[person_to_vote] = ''
                imposters[person_to_vote] = ''

        astronauts_count = sum([v != '' for v in astronauts])
        imposters_count = sum([v != '' for v in imposters])

        if astronauts_count <= 2 and imposters_count == 2:
            print("The imposters won!")
            break

        if astronauts_count <= 1:
            print("The imposters won!")
            break

        if imposters_count <= 0:
            print("The crewmates won!")
            break

main()