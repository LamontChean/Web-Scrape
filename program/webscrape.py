# Real-Life example of Parallelism
# WEB SCRAPING
# simulate a web scraping task where we scrape multiple pages parallely
# web scraping tasks often be slow due to network latency

# Problem 
# scrape data from multiple websites
# each url will return a HTML response

# Objective
# to scrape quotes from "http://quotes.toscrape.com"
# a website specifically for scraping practice

# Dependencies
# pip install requests beautifulsoup4
import requests
import concurrent.futures
from bs4 import BeautifulSoup

def scrape(page):
    url = f"http://quotes.toscrape.com/page/{page}"
    
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to visit website")
        return 

    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('div', class_='quote')

    try:
        with open("data.txt", "a") as file:
            for quote in quotes:
                text = quote.find('span', class_='text').text
                author = quote.find('small', class_='author').text

                file.writelines(f"{text};{author}\n")
    except FileNotFoundError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(scrape, i): i for i in range(1,6)}

        for future in concurrent.futures.as_completed(futures):
            try:
                print(f"Page {futures[future]} scrapped")
            except Exception as e:
                print(f"{e}")
        
