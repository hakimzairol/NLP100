import json

class Word:
    def __init__(self, text, lemma, pos):
        self.text = text
        self.lemma = lemma
        self.pos = pos
    
    def __repr__(self):
        return f"Word(text='{self.text}', lemma='{self.lemma}', pos='{self.pos}')"

def read_dependency_parse_result(file_path):
    try:
        # Attempt to open the file with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except UnicodeDecodeError:
        print("Error decoding the file. Trying a different encoding...")
        # You might need to try different encodings if UTF-8 doesn't work
        with open(file_path, 'r', encoding='cp932') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        data = None
    except json.JSONDecodeError:
        print("Error decoding JSON. The file may be corrupted or not in JSON format.")
        data = None
    return data

def create_sentences(data):
    sentences = []
    
    if data and 'sentences' in data:
        for sentence_data in data['sentences']:
            sentence = []
            for token in sentence_data['tokens']:
                word = Word(
                    text=token['word'],
                    lemma=token['lemma'],
                    pos=token['pos']
                )
                sentence.append(word)
            sentences.append(sentence)
    
    return sentences

def display_first_sentence(sentences):
    if sentences:
        first_sentence = sentences[0]
        for word in first_sentence:
            print(word)
    else:
        print("No sentences found.")

# Example usage
file_path = 'ai.en.txt.json'
data = read_dependency_parse_result(file_path)
if data:
    sentences = create_sentences(data)
    display_first_sentence(sentences)

