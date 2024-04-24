import random
    
everyone = ["Red", "Blue", "Pink", "Yellow", "Black", "Green", "White", "Cyan", "Purple", "Orange"]
everyone_count = len(everyone)
astronauts = ["Red", "Blue", "Pink", "Yellow", "Black", "Green", "White", "Cyan", "Purple", "Orange"]
astronauts_count = len(astronauts)
imposters = []
imposters_count = int(input("How many imposters should be in the game? : "))

for i in range(imposters_count):
    random_imposter = random.randint(0, len(astronauts) - 1)
    imposters.append(astronauts.pop(random_imposter))   
print(f"{", ".join(imposters[:imposters_count - 1])} and {imposters[-1]} are the imposters!")

while True:
    vote = True
    kill = random.randint(0, 2)
    print(f"{", ".join(everyone[:everyone_count - 1])} and {everyone[-1]} are still alive.")

    if kill == 1:
        person_to_kill = astronauts[random.randint(0, len(astronauts) - 1)]
        everyone.remove(person_to_kill)
        astronauts.remove(person_to_kill)
        print(f"{person_to_kill} got killed!")

    if vote == True:
        person_to_vote = everyone[random.randint(0, len(everyone) - 1)]
        if person_to_vote in imposters:
            imposters.remove(person_to_vote)
        else:
            astronauts.remove(person_to_vote)
        everyone.remove(person_to_vote)
        print(f"{person_to_vote} got voted out!")

    everyone_count = len(everyone)
    astronauts_count = len(astronauts)
    imposters_count = len(imposters)

    if astronauts_count <= 2 and imposters_count == 2:
        print("The imposters won!")
        break

    if astronauts_count <= 1:
        print("The imposters won!")
        break

    if imposters_count <= 0:
        print("The crewmates won!")
        break