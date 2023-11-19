# CongressionalRecords

## Overview
`CongressionalRecords` is an automated Python toolkit designed to extract and convert U.S. Congressional records from the GPO website into a text format. This repository includes scripts for web scraping URLs, downloading PDF files, and transforming these PDFs into readable text files using PyPDF2. The primary goal is to streamline the process of accessing and analyzing congressional documents, making it easier for researchers, data analysts, and policy enthusiasts to work with this valuable data.

## Features
- **Web Scraping**: Automatically scrape URLs of congressional records from the GPO website.
- **PDF Downloading**: Download PDFs of the congressional records from the scraped URLs.
- **PDF to Text Conversion**: Convert the downloaded PDF documents into text files for easier analysis and processing.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- Required Python libraries: `requests`, `PyPDF2`, `csv`, `os`, and `time`

## Installation
Clone the repository to your local machine:
git clone https://github.com/your-username/CongressionalRecords.git

Navigate to the cloned directory and install the required Python packages:
pip install requests PyPDF2

## Usage
1. **Set Up Directories**: Update the script with the paths to your target directories for saving PDFs and extracted text files.
2. **Run the Scraper**: Execute the web scraping script to collect URLs of congressional records.
3. **Download PDFs**: Use the downloader script to save the PDFs from the collected URLs.
4. **Convert PDFs to Text**: Run the PDF-to-text conversion script to transform the downloaded documents into text files.

## Contributing
Contributions to improve `CongressionalRecords` are welcome. Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- U.S. Government Publishing Office (GPO) for providing access to the congressional records.
- Contributors and maintainers of the `requests` and `PyPDF2` libraries.
