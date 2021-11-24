# import random module
import random

# set up blank list
zoo =[]

#Asks user for 5 animals to add to the zoo
for i in range (0,5):
    animal = input("Please add an animal to the zoo ")
    # adds animal to the zoo list
    zoo.append(animal)

# sorts list into alphabetica order
zoo.sort()

# prints list in one line
print(",".join(zoo))

valid = True
while True:
    #remove animal if in list
    remove_animal = input("What animal has left the zoo? ")
    if remove_animal in zoo:
        # gets animal list number
        index = zoo.index(remove_animal)
        print("{} has been removed from the zoo and was number {}".format(remove_animal,index))
        # removed animal from the list
        zoo.remove(remove_animal)
    else:
        print("That animal is not at the zoo")





