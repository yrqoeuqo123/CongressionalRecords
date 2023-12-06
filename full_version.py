import os
import re
import pdfplumber
import nltk
import yaml
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Ensure nltk resources are available
nltk.download('punkt')
nltk.download('stopwords')

# Directory configuration
pdf_dir = r''
csv_dir = r''
yaml_dir = r''  # Update with the actual path to your YAML files

# Define a function to load YAML files containing congressperson data
def load_congressperson_data(yaml_dir):
    congressperson_data = []
    for yaml_file in os.listdir(yaml_dir):
        if yaml_file.endswith('.yaml'):
            yaml_path = os.path.join(yaml_dir, yaml_file)
            with open(yaml_path, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
                congressperson_data.append(data)
    return congressperson_data

def process_ocr_files(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + ' '  # Concatenate text from each page
    return text

def parse_speeches(text):
    pattern = r'(Mr\.|Ms\.|Mrs\.) [A-Z][A-Z]+(?: [A-Z][A-Z]+)? of [A-Z][a-z]+'
    speeches = re.split(pattern, text)[1:]  # Split and ignore the first chunk as it's likely not a speech
    return speeches

def clean_speech_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic characters
    text = text.lower()  # Convert to lowercase
    tokens = nltk.word_tokenize(text)  # Tokenize
    filtered_tokens = [word for word in tokens if word not in stopwords.words('english')]  # Remove stopwords
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]  # Stemming
    return ' '.join(stemmed_tokens)

def match_congressperson_metadata(metadata, congressperson_data):
    # Implement the matching logic here
    pass

def compute_bigram_counts(text):
    # Tokenize the text
    tokens = text.split()

    # Create bigrams
    bigrams = zip(tokens, tokens[1:])

    # Count bigrams
    bigram_counts = Counter(bigrams)
    return bigram_counts

def generate_vocabulary(speeches):
    # Implement vocabulary generation here
    pass

def estimate_partisanship(phrases):
    # Implement partisanship estimation here
    pass

def classify_phrases_into_topics(phrases):
    # Implement topic classification here
    pass

def match_congressperson_metadata(metadata, congressperson_data):
    matched_congressperson = None
    # Implement your matching logic here
    for congressperson in congressperson_data:
        # Compare the extracted metadata with congressperson data
        if (
            metadata['first_name'] == congressperson['first_name'] and
            metadata['last_name'] == congressperson['last_name'] and
            metadata['chamber'] == congressperson['chamber'] and
            metadata['gender'] == congressperson['gender'] and
            metadata['state'] == congressperson['state']
        ):
            matched_congressperson = congressperson
            break
    return matched_congressperson

def main():
    # Load congressperson data from YAML files
    congressperson_data = load_congressperson_data(yaml_dir)
for file in os.listdir(pdf_dir):
    if file.endswith('.pdf'):
        pdf_path = os.path.join(pdf_dir, file)
        text = process_ocr_files(pdf_path)

        # Speech parsing, cleaning, and bigram count computation
        speeches = parse_speeches(text)
        bigram_counts_all = []
        for speech in speeches:
            cleaned_text = clean_speech_text(speech)
            bigram_counts = compute_bigram_counts(cleaned_text)
            bigram_counts_all.append(bigram_counts)

            # Metadata extraction
            metadata = extract_metadata(speech)

            # Match metadata with congressperson data
            matched_congressperson = match_congressperson_metadata(metadata, congressperson_data)
            if matched_congressperson:
                # Assign speech to the associated congressperson
                # Implement this logic as needed
                # For example, you might want to append the speech to a list associated with the congressperson
                pass  # Replace 'pass' with your implementation

        # Further processing like vocabulary generation, partisanship estimation, topic classification
        vocabulary = generate_vocabulary(speeches)
        partisanship = estimate_partisanship(vocabulary)
        topics = classify_phrases_into_topics(vocabulary)

        # Save or handle the processed data as needed

if __name__ == "__main__":
    main()
