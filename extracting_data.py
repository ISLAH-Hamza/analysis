from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Set Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Comment this line to display the browser window
webdriver_path = './chromedriver.exe'
# Create a new Chrome driver with the configured options
driver = webdriver.Chrome(executable_path=webdriver_path)   #options=chrome_options
driver.get('https://applications-web.hcp.ma/InventaireCommunal/')

region = Select(driver.find_element(By.CSS_SELECTOR, 'select#ddlReg'))
indexes = len(region.options)
 
for i in range(indexes):
    region_select = Select(driver.find_element(By.CSS_SELECTOR, 'select#ddlReg'))
    options = region_select.options
    region_select.select_by_value(options[i].get_attribute("value"))
    time.sleep(2)

    province = Select(driver.find_element(By.CSS_SELECTOR, 'select#ddlPro'))
    for j in range(len(province.options)) :
        province_select = Select(driver.find_element(By.CSS_SELECTOR, 'select#ddlPro'))
        province_options = province_select.options
        province_select.select_by_value(province_options[j].get_attribute("value"))
    
        time.sleep(2)
input()