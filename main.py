from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\\Users\\benja\\Desktop\\reinforcement learning\\chrome driver\\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.linkedin.com")
title = driver.title

# username
username = driver.find_element(By.NAME, "session_key")
username.send_keys("benjaminmutie53@gmail.com")
username.send_keys(Keys.RETURN)

# password
password = driver.find_element(By.NAME, "session_password")
password.send_keys("MonkeyDluffy282")
password.send_keys(Keys.RETURN)

# search
search = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
search.send_keys("python coding")
search.send_keys(Keys.RETURN)

time.sleep(15)
if __name__ == '__main__':
    print("DONE")
