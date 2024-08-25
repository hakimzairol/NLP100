def cipher(string):
    message = []
    for i in range (len(string)):
        if string[i] == "c":
            new_char = chr(219)
            message.append(new_char)

        else:
            message.append(string[i])
    return "".join(message)

def decipher(string):
    message = []
    for i in range (len(string)):
        if string[i] == "Û":
            new_char = "c"
            message.append(new_char)

        else:
            message.append(string[i])
    return "".join(message)

message = " Hello World! This is a test message containing c"

ciphered = cipher(message)
deciphered = decipher(message)

print("Original: ", message)
print( "Ciphered: ",ciphered)
print("Deciphered: ",deciphered)

