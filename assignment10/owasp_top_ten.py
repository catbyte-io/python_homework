import csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Task 6: Scraping Structured Data
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get('https://owasp.org/www-project-top-ten/')

    top_ten = []

    page_body = driver.find_element(By.ID, "sec-main")

    if page_body:
        link_elements = page_body.find_elements(By.CSS_SELECTOR, 'a')

        for link in link_elements[1:]:
            vulnerability = {}
            vulnerability['title'] = link.text
            vulnerability['link'] = link.get_attribute('href')
            top_ten.append(vulnerability)

        print(top_ten)
    
    with open('owasp_top_ten.csv', 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['title', 'link'])
        for row in top_ten:
            csv_writer.writerow([row['title'], row['link']])

except Exception as e:
    print("Could not find website.")
    print(f"Exception: {type(e).__name__} {e}")
finally:
    driver.quit()

