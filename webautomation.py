from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Replace the path with the path to your chromedriver executable
PATH ="C:\\Users\\DELL\\Desktop\\chromedriver-win64\\"

# Initialize the Chrome driver
service = Service(PATH)
driver = webdriver.Chrome()

# Open a website
driver.get("https://google.com")

# Interact with elements on the page
search_bar = driver.find_element(By.NAME,"q")
#search_bar = driver.find_element(By.CLASS_NAME,"gLFyf")
search_bar.clear()
search_bar.send_keys("python library")
search_bar.send_keys(Keys.RETURN)

# Capture and print the current URL
print("Current URL:", driver.current_url)

# Close the browser
driver.quit()
