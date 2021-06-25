from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome( PATH )
url = "https://www.walmart.com/account/login?tid=0&returnUrl=%2Fip%2FSony-PlayStation-5-Video-Game-Console%2F363472942"
test_url = "https://www.walmart.com/account/login?tid=0&returnUrl=%2Fip%2FOzark-Trail-50-Degree-Warm-Weather-Adult-Sleeping-Bag-Red%2F250528859"

driver.get( test_url )
check = False

driver.find_element_by_id( "email" ).send_keys( "colepjohnston1@gmail.com" )
driver.find_element_by_id( "password" ).send_keys( "Colemacey1" )
driver.find_element_by_css_selector( ".text-inherit" ).click()

while check is False:
    try:
        atocart = WebDriverWait( driver, 3 ).until(
            EC.element_to_be_clickable( ( By.CSS_SELECTOR, '//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button/span/span' ) )
        )
        check = True
    except:
        driver.refresh()

atocart.click()