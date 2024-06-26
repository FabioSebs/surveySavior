from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
import json
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

class WebScraper:
    def __init__(self, url, fname) -> None:
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("start-maximized")

        self.fname = fname
        self.url = url
        self.driver = webdriver.Chrome(options=options)
        self.entries = []

    def navigate_to_url(self):
        self.driver.get(self.url)

    # NOTE: override this
    def perform_scraping(self):
        pass

    def write_json(self):
        with open(self.fname, "w") as json_file:
            json.dump(self.entries, json_file, indent=2)

    def append_entry(self, new_entry):
        self.entries.append(new_entry)
        self.write_json()


    def close_driver(self):
        if self.driver:
            self.driver.quit()

    def run(self):
        try:
            self.navigate_to_url()
            self.perform_scraping()
            self.write_json()
        finally:
            self.close_driver()

def __init__():
    chromedriver_autoinstaller.install()