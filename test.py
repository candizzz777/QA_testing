from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

driver = webdriver.Chrome()

driver.get('https://www.google.com.ua/')
input_google = driver.find_element(By.XPATH, "")
input_google.send_keys("Iphone")
input_google.send_keys(Keys.RETURN)
assert "Iphone - Поиск в Google" in driver.title
driver.quit()