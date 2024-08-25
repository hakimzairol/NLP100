import random

message = input("Enter a string: ")

split_message = message.split()

shuffled_message = []

for word in split_message:
    if len(word) > 4:
        shuffle = list(word)

        first_letter = shuffle[0]
        last_letter = shuffle[-1]

        middle_part = list(shuffle[1:-1])

        random.shuffle(middle_part)

        shuffled_word = first_letter + "".join(middle_part) + last_letter

        shuffled_message.append(shuffled_word)
    else:
        shuffled_message.append(word)

shuffled_string = " ".join(shuffled_message)


print("Shuffled Message: ", shuffled_string)





    

