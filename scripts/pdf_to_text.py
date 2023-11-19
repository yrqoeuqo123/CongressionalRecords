import PyPDF2
import os

# Directory where the downloaded PDFs are located
pdf_dir = r'YOUR_DIRECTORY_HERE'

# Directory where you want to save the extracted text files
text_dir = r'YOUR_DIRECTORY_HERE'

# Ensure the text directory exists
if not os.path.exists(text_dir):
    os.makedirs(text_dir)

# Function to extract text from a PDF file
def extract_text(pdf_filename, text_filename):
    try:
        with open(pdf_filename, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            text = ''
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                text += page.extractText()
        
        with open(text_filename, 'w', encoding='utf-8') as text_file:
            text_file.write(text)
        
        print(f"Text extracted from {pdf_filename} and saved to {text_filename}")
    except Exception as e:
        print(f"Error extracting text from {pdf_filename}: {str(e)}")

# Get a list of PDF files in the directory
pdf_files = [filename for filename in os.listdir(pdf_dir) if filename.endswith(".pdf")]

# Initialize a counter for tracking progress
total_pdfs = len(pdf_files)
processed_pdfs = 0

# Loop through the PDF files in the directory
for filename in pdf_files:
    pdf_path = os.path.join(pdf_dir, filename)
    text_filename = os.path.join(text_dir, os.path.splitext(filename)[0] + '.txt')
    extract_text(pdf_path, text_filename)
    
    # Increment the processed count
    processed_pdfs += 1

    # Calculate progress percentage
    progress = (processed_pdfs / total_pdfs) * 100
    print(f"Progress: {progress:.2f}%")
