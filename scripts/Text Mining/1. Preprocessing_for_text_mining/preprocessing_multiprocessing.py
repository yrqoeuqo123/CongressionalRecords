import os
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from tqdm import tqdm
from multiprocessing import Pool

# Download stopwords from NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Set the directories
input_directory = r'C:\Users\Tianyi Zhang\Desktop\Lab\Extracted_Text'
output_directory = r'C:\Users\Tianyi Zhang\Desktop\Lab\Processed_Text'

# Check if output directory exists, if not, create it
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Initialize a stemmer (optional, set to False to disable)
use_stemmer = True
stemmer = PorterStemmer() if use_stemmer else None

# Load stopwords only once
stop_words = set(stopwords.words('english'))

# Preprocess a single file
def preprocess_file(file_name, stemmer=None):
    file_path = os.path.join(input_directory, file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

        # Convert to lowercase
        text = text.lower()

        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Tokenize text
        tokens = word_tokenize(text)

        # Remove stopwords and numbers, and optionally stem words
        processed_text = [
            stemmer.stem(word) if stemmer else word
            for word in tokens if word.isalpha() and word not in stop_words
        ]

        return ' '.join(processed_text)

# Function to be executed in parallel
def process_file(file_name):
    input_file_path = os.path.join(input_directory, file_name)
    output_file_path = os.path.join(output_directory, f'Processed_{file_name}')
    
    if os.path.exists(input_file_path):
        processed_data = preprocess_file(file_name, stemmer)
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(processed_data)

if __name__ == "__main__":
    file_names = [f'Congress_{i}.txt' for i in range(104, 119)]

    # Using Pool to parallelize processing
    with Pool() as pool:
        list(tqdm(pool.imap(process_file, file_names), total=len(file_names), desc="Processing files", unit="file"))

    print('Processing complete.')
