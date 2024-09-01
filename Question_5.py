#Fetch multiple products from rokomari dot com from any category.

from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Set up the web driver
driver_path = os.path.join(os.getcwd(), 'chromedriver-win64')
exe_path = os.path.join(driver_path, 'chromedriver.exe')
driver = webdriver.Chrome()
driver.maximize_window()

# URL of the category page on Rokomari.com
base_url = 'https://www.rokomari.com/book/publisher/586/islamic-foundation'

def fetch_products_from_page(url):
    driver.get(url)
    time.sleep(5)  # Wait for the page to load
    
    # Find product elements on the page
    products = driver.find_elements(By.CSS_SELECTOR, 'div.book-text-area')
    
    # Extract product information
    product_data = []
    for product in products:
        name_elements = product.find_elements(By.CSS_SELECTOR, 'h4.book-title')
        author_elements = product.find_elements(By.CSS_SELECTOR, 'p.book-author')

        name = name_elements[0].text
        author = author_elements[0].text

        product_data.append({'Name': name, 'Author Name': author})

    return product_data

def get_next_page_url():
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, 'body > div.browse-page > div > div > div > section.browse__content > div.pagination > a:nth-child(10)')
        return next_button.get_attribute('href')
    except Exception:
        return None

# Initialize page URL and product list
page_url = base_url
all_products = []

# Loop through pages
while page_url:
    print(f"Fetching products from: {page_url}")
    products = fetch_products_from_page(page_url)
    all_products.extend(products)
    
    # Get the URL for the next page
    next_page_url = get_next_page_url()
    
    if next_page_url:
        page_url = next_page_url
        print("Moving to the next page...")
    else:
        page_url = None
        print("No more pages to fetch.")

# Create a DataFrame and save to CSV
df = pd.DataFrame(all_products)
df.to_csv('Book_list.csv', index=False)

print("Data saved to products.csv")

# Close the web driver
driver.quit()
