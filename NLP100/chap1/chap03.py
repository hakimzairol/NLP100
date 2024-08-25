text = "Now i need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"

list = text.split(" ")

print(list)

lengths = []

for i in list:
    lengths.append(len(i))

print(lengths)
