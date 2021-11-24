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
