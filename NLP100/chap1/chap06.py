# function to generate bigrams from a word
def generate_bigrams(word):
    return {word[i:i+2] for i in range(len(word)-2+1)}

str1 = "paraparaparadise"
str2 = "paragraph"

X = generate_bigrams(str1)
Y = generate_bigrams(str2)

#compute union, intersection, and difference
union = X | Y
intersection = X & Y
difference_X_Y = X - Y
difference_Y_X = Y - X

#check for presence of bi-gram "se"
contains_se_X = "se" in X
contains_se_Y = "se" in Y

#print results
print("Set X:", X)
print("Set Y:", Y)
print("Union:", union)
print("Intersection:", intersection)
print("Difference X - Y:", difference_X_Y)
print("Difference Y - X:", difference_Y_X)
print('Is "se" in X?', contains_se_X)
print('Is "se" in Y?', contains_se_Y)
