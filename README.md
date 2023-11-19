# CongressionalRecords

## Overview
`CongressionalRecords` is a collection of Python scripts for extracting and converting U.S. Congressional records from the GPO website into text format. Covering the period from 1995-01-04 to 2023-11-09, from the 104th to the 118th Congress, this repository provides the tools needed to scrape URLs, download PDF files, and transform these PDFs into readable text files using PyPDF2. In addition, it includes a library of URLs, PDFs, text files, and CSVs, offering a comprehensive resource for analyzing congressional documents.

## Dataset Introduction

### Source: Congress.gov
[Congress.gov](https://www.congress.gov/) is an essential source of legislative information, ideal for investigating specific legislation and exploring legislative history. Congress.gov also contains vast amounts of data. Over the years, users have "scraped" the website, and the Government Publishing Office (GPO) has offered bulk data downloads for some collections. The introduction of the beta Congress.gov API marks a significant advancement, providing structured and accurate congressional data. This API is a RESTful API, offering responses in XML or JSON, and covers a broad range of collections including bills, amendments, summaries, Congress members, the Congressional Record, committee reports, nominations, treaties, and House Communications.

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
