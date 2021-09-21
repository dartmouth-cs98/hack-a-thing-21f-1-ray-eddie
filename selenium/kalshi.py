#From tutorial https://selenium-python.readthedocs.io/
#Needs selenium package as well as compatible chrome driver in PATH to work

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_options = Options()
#Headless option from following stackoverflow
#https://stackoverflow.com/questions/53657215/running-selenium-with-headless-chrome-webdriver
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://www.kalshi.com")

# element = driver.find_element_by_partial_link_text('Log')
#element.click()

element = driver.find_element_by_xpath("//button[text()='Log in']")
element.click()


wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[3]/div[3]/div[1]/div[2]/div[2]/form/input[1]')))
element.send_keys('Fake@Gmail.com')
driver.find_element_by_xpath('//*[@id="root"]/div[3]/div[3]/div[1]/div[2]/div[2]/form/input[2]').send_keys('12345')
element.submit()

time.sleep(10)

driver.close()

