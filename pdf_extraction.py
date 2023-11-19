import requests
import csv
import os
import time

# Directory where you want to save the downloaded PDFs
pdf_dir = r'YOUR_DIRECTORY_HERE'

# Ensure the PDF directory exists
if not os.path.exists(pdf_dir):
    os.makedirs(pdf_dir)

# Function to download a PDF from a URL and save it
def download_pdf(pdf_url, pdf_filename, default_wait=60):
    while True:
        response = requests.get(pdf_url)
        if response.status_code == 200:
            with open(pdf_filename, 'wb') as pdf_file:
                pdf_file.write(response.content)
            print(f"Downloaded {pdf_filename}")
            break
        elif response.status_code == 429:
            wait_time = response.headers.get('Retry-After', default_wait)
            print(f"Rate limit exceeded, retrying after {wait_time} seconds")
            time.sleep(int(wait_time))
        else:
            print(f"Failed to download {pdf_filename} (Status code: {response.status_code})")
            break

# Directory where the CSV files are located
csv_dir = r'YOUR_DIRECTORY_HERE'

# Directory to save the PDFs within the same directory as CSV files
saved_pdf_dir = os.path.join(csv_dir, 'savedPDF')

# Ensure the "savedPDF" directory exists
if not os.path.exists(saved_pdf_dir):
    os.makedirs(saved_pdf_dir)

# Loop through the CSV files in the directory
for filename in os.listdir(csv_dir):
    if filename.endswith(".csv"):
        csv_path = os.path.join(csv_dir, filename)
        
        # Read the CSV file
        with open(csv_path, mode='r') as file:
            csv_reader = csv.reader(file)
            
            # Skip the header row
            next(csv_reader)
            
            # Loop through the rows in the CSV
            for row in csv_reader:
                pdf_url = row[5]  # Assuming the PDF URL is in the 6th column
                if pdf_url:
                    pdf_filename = os.path.join(saved_pdf_dir, f"{row[0]}_{row[1]}.pdf")  # Using Congress and ID for the filename
                    download_pdf(pdf_url, pdf_filename)
