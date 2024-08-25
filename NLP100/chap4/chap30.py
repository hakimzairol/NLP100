def read_pos_tagged_file(file_path):
    sentences = []
    sentence = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # If the line is not empty
                columns = line.split('\t')
                if len(columns) >= 3:
                    word_data = {
                        'text': columns[0],  # Surface form
                        'lemma': columns[1], # Lemma (base form)
                        'pos': columns[2]    # Part-of-speech tag
                    }
                    sentence.append(word_data)
            else:  # An empty line indicates the end of a sentence
                if sentence:  # If there is a sentence accumulated
                    sentences.append(sentence)
                    sentence = []  # Reset for the next sentence
        
        # Add the last sentence if the file does not end with a blank line
        if sentence:
            sentences.append(sentence)
    return sentences

def inspect_pos_tags(file_path, num_lines=10):
    with open(file_path, 'r') as file:
        for _ in range(num_lines):
            line = file.readline().strip()
            if line:
                columns = line.split('\t')
                if len(columns) >= 3:
                    print(f"Word: {columns[0]}, Lemma: {columns[1]}, POS: {columns[2]}")
                else:
                    print("Malformed line:", line)
            else:
                break


def extract_verbs(sentences):
    verbs = []
    # Define a list of POS tags that generally represent verbs
    verb_tags = {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}

    for sentence in sentences:
        for word_data in sentence:
            if word_data['pos'] in verb_tags:
                verbs.append(word_data['text'])
    
    return verbs


file_path = "C:\\Users\\Hakim Hisham\\Documents\\NLP100\\alice\\alice.txt.conll"


pos_tagged_sentences = read_pos_tagged_file(file_path)
for word in pos_tagged_sentences[0]:
    print(word)

inspect_pos_tags(file_path)

if pos_tagged_sentences:
    verbs = extract_verbs(pos_tagged_sentences)
    print("Extracted verbs:")
    for verb in verbs:
        print(verb)

