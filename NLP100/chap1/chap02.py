a = "shoe"
b = "cold"

c = []

for x,y in zip(a,b):
    c.append(x+y)

print(c)

txt = "".join(c)
print(txt)

