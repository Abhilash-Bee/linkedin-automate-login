from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "L:\Development\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("https://www.linkedin.com/")

username = driver.find_element(By.NAME, "session_key")
username.send_keys("Linkedin_Username")

password = driver.find_element(By.NAME, "session_password")
password.send_keys("Linkedin_Password")

login = driver.find_element(By.CSS_SELECTOR, ".sign-in-form__submit-button")
login.click()

jobs = driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a/div/div')
jobs.click()

# job_search = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
# job_search.send_keys("Python Developer")
# job_search.send_keys(Keys.ENTER)
#
# job_location = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
# job_location.send_keys("Bengaluru, Karnataka, India")
# job_location.send_keys(Keys.ENTER)
