import json

class Word:
    def __init__(self, text, lemma, pos, head=None, dep=None, children=None):
        self.text = text
        self.lemma = lemma
        self.pos = pos
        self.head = head
        self.dep = dep
        self.children = children if children is not None else []
    
    def __repr__(self):
        return (f"Word(text='{self.text}', lemma='{self.lemma}', pos='{self.pos}', "
                f"head='{self.head.text if self.head else None}', dep='{self.dep}', "
                f"children={[child.text for child in self.children]})")

def read_dependency_parse_result(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except UnicodeDecodeError:
        print("Error decoding the file. Trying a different encoding...")
        with open(file_path, 'r', encoding='cp932') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        data = None
    except json.JSONDecodeError:
        print("Error decoding JSON. The file may be corrupted or not in JSON format.")
        data = None
    return data

def create_sentences_with_dependencies(data):
    sentences = []
    
    if data and 'sentences' in data:
        for sentence_data in data['sentences']:
            words = {}
            for token in sentence_data['tokens']:
                word = Word(
                    text=token.get('word', ''),
                    lemma=token.get('lemma', ''),
                    pos=token.get('pos', ''),
                    head=None,
                    dep=token.get('dep', None),
                    children=[]
                )
                words[token.get('index')] = word
            
            # Set head and children relationships
            for token in sentence_data['tokens']:
                word = words.get(token.get('index'))
                head_index = token.get('head', 0)  # Default to 0 if 'head' is missing
                if head_index != 0:
                    head_word = words.get(head_index)
                    word.head = head_word
                    if head_word:
                        head_word.children.append(word)
            
            # Append the sentence with words in order
            sentence = [words[i] for i in sorted(words)]
            sentences.append(sentence)
    
    return sentences

def display_root_words(sentences):
    if sentences:
        for idx, sentence in enumerate(sentences):
            root_words = [word for word in sentence if word.head is None]
            print(f"Sentence {idx + 1} root words:")
            for root_word in root_words:
                print(f"Root Word: {root_word.text}")
            print()  # Print an empty line between sentences
    else:
        print("No sentences found.")

# Example usage
file_path = 'ai.en.txt.json'
data = read_dependency_parse_result(file_path)
if data:
    sentences = create_sentences_with_dependencies(data)
    display_root_words(sentences)
