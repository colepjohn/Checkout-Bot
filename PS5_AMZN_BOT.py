from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome( PATH )
xbox_url = "https://www.amazon.com/EVGA-PowerLink-Support-Founders-600-PL-2816-LR/dp/B01MQ1YEYH/ref=sr_1_9?dchild=1&keywords=geforce+rtx+3080+founders+edition&qid=1620347107&sr=8-9"
ps5_url = "https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG/ref=sr_1_13?dchild=1&keywords=playstation+5&qid=1620357876&sr=8-13"
c_out = "https://www.amazon.com/gp/cart/view.html?ref_=nav_cart"

driver.get( ps5_url )
check = False

driver.find_element_by_id( "nav-link-accountList" ).click()

email = driver.find_element_by_id( "ap_email" )
email.send_keys( "colepjohnston1@gmail.com" )
driver.find_element_by_id( "continue" ).click()

password = driver.find_element_by_id( "ap_password" )
password.send_keys( "Patricklynne1" )
driver.find_element_by_id( "signInSubmit" ).click()

time.sleep(10)

while check is False:
    try:
        atocart = WebDriverWait( driver, 4 ).until(
            EC.element_to_be_clickable( ( By.ID, "buy-now-button" ) )
        )
        check = True
    except:
        driver.refresh()

atocart.click()

try:
    cout = WebDriverWait( driver, 10 ).until(
        EC.element_to_be_clickable( ( By.ID, "hlb-ptc-btn" ) )
    )
except:
    driver.refresh()

cout.click()

try:
    buy = WebDriverWait( driver, 10 ).until(
        EC.element_to_be_clickable( ( By.CSS_SELECTOR, ".a-button-input" ) )
    )
except:
    driver.refresh()

buy.click()