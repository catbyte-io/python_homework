import pandas as pd
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


### Task 3: Write a Program to Extract this Data ###
# Initialize driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Get the Durham library website
try:
    driver.get('https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart')

    # Find all the li elements in that page for the search list results.
    list_items = driver.find_elements(By.CSS_SELECTOR, 'li.cp-search-result-item')

    # Within your program, create an empty list called results.
    results = []
    
    # Iterate through entries. Create a dict that stores these values, with the keys being Title, Author, and Format-Year.  Then append that dict to your results list.
    for item in list_items:
        values = {}
        values['Title'] = item.find_element(By.CLASS_NAME, 'title-content').text
        authors = item.find_elements(By.CLASS_NAME, 'author-link')
        if (authors):
            author_list = [author.text for author in authors]
            author_names = ';'.join(author_list)
            values['Author'] = author_names
        format_info = item.find_element(By.CLASS_NAME, 'cp-format-info')
        if (format_info):
            format_year = format_info.find_element(By.CLASS_NAME,'cp-screen-reader-message')
            values['Format-Year'] = format_year.text

        results.append(values)

    # Create DataFrame from results
    df_results = pd.DataFrame(results)
    print(df_results)

    # Task 4: Write out the Data
    # Write the DataFrame to a csv file
    df_results.to_csv('get_books.csv')

    # Write the results list out to a file called get_books.json,
    with open('get_books.json', 'w') as file:
        json.dump(results, file)

except Exception as e:
    print("Could not find website.")
    print(f"Exception: {type(e).__name__} {e}")
finally:
    driver.quit()
