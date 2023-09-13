import requests
from bs4 import BeautifulSoup

# Replace this URL with the LinkedIn profile URL you want to scrape
linkedin_url = 'https://www.linkedin.com/search/results/people/?currentCompany=%5B86811619%5D&origin=COMPANY_PAGE_CANNED_SEARCH&sid=t-U'

# Send an HTTP GET request to the LinkedIn profile URL
response = requests.get(linkedin_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the name and headline
    name = soup.find('h1', {'class': 'text-heading-xlarge inline t-24 v-align-middle break-words'})
    headline = soup.find('p', {'class': 'mt1 t-18 t-black t-normal break-words'})
    
    if name and headline:
        print(f"Name: {name.text.strip()}")
        print(f"Heading: {headline.text.strip()}")
    else:
        print("Name or headline not found on the profile.")
else:
    print("Failed to retrieve the LinkedIn profile.")
