import requests
import time
from datetime import datetime, timedelta
import csv

# Replace 'YOUR_API_KEY' with your actual API key
api_key = "YOUR_UNIQUE_API_KEY"

# Define the base URL for the API
base_url = 'https://api.congress.gov/v3/congressional-record/'

# Calculate delay between requests to stay well below the rate limit
requests_per_hour = 1000
seconds_in_hour = 3600
# Let's use a delay that results in about 3 requests per minute, which is slower than the limit
delay_between_requests = seconds_in_hour / requests_per_hour * 20  # 20 seconds per request

# Function to fetch data with pagination
def fetch_data(date, start_record=0):
    formatted_date = date.strftime("%Y-%m-%d")
    results = []
    page_size = 250  # Max results per page
    current_offset = start_record

    while True:
        url = f"{base_url}?y={date.year}&m={date.month}&d={date.day}&api_key={api_key}&limit={page_size}&offset={current_offset}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            results.extend(data['Results']['Issues'])  # Add the results to the main list
            # Check if we've got the last page
            if len(data['Results']['Issues']) < page_size:
                break
            current_offset += page_size  # Increase the offset to get the next page of results
        elif response.status_code == 429:
            # Rate limit hit - wait for one minute and retry
            print(f"Rate limit hit for {formatted_date}. Waiting for one minute.")
            time.sleep(60)
        elif response.status_code == 500:
            # Internal Server Error - skip this date and continue with the next
            print(f"Internal Server Error for {formatted_date}. Skipping this date.")
            break
        else:
            print(f"Error fetching data for {formatted_date}: {response.status_code}")
            # Retry after one minute even if there's an error
            time.sleep(60)

        # Wait for 20 seconds before making the next request
        time.sleep(delay_between_requests)

    return results

# Function to save metadata to CSV
def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Congress', 'Id', 'Issue', 'PublishDate', 'Volume', 'PDF URL'])
        
        for issue in data:
            for link_type, link_info in issue['Links'].items():
                pdf_url = link_info['PDF'][0]['Url']  # Assuming you only want the first PDF
                writer.writerow([issue['Congress'], issue['Id'], issue['Issue'], issue['PublishDate'], issue['Volume'], pdf_url])

# Date range to fetch data for
end_date = datetime(1994, 12, 1) 
start_date = datetime(1993, 1, 1)  # Start from January 1, 1993

# Initialize a counter for tracking progress
total_dates = (end_date - start_date).days
processed_dates = 0

# Fetch and save data for each date
for single_date in (end_date - timedelta(n) for n in range((end_date - start_date).days)):
    date_str = single_date.strftime('%Y-%m-%d')
    data = fetch_data(single_date)
    if data:
        filename = f"congressional_record_{date_str}.csv"
        save_to_csv(data, filename)
        processed_dates += 1
        print(f"Data for {date_str} saved to {filename}")

        # Calculate progress percentage
        progress = (processed_dates / total_dates) * 100
        print(f"Progress: {progress:.2f}%")

        # Wait for 20 seconds before making the next request
        time.sleep(20)