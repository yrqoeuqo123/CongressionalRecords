import os
import requests

'''
Author's Note from Tianyi:
I would like to extend my heartfelt appreciation to the dedicated maintainers of the unitedstates/congress-legislators repository on GitHub. 
Their tireless efforts in curating and providing valuable data about current and historical Members of Congress, committees, 
social media accounts, district offices, and executive officials have been instrumental in my work. 
This repository's commitment to transparency and accessibility is a testament to the open-source community's spirit, 
making vital information easily accessible to researchers, educators, and anyone interested in understanding 
the workings of the United States Congress. I am truly grateful for their contributions, 
which have been invaluable in advancing my research and projects.
'''

# Define the URL of the GitHub repository
repository_url = 'https://github.com/unitedstates/congress-legislators'

# Define the target directory where you want to save the files
target_directory = 'REPLACE_WITH_YOUR_DIRECTORY'

# Create the target directory if it doesn't exist
os.makedirs(target_directory, exist_ok=True)

# List of data files to download
files_to_download = [
    ('legislators-current', 'YAML'),
    ('legislators-historical', 'YAML'),
    ('legislators-social-media', 'YAML'),
    ('committees-current', 'YAML'),
    ('committee-membership-current', 'YAML'),
    ('committees-historical', 'YAML'),
    ('legislators-district-offices', 'YAML'),
    ('executive', 'YAML'),
]

# Download each data file
for file_name, file_format in files_to_download:
    file_url = f'{repository_url}/raw/main/{file_name}.{file_format.lower()}'
    response = requests.get(file_url)

    if response.status_code == 200:
        file_path = os.path.join(target_directory, f'{file_name}.{file_format.lower()}')
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f'Downloaded: {file_name}.{file_format.lower()}')
    else:
        print(f'Failed to download: {file_name}.{file_format.lower()}')

# Credit and appreciation message
print('Downloaded all data files to the target directory.')
print('Credit and Appreciation to the unitedstates/congress-legislators repository for providing this data.')
