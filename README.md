# Web Scraping Project: RTL Theme Scraper

## Overview
This Python script is designed to scrape data from the RTL Theme website. It navigates through multiple pages, extracts detailed information about each theme, and saves the data in a JSON format.

## Features
- Scrape multiple pages of the RTL Theme website.
- Extract information like name, price, link, image URL, sales, and satisfaction data.
- Handle pagination and user-agent simulation to mimic a web browser.
- Error handling to manage issues during scraping.
- Saving the scraped data in a JSON file for easy use.

## How to Use
1. **Setting Up the Environment**
   - Ensure Python is installed on your machine.
   - Install the required packages: `requests` and `beautifulsoup4`.
   - Change URL Inside `python rtl_theme_scraper.py`.

2. **Running the Script**
   - Run the script using `python rtl_theme_scraper.py`.
   - Enter the number of pages you want to scrape when prompted.

3. **Output**
   - The scraped data is saved in `scraped_data.json` in the same directory as the script.

## Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`

## Limitations
- The script is specifically tailored for the RTL Theme website. It may not work on other websites without modifications.
- It respects the website’s TOS and ethical scraping guidelines.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Disclaimer
This script is for educational purposes only. Users are responsible for adhering to the RTL Theme's terms of service regarding scraping.
