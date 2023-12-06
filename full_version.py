import os
import re
import pdfplumber
import nltk
import yaml
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

"""
This script is part of an ongoing project to process and analyze text data from the Congressional Record. 
It is currently under construction, and we welcome patience and contributions from those interested in 
helping develop these tools further. The pipeline includes several steps: loading data, processing OCR files, 
extracting metadata, parsing speeches, cleaning text, and more. Each function is documented with its purpose 
and usage. The ultimate goal is to enable robust analysis of Congressional speeches and facilitate research 
into political discourse.
"""

# Ensure nltk resources are available
nltk.download('punkt')
nltk.download('stopwords')

# Directory configuration
pdf_dir = r'YOUR_DIRECTORY'
csv_dir = r'YOUR_DIRECTORY'
yaml_dir = r'YOUR_DIRECTORY'  # Update with the actual path to your YAML files

# Define a function to load YAML files containing congressperson data
def load_congressperson_data(yaml_dir):

    """
    Load congressperson data from YAML files in the specified directory.
    
    Args:
    yaml_dir (str): The directory containing YAML files with congressperson data.
    
    Returns:
    list: A list of dictionaries, each containing data of a single congressperson.
    """

    congressperson_data = []
    for yaml_file in os.listdir(yaml_dir):
        if yaml_file.endswith('.yaml'):
            yaml_path = os.path.join(yaml_dir, yaml_file)
            with open(yaml_path, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
                congressperson_data.append(data)
    return congressperson_data

def process_ocr_files(pdf_path):

    """
    Process OCR files from a given PDF path, extracting text from each page.
    
    Args:
    pdf_path (str): The file path to the PDF document.
    
    Returns:
    list: A list of strings, each representing text from a single page.
    """

    pages_text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                pages_text.append(page_text)  # Store text of each page separately
    return pages_text

def extract_metadata_from_text(text):

    """
    Extract metadata from the text of a single page using regular expressions.
    
    Args:
    text (str): Text content from which to extract metadata.
    
    Returns:
    dict: A dictionary containing extracted metadata such as congress, session, volume, date, and issue.
    """

    metadata = {}
    # Patterns to extract metadata from the text
    congress_pattern = r'THE (\d+)(TH|ST|ND|RD) CONGRESS'
    session_pattern = r'(\d+)(ST|ND|RD|TH) SESSION'
    volume_pattern = r'Vol\. (\d+)'
    date_pattern = r'([A-Z][a-z]+day), (\w+ \d{1,2}, \d{4})'
    issue_pattern = r'No\. (\d+)'
    
    metadata['congress'] = re.search(congress_pattern, text).group(1)
    metadata['session'] = re.search(session_pattern, text).group(1)
    metadata['volume'] = re.search(volume_pattern, text).group(1)
    metadata['date'] = re.search(date_pattern, text).group(2)
    metadata['issue'] = re.search(issue_pattern, text).group(1)

    return metadata

def parse_speeches(text):

    """
    Parse speeches from the text, separating each speech based on a predefined pattern.
    
    Args:
    text (str): Text content that contains multiple speeches.
    
    Returns:
    list: A list of speeches, split and separated from the text.
    """

    pattern = r'(Mr\.|Ms\.|Mrs\.) [A-Z][A-Z]+(?: [A-Z][A-Z]+)? of [A-Z][a-z]+'
    speeches = re.split(pattern, text)[1:]  # Split and ignore the first chunk as it's likely not a speech
    return speeches

def clean_speech_text(text):

    """
    Clean speech text by removing non-alphabetic characters, converting to lowercase, 
    tokenizing, removing stopwords, and applying stemming.
    
    Args:
    text (str): The speech text to be cleaned.
    
    Returns:
    str: A cleaned and processed version of the input text.
    """


    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic characters
    text = text.lower()  # Convert to lowercase
    tokens = nltk.word_tokenize(text)  # Tokenize
    filtered_tokens = [word for word in tokens if word not in stopwords.words('english')]  # Remove stopwords
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]  # Stemming
    return ' '.join(stemmed_tokens)

def match_congressperson_metadata(metadata, congressperson_data):

    """
    Match speech metadata with congressperson data to find the corresponding congressperson.
    
    Args:
    metadata (dict): A dictionary containing metadata of a speech.
    congressperson_data (list): A list of dictionaries containing congressperson data.
    
    Returns:
    dict or None: The matched congressperson's data or None if no match is found.
    """

    # Implement the matching logic here
    pass

def compute_bigram_counts(text):

    """
    Compute the counts of bigrams (two adjacent words) in the given text.
    
    Args:
    text (str): The text for which to compute bigram counts.
    
    Returns:
    Counter: A Counter object with bigrams as keys and their counts as values.
    """


    # Tokenize the text
    tokens = text.split()

    # Create bigrams
    bigrams = zip(tokens, tokens[1:])

    # Count bigrams
    bigram_counts = Counter(bigrams)
    return bigram_counts

def generate_vocabulary(speeches):

    """
    Generate a vocabulary from a collection of speeches. A vocabulary is a set of unique words that
    appear in the data corpus.

    Args:
    speeches (list of str): A list of speeches from which to extract the vocabulary.

    Returns:
    set: A set of unique words that make up the vocabulary of the corpus.
    """

    # Implement vocabulary generation here
    pass

def estimate_partisanship(phrases):

    """
    Estimate the partisanship of given phrases. Partisanship, in this context, refers to the political
    bias or alignment of the phrases, indicating whether they are more frequently used by a particular
    political party or ideology.

    Args:
    phrases (list of str): A list of phrases to analyze for partisanship.

    Returns:
    dict: A dictionary mapping each phrase to its estimated partisanship score.
    """

    # Implement partisanship estimation here
    pass

def classify_phrases_into_topics(phrases):

    """
    Classify phrases into topics based on their content. This helps in categorizing text data into
    thematic groups, which can be useful for understanding the main subjects of discourse.

    Args:
    phrases (list of str): A list of phrases to classify into topics.

    Returns:
    dict: A dictionary mapping each phrase to its respective topic(s).
    """

    # Implement topic classification here
    pass

def match_congressperson_metadata(metadata, congressperson_data):

    """
    Match metadata extracted from speeches with congressperson data to identify the speaker.

    Args:
    metadata (dict): Metadata extracted from a speech, which may include the speaker's name, state, etc.
    congressperson_data (list of dict): A list of dictionaries, each containing data about a congressperson.

    Returns:
    dict or None: The matched congressperson's data if a match is found; otherwise, None.
    """

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
            pages_text = process_ocr_files(pdf_path)

            for page_text in pages_text:
                # Extract metadata from each page
                metadata = extract_metadata_from_text(page_text)
                
                # Speech parsing, cleaning, and bigram count computation
                speeches = parse_speeches(page_text)
                bigram_counts_all = []
                for speech in speeches:
                    cleaned_text = clean_speech_text(speech)
                    bigram_counts = compute_bigram_counts(cleaned_text)
                    bigram_counts_all.append(bigram_counts)

                    # Match metadata with congressperson data
                    matched_congressperson = match_congressperson_metadata(metadata, congressperson_data)
                    if matched_congressperson:
                        # Assign speech to the associated congressperson
                        # You can implement this logic as needed
                        pass  # Placeholder for additional logic

                # Further processing like vocabulary generation, partisanship estimation, topic classification
                # (These functions need to be implemented)
                # vocabulary = generate_vocabulary(speeches)
                # partisanship = estimate_partisanship(vocabulary)
                # topics = classify_phrases_into_topics(vocabulary)

                # Save or handle the processed data as needed
                # (This needs to be implemented)
                pass  # Placeholder for saving or processing the data

if __name__ == "__main__":
    main()