import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code!= 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None
    
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the title of the webpage
    title = soup.title.string if soup.title else 'No title found'
    
    return title

# Specify the URL you want to scrape
url = 'https://example.com'
title = scrape_website(url)

if title:
    print(f'Title of the webpage: {title}')

