import os
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from tqdm import tqdm

'''
This script preprocesses the text files extracted from the PDFs.
Preprocessing steps:
    1. Convert to lowercase
    2. Remove punctuation
    3. Tokenize text
    4. Remove stopwords and numbers
    5. (Optional) Stem words

Preprocessing is always important, but especially so for topic modeling.

The files are already saved and you could find them in the folder "Processed_Text" on my GitHub.
Be careful the processed texts on the github are stemmed. 
If you do not want to stem the texts, you could change the use_stemmer to false.
'''


# Download stopwords from NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Set the directories
input_directory = r'Your directory here'
output_directory = r'Your directory here'

# Check if output directory exists, if not, create it
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Initialize a stemmer (optional, set to False to disable)
use_stemmer = True
stemmer = PorterStemmer() if use_stemmer else None

# Preprocess a single file
def preprocess_file(file_path, stemmer=None):
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
            for word in tokens if word.isalpha() and word not in stopwords.words('english')
        ]

        return ' '.join(processed_text)

# File names to process
file_names = [f'Congress_{i}.txt' for i in range(104, 119)]

# Process and save files with tqdm progress bar
for file_name in tqdm(file_names, desc="Processing files", unit="file"):
    input_file_path = os.path.join(input_directory, file_name)
    output_file_path = os.path.join(output_directory, f'Processed_{file_name}')

    if os.path.exists(input_file_path):
        processed_data = preprocess_file(input_file_path, stemmer)
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(processed_data)
    else:
        print(f'{file_name} does not exist.')

print('Processing complete.')
