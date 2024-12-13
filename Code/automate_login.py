from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up the browser driver
chrome_options = Options()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Path to Chrome executable
service = Service(r"E:\Selenium\chromedriver-win64\chromedriver.exe")  # Path to ChromeDriver

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Navigate to the login page
    driver.get("https://www.saucedemo.com/v1/")
    time.sleep(2)  # Wait for the page to load

    # Step 2: Automate Login
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    password_field.send_keys(Keys.RETURN)
    time.sleep(2)  # Wait for login to complete

    # Step 3: Navigate and Extract Data
    driver.get("https://www.saucedemo.com/v1/inventory.html")
    time.sleep(2)  # Wait for the page to load

    # Extract product names (or rows, if in a table format)
    rows = driver.find_elements(By.CLASS_NAME, "inventory_item")  # Adjusted to find each product item

    # Print each row's text with a space after each row
    for row in rows:
        print(row.text)
        print()  # Add an empty line for better readability

finally:
    # Step 4: Close the Browser
    driver.quit()
