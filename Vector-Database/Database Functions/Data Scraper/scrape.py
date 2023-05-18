from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import json

DRIVER_PATH = 'C:\Py Projects\Fashion App\Vector Database\Database Functions\Data Scraper\chromedriver.exe'
driver = webdriver.Chrome(DRIVER_PATH)
urls =[]
processed_urls = []

def scrape_palettes(url):
    driver.get(url)
    
    time.sleep(2)

    # Press Ctrl+1
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('1').key_up(Keys.CONTROL).perform()
    # Wait for the page to load
    time.sleep(1)

    for i in range(1667):

        # Press Space
        action = ActionChains(driver)
        action.send_keys(Keys.SPACE).perform()

        # Wait for any changes to take effect
        time.sleep(0.1)

        # Append the current URL
        urls.append(driver.current_url)

def format_urls(urls):  
    for url in urls:
        # Remove the "https://coolors.co/" part
        stripped_url = url.replace("https://coolors.co/", "")
        
        # Split the remaining string by "-"
        split_url = stripped_url.split("-")
        
        processed_urls.append(split_url)
    


scrape_palettes('https://coolors.co/fef9f3-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/fef5eb-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/fdf1e3-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/fdeddc-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/fcead4-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/fce6cc-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/fce2c4-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/fbdebc-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/fbdab5-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/fad6ad-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/fad3a5-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/facf9d-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/f9cb96-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/f9c78e-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/f8c386-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/f8c07e-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/f8bc77-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/f7b86f-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/f7b467-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/f6b05f-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/f6ac58-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/f6a950-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/f5a548-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/f5a140-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/f49d38-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/f49931-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/f49629-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/f39221-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/f38e19-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/f28a12-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/f0860c-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/e8820b-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/e17d0b-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/d9790b-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/d1750a-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/c9700a-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/c26c09-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/ba6809-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/b26309-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/aa5f08-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/a35b08-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/9b5607-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/935207-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/8b4e07-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/844906-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/7c4506-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/744105-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/6c3c05-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/643805-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/5d3404-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/552f04-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/4d2b03-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/452703-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/3e2203-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/361e02-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/2e1a02-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/261501-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/1f1101-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/170d01-c6caed-ada8be-4a5240-000000')
scrape_palettes('https://coolors.co/0f0800-c6caed-ada8be-4a5240-000000')
format_urls(urls)

with open("C:\Py Projects\Fashion App\Vector Database\database\matrix\palette_data.json", "w") as outfile:
        json.dump(processed_urls, outfile)
# Close the WebDriver
driver.quit()
