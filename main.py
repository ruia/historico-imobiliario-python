import csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

house_listings = []

def main():
    print("Realstate Scraper starting... ")

    print("Reading input listings input file...")
    house_listings = read_data_from_input_file()
    print(f"Found {len(house_listings)} entries")

    print("Starting driver... ")
    driver = start_webdriver()

    print("\nGetting listing data... ")
    driver.get(house_listings[0])
    driver.implicitly_wait(2)
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    listing_name = driver.find_element(By.XPATH, '//header/h1').text
    listing_price = driver.find_element(By.XPATH, '//header/strong').text.replace(' ','').strip('€')
    print(listing_name)
    print(listing_price)
    # for listing in house_listings:
    #     driver.get(listing)
    #     driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()


def read_data_from_input_file():
    with open('data/data_input.csv') as f:
        contents = []
        reader = csv.reader(f)
        for row in reader:
            contents.append(row[0]) #TODO: remove the list index later. only used for single column input file
   
    return contents

def start_webdriver():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    return driver
    

if __name__ == "__main__":
   main()