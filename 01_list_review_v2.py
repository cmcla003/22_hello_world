import random

saying = "How vexingly quick daft zebras jump!"

char_list = list(saying)
word_list = saying.split()
print(", ".join(char_list))
print(word_list)

junk_food =["Chocolate", "Chips", "Icecream", "Pies", "Cupcakes", "Chocolate", "Chips"]

for item in junk_food:
    print(item)
    print(junk_food.count(item))

print(junk_food.index("Icecream"))

print(junk_food)
print(" ".join(junk_food))
junk_food.sort()
print(junk_food)
random.shuffle(junk_food)
print(junk_food)

5*3

