from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
# ...
driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the Selenium web driver
chrome_driver_path = 'your_chromedriver_path'  # Replace with the path to your ChromeDriver executable
driver = webdriver.Chrome(service=ChromeService(executable_path=chrome_driver_path))

# URL of the manga page you want to scrape
manga_url = 'https://manganato.com/manga-un971622'

# Navigate to the URL
driver.get(manga_url)

# Extract the information using Selenium
title = driver.find_element(By.XPATH, '//h1').text
alternative_title = driver.find_element(By.XPATH, '//td[contains(text(), "Alternative :")]/following-sibling::td/h2').text
authors = driver.find_element(By.XPATH, '//td[contains(text(), "Author(s) :")]/following-sibling::td').text
status = driver.find_element(By.XPATH, '//td[contains(text(), "Status :")]/following-sibling::td').text
genres = driver.find_element(By.XPATH, '//td[contains(text(), "Genres :")]/following-sibling::td').text

# Print the extracted data
print("Title:", title)
print("Alternative Title:", alternative_title)
print("Authors:", authors)
print("Status:", status)
print("Genres:", genres)

# Close the web driver
driver.quit()
