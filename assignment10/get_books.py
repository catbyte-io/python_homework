import pandas as pd
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


### Task 3: Write a Program to Extract this Data ###
# Initialize driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Get the library website
driver.get('https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart')
