def generate_ngrams(text, n):
    words = text.split()
    n_grams = [words[i:i+n] for i in range (len(words)-n+1)]
    return [" ".join(ngram) for ngram in n_grams]

text = "I am an NLPer"

bigrams = generate_ngrams(text,2)

print("Bigrams", bigrams)