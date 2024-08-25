text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"

list = text.split(" ")

print(list)

firstletter = [0,4,5,6,7,8,14,15,18]
twoletter = [1,2,3,9,10,11,12,13,16,17,19]

for i,name in enumerate(list):
    if i in firstletter:
        print(name[0])
    else:
        print(name[0:2])
    


