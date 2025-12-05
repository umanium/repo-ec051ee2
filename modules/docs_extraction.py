from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

import os 

'''
Download a document from an issuu URL to a specified destination.
This method uses selenium to download the document.

:param doc_url: an issuu URL of a document
:param destination_dir: the directory to download the document
:return: location of downloaded document
'''
def from_url(doc_url, destination_dir):
    initial_dest = os.listdir(destination_dir)

    # setting up browser
    chrome_options = Options()
    prefs = {'download.default_directory' : destination_dir}
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--headless=new')

    # open the browser
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(doc_url)

    doc_iframe = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, "DocPageReaderIframe"))
    )
    driver.get(doc_iframe.get_attribute('src'))

    download_button = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Download']"))
    )
    download_button.click()

    while (len(os.listdir(destination_dir)) <= len(initial_dest)) or any(f.endswith('.crdownload') for f in os.listdir(destination_dir)):
        sleep(1)
    
    driver.close()

    return os.path.join(destination_dir, [f for f in os.listdir(destination_dir) if f not in initial_dest][0])
