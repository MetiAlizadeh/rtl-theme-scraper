import requests
from bs4 import BeautifulSoup
import json
import time

# Function to scrape data from a single page
def scrape_page(url):
    try:
        # Set user-agent in headers to simulate a web browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)

        # Check if the response is successful (status code 200)
        if response.status_code != 200:
            print(f"Failed to retrieve page: {url}")
            return []

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all items on the page with a specific class
        items = soup.find_all('div', class_='col-lg-4 col-md-6')
        
        page_data = []

        # Loop through each item and extract data
        for item in items:
            data = extract_item_data(item, url)
            if data:
                page_data.append(data)

        return page_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Function to extract data from a single HTML item
def extract_item_data(item, page_url):
    try:
        # Extract price information
        price_element = item.find('ins', class_="sale")
        price = price_element.text.strip() if price_element else 'N/A'

        # Extract link information
        link_element = item.find('a')
        link = link_element.get('href') if link_element else 'N/A'

        # Extract name information
        name_element = item.find('span', class_="title")
        name = name_element.text.strip() if name_element else 'N/A'

        # Extract image information
        image_element = item.find('img')
        image = image_element.get('data-src') if image_element else 'N/A'

        # Extract sales information
        sales_element = item.find('a')
        sales = json.loads(sales_element.get('data-ga')).get('item_category3') if sales_element else 'N/A'

        # Extract satisfaction information
        satisfaction_element = item.find('a')
        satisfaction = json.loads(satisfaction_element.get('data-ga')).get('item_category4') if satisfaction_element else 'N/A'

        return {
            'name': name,
            'price': price,
            'link': link,
            'image': image,
            'sales': sales,
            'satisfaction': satisfaction,
            'page': page_url,
        }
    except Exception as e:
        print(f"Error processing item: {e}")
        return None

# Main function
def main():
    howManyPages = int(input('Enter How Many Pages You Want To Scrape: '))
    pageNumber = 1

    scraped_data = []

    # Try to read existing data from a JSON file
    try:
        with open('scraped_data.json', 'r', encoding='utf-8') as json_file:
            scraped_data = json.load(json_file)
    except FileNotFoundError:
        pass

    while pageNumber <= howManyPages:
        url = f'https://www.rtl-theme.com/category/wp-themes/?order=DESC&orderBy=updateDate&style=grid&paged={pageNumber}'
        page_data = scrape_page(url)
        scraped_data.extend(page_data)
        print(f"Page {pageNumber} done")
        pageNumber += 1
        time.sleep(2)  # Sleep for 2 seconds between requests to avoid overloading the server

    # Save the scraped data to a JSON file
    with open('scraped_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(scraped_data, json_file, ensure_ascii=False, indent=4)

    print("Scraped data saved to 'scraped_data.json'")

if __name__ == "__main__":
    main()
