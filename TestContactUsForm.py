import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import datetime
csv_file = 'E:/FormLog.csv' #csv file address
expected_message = "Thanks for contacting us! We will get in touch with you shortly."
driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
driver.get("https://www.vikramsolar.com/")
driver.maximize_window()
start_time = datetime.datetime.now()
driver.find_element(By.CLASS_NAME,'elementor-button-content-wrapper').click()
time_to_load = datetime.datetime.now()-start_time
form_url = driver.current_url
form_title = driver.title
driver.find_element(By.ID,'input_2_1_3').send_keys('My First Name')
driver.find_element(By.ID,'input_2_1_4').send_keys('My Middle Name')
driver.find_element(By.ID,'input_2_1_6').send_keys('My Last Name')
Select(driver.find_element(By.ID,'input_2_3')).select_by_index(3)
driver.find_element(By.ID,'input_2_19').send_keys('My Company Name')
driver.find_element(By.ID,'input_2_6').send_keys('myemail@gmail.com')
driver.find_element(By.ID,'input_2_7').send_keys('+919876543210')
driver.find_element(By.ID,'input_2_9').send_keys('+919876543210')
driver.find_element(By.ID,'input_2_10').send_keys('mywebsite.com')
Select(driver.find_element(By.ID,'input_2_11')).select_by_index(4)
Select(driver.find_element(By.ID,'input_2_13')).select_by_index(2)
driver.find_element(By.ID,'input_2_12').send_keys('My description')
driver.find_element(By.ID,'gform_submit_button_2').click()
time.sleep(5)
submit_message = driver.find_element(By.ID,'gform_confirmation_message_2').get_attribute('innerHTML').strip()
#print('submit message: '+submit_message)
result = ''
if(expected_message == submit_message):
    result = 'Submit Successful'
else:
    result = 'Submit Failed'
csv_entry = [str(start_time),form_url,time_to_load,form_title,result]
f = open(csv_file,'w', encoding='UTF8', newline='')
writer = csv.writer(f)
writer.writerow(csv_entry)
f.close()
