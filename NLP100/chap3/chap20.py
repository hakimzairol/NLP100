import gzip
import json
import re

def read_uk_article(file_path):
    try:
        with gzip.open(file_path, 'rt', encoding='utf-8') as file:
            for line in file:
                # Parse each line as a JSON object
                article = json.loads(line)

                # Check if the title of the article is "United Kingdom"
                if article.get('title') == 'United Kingdom':
                    # Return the body of the article
                    return article.get('text', 'No text available')

        return "Article on 'United Kingdom' not found."

    except FileNotFoundError:
        return "File not found."
    except json.JSONDecodeError:
        return "Error decoding JSON."


def extract_categories(file_path):
    category_pattern = re.compile(r'\[\[Category:(.*?)\]\]')
    category_lines = []

    try:
        with gzip.open(file_path, 'rt', encoding='utf-8') as file:
            for line in file:
                # Parse each line as a JSON object
                article = json.loads(line)

                # Get the article text
                text = article.get('text', '')

                # Find all category names in the text
                categories = category_pattern.findall(text)

                if categories:
                    # Store the categories along with the article title
                    category_lines.append({
                        'title': article.get('title', 'No Title'),
                        'categories': categories
                    })

        return category_lines

    except FileNotFoundError:
        print("File not found.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return []



def extract_category_names(file_path):
    category_pattern = re.compile(r'\[\[Category:(.*?)\]\]')
    category_names = []

    try:
        with gzip.open(file_path, 'rt', encoding='utf-8') as file:
            for line in file:
                # Parse each line as a JSON object
                article = json.loads(line)

                # Get the article text
                text = article.get('text', '')

                # Find all category names in the text
                categories = category_pattern.findall(text)

                if categories:
                    category_names.extend(categories)

        return category_names

    except FileNotFoundError:
        print("File not found.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return []


def extract_section_structure(file_path):
    section_pattern = re.compile(r'^(=+)\s*(.*?)\s*\1$', re.MULTILINE)
    section_structure = []

    try:
        with gzip.open(file_path, 'rt', encoding='utf-8') as file:
            for line in file:
                # Parse each line as a JSON object
                article = json.loads(line)

                # Check if the article is about the "United Kingdom"
                if article.get('title') == 'United Kingdom':
                    # Extract the text of the article
                    text = article.get('text', '')

                    # Find all sections and their levels
                    sections = section_pattern.findall(text)

                    for section in sections:
                        level = len(section[0]) - 1  # Number of equal signs minus one gives the level
                        section_name = section[1].strip()  # Get the section name
                        section_structure.append((level, section_name))

                    return section_structure

    except FileNotFoundError:
        print("File not found.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return []


def extract_media_references(file_path):
    media_pattern = re.compile(r'\[\[(File|Image):([^|\]]+).*?\]\]')
    media_references = []

    try:
        with gzip.open(file_path, 'rt', encoding='utf-8') as file:
            for line in file:
                # Parse each line as a JSON object
                article = json.loads(line)

                # Check if the article is about the "United Kingdom"
                if article.get('title') == 'United Kingdom':
                    # Extract the text of the article
                    text = article.get('text', '')

                    # Find all media file references
                    media_files = media_pattern.findall(text)

                    for media in media_files:
                        media_references.append(media[1].strip())

                    return media_references

    except FileNotFoundError:
        print("File not found.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return []

def extract_infobox_country(file_path):
    infobox_pattern = re.compile(r'\{\{Infobox country(.*?)\n\}\}', re.DOTALL)
    field_pattern = re.compile(r'\|\s*(.*?)\s*=\s*(.*?)(?=\n\|)', re.DOTALL)

    infobox_data = {}

    try:
        with gzip.open(file_path, 'rt', encoding='utf-8') as file:
            for line in file:
                # Parse each line as a JSON object
                article = json.loads(line)

                # Check if the article is about the "United Kingdom"
                if article.get('title') == 'United Kingdom':
                    # Extract the text of the article
                    text = article.get('text', '')

                    # Extract the Infobox country section
                    infobox_match = infobox_pattern.search(text)

                    if infobox_match:
                        infobox_content = infobox_match.group(1)

                        # Extract each field and its value
                        fields = field_pattern.findall(infobox_content)

                        for field, value in fields:
                            infobox_data[field.strip()] = value.strip()

                    return infobox_data

    except FileNotFoundError:
        print("File not found.")
        return {}
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return {}


def extract_infobox_country(file_path):
    infobox_pattern = re.compile(r'\{\{Infobox country(.*?)\n\}\}', re.DOTALL)
    field_pattern = re.compile(r'\|\s*(.*?)\s*=\s*(.*?)(?=\n\|)', re.DOTALL)
    emphasis_pattern = re.compile(r"''+")

    infobox_data = {}

    try:
        with gzip.open(file_path, 'rt', encoding='utf-8') as file:
            for line in file:
                # Parse each line as a JSON object
                article = json.loads(line)

                # Check if the article is about the "United Kingdom"
                if article.get('title') == 'United Kingdom':
                    # Extract the text of the article
                    text = article.get('text', '')

                    # Extract the Infobox country section
                    infobox_match = infobox_pattern.search(text)

                    if infobox_match:
                        infobox_content = infobox_match.group(1)

                        # Extract each field and its value
                        fields = field_pattern.findall(infobox_content)

                        for field, value in fields:
                            # Remove emphasis markups
                            clean_value = emphasis_pattern.sub('', value.strip())
                            infobox_data[field.strip()] = clean_value

                    return infobox_data

    except FileNotFoundError:
        print("File not found.")
        return {}
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return {}


def extract_infobox_country(file_path):
    infobox_pattern = re.compile(r'\{\{Infobox country(.*?)\n\}\}', re.DOTALL)
    field_pattern = re.compile(r'\|\s*(.*?)\s*=\s*(.*?)(?=\n\|)', re.DOTALL)
    emphasis_pattern = re.compile(r"''+")
    link_pattern = re.compile(r'\[\[(?:[^|\]]*\|)?([^|\]]+)\]\]')

    infobox_data = {}

    try:
        with gzip.open(file_path, 'rt', encoding='utf-8') as file:
            for line in file:
                # Parse each line as a JSON object
                article = json.loads(line)

                # Check if the article is about the "United Kingdom"
                if article.get('title') == 'United Kingdom':
                    # Extract the text of the article
                    text = article.get('text', '')

                    # Extract the Infobox country section
                    infobox_match = infobox_pattern.search(text)

                    if infobox_match:
                        infobox_content = infobox_match.group(1)

                        # Extract each field and its value
                        fields = field_pattern.findall(infobox_content)

                        for field, value in fields:
                            # Remove emphasis markups
                            clean_value = emphasis_pattern.sub('', value.strip())
                            # Remove internal links
                            clean_value = link_pattern.sub(r'\1', clean_value)
                            infobox_data[field.strip()] = clean_value

                    return infobox_data

    except FileNotFoundError:
        print("File not found.")
        return {}
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return {}


file_path = 'enwiki-country.json.gz'

read_article = read_uk_article(file_path)
print("Successfully Read UK Articles!")

categories = extract_categories(file_path)
for entry in categories:
    print(f"Article Title: {entry['title']}")
    print(f"Categories: {', '.join(entry['categories'])}")
    print()

categories_name = extract_category_names(file_path)
for names in categories_name:
    print(names)

sections = extract_section_structure(file_path)
for level, section_name in sections:
    print(f"Level {level}: {section_name}")

media_references = extract_media_references(file_path)
for media in media_references:
    print(media)

infobox = extract_infobox_country(file_path)
for field, value in infobox.items():
    print(f"{field}: {value}")

infobox = extract_infobox_country(file_path)
for field, value in infobox.items():
    print(f"{field}: {value}")

infobox = extract_infobox_country(file_path)
for field, value in infobox.items():
    print(f"{field}: {value}")