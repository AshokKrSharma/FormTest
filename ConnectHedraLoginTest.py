import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
driver.get("https://connect-test.hedera.online/start")
print("TEST 1")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "SIGN IN"))
    )
    driver.maximize_window()
    print("URL page loaded successfully.")
    element.click()
    print("TEST 2")
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "MuiButton-label"))
        )
        print("Login page loaded successfully.")
        driver.find_element(By.ID, 'username').send_keys("Email Here")
        driver.find_element(By.ID, 'password').send_keys("Password Here")
        element.click()
        print("TEST 3")
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "input"))
            )
            print("Login successful!")
        except:
            print("Login failed!")
    except:
        print("Could not load Login page")
except:
    print("Could not load URL")