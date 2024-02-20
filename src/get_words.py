import requests
from bs4 import BeautifulSoup
import re
import csv

def scrape_site_for_5_letter_words(url):
    # Send a request to the website

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract text from the parsed content
        text = soup.get_text()
        
        # Find all 5-letter words using regex
        words = re.findall(r'\b\w{5}\b', text)
        
        # Remove duplicates and return the list
        return list(set(words))
    else:
        print("Failed to retrieve the webpage")
        response = requests.get(url)
        print("Status Code:", response.status_code)
        return []

def save_words_to_csv(words, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for word in words:
            writer.writerow([word])

# # Example usage
# urls = ['https://raw.githubusercontent.com/tabatkins/wordle-list/main/words'] # Replace with your target URL

# five_letter_words = []

# for url in urls:
#     five_letter_words += scrape_site_for_5_letter_words(url)

# save_words_to_csv(set(five_letter_words), 'all_fiveletterwords.csv')
