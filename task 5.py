import requests
from bs4 import BeautifulSoup
import csv

def scrape_product_info(url):
    
    response = requests.get(url)
    
    
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return None
    
   
    soup = BeautifulSoup(response.content, 'html.parser')
    
   
    product_info = []
    products = soup.find_all('div', class_='product')
    for product in products:
        name = product.find('h2', class_='product-name').text.strip()
        price = product.find('span', class_='price').text.strip()
        rating = product.find('div', class_='rating').text.strip()
        product_info.append((name, price, rating))
    
    return product_info

def save_to_csv(product_info, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Price', 'Rating'])
        writer.writerows(product_info)

if __name__ == "__main__":
    
    url = "https://www.example.com"
    
    
    product_info = scrape_product_info(url)
    
    if product_info:
       
        save_to_csv(product_info, 'product_info.csv')
        print("Product information saved to product_info.csv")
    else:
        print("No product information scraped.")


