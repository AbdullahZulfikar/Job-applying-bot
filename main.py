from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location"
           "=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
try:
    driver.find_element(By.XPATH, '//*[@id="ember16"]')


except:
    button = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
    button.send_keys(Keys.ENTER)

    session = driver.find_element(By.NAME, "session_key")
    session.send_keys("abdullahzulfiqar123apple@gmail.com")

    password = driver.find_element(By.NAME, "session_password")
    password.send_keys("abdullahai")

    button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    button.send_keys(Keys.ENTER)

    apply_button = driver.find_element(By.CSS_SELECTOR,".jobs-s-apply button")
    apply_button.send_keys(Keys.ENTER)

    next_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button_text")
    next_button.click()
time.sleep(1000)

driver.quit()
