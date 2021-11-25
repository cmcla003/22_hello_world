names = ["Jack", "Jacob", "Jamie"]

print(names[2])
print(names)
print(", ".join(names))

# add names to list
names.append("John")
names.insert(1,"Juan")
print(names)

# remove names from list
names.pop(0)
print(names)
names.remove("Jacob")
print(", ".join(names))
