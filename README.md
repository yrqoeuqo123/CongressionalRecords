# CongressionalRecords

## Overview
`CongressionalRecords` is a collection of Python scripts for extracting and converting U.S. Congressional records from the  [Congress.gov API](https://api.congress.gov/) into text format. Covering the period from 1995-01-04 to 2023-11-09, from the 104th to the 118th Congress, this repository provides the tools needed to scrape URLs, download PDF files, and transform these PDFs into readable text files using PyPDF2. In addition, it includes a library of URLs, PDFs, text files, and CSVs, offering a comprehensive resource for analyzing congressional documents.

## Dataset Introduction and Accessing the Data

To effectively use the CongressionalRecords scripts or access data from the Congress.gov API, it's essential to acquire a unique API key from [Congress.gov](https://www.congress.gov/). This key will allow you to authenticate your requests and access the wealth of congressional data provided by the API.

### Source: Congress.gov
[Congress.gov](https://www.congress.gov/) is an essential source of legislative information, ideal for investigating specific legislation and exploring legislative history. Congress.gov also contains vast amounts of data. Over the years, users have "scraped" the website, and the Government Publishing Office (GPO) has offered bulk data downloads for some collections. The introduction of the beta [Congress.gov API](https://api.congress.gov/) marks a significant advancement, providing structured and accurate congressional data. This API is a RESTful API, offering responses in XML or JSON, and covers a broad range of collections including bills, amendments, summaries, Congress members, the Congressional Record, committee reports, nominations, treaties, and House Communications.

### Obtaining an API Key

1. **Visit Congress.gov API**: Navigate to  [Congress.gov API](https://api.congress.gov/).
2. **Register for an API Key**: Follow the instructions on the website to sign up for an API key. This usually involves creating an account and agreeing to certain terms of use.
3. **Keep Your Key Secure**: Once you receive your API key, keep it secure. Avoid sharing it publicly or uploading it to public repositories.

### Configuring the Scripts

The provided scripts in this repository are designed to be plug-and-play, with minimal setup required:

1. **Local Directory Setup**: Ensure that your local directory paths in the scripts are correctly set up to where you want to download and store the PDFs and text files.
2. **Insert Your API Key**: Locate the section in the script where the API key is required and insert your unique key. This will usually be clearly marked in the code.
   
   Example:
   ```python
   # Insert your API key here
   api_key = "YOUR_UNIQUE_API_KEY"

3. **Run the Scripts**: With your API key in place and directories set up, you should be able to run the scripts.

### Using the Scripts

After configuring the scripts with your API key, you're all set to start:

- **Scraping data**: The scripts will fetch URLs from Congress.gov using your API key.
- **Downloading and converting data**: The scripts will download PDFs and convert them into text format for further analysis.
  
Remember, the API key is essential for accessing the Congress.gov data, so make sure it is correctly implemented in the scripts.

## Features
- **Web Scraping**: Scripts to automatically scrape URLs of congressional records.
- **PDF Downloading**: Scripts to download PDFs from the scraped URLs.
- **PDF to Text Conversion**: Scripts to convert the downloaded PDF documents into text files.
- **Resource Library**: A collection of URLs, PDFs, text files, and CSVs from 1995-01-04 to 2023-11-09.
- **Text Mining Techniques**: Insights into general text mining techniques, with a focus on specific topics like climate change.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- Required Python libraries: `requests`, `PyPDF2`, `csv`, `os`, and `time`

## Installation
Clone the repository to your local machine:
`git clone https://github.com/your-username/CongressionalRecords.git`

Navigate to the cloned directory and install the required Python packages:
`pip install requests PyPDF2`

## Usage
1. **Explore the Dataset**: Look through the provided URLs, PDFs, text files, and CSVs spanning from 1995-01-04 to 2023-11-09.
2. **Utilize the Scripts**: Employ the scripts to scrape, download, and convert new data.
3. **Apply Text Mining Techniques**: Implement text mining methods on the data for extracting insights, particularly focusing on areas like climate change.

## Text Mining Techniques Overview
- **Keyword Extraction**: Identify key terms within the congressional records.
- **Topic Modeling**: Employ LDA to uncover underlying topics in large text volumes.
- **Sentiment Analysis**: Analyze textual sentiment to understand positions on various issues.

## Congressional Document Types
The dataset encompasses a variety of congressional document types:
- Daily Digest
- House of Representatives Records
- Extensions of Remarks
- Senate Records

Each type provides insights into the U.S. Congress, valuable for research and policy analysis.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- U.S. Government Publishing Office (GPO) for the congressional records access.
- `requests` and `PyPDF2` library maintainers and contributors.
