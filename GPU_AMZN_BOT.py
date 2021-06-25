from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome( PATH )

gpu_url = "https://www.amazon.com/dp/B08LW46GH2/ref=as_li_ss_tl?ie=UTF8&linkCode=ll1&tag=siusa-mp-20&linkId=f0e804d4c1423a4f552d9347e0e7628e&language=en_US"
c_out = "https://www.amazon.com/gp/cart/view.html?ref_=nav_cart"

driver.get( gpu_url )
check = False

driver.find_element_by_id( "nav-link-accountList" ).click()

email = driver.find_element_by_id( "ap_email" )
email.send_keys( "username" )
driver.find_element_by_id( "continue" ).click()

password = driver.find_element_by_id( "ap_password" )
password.send_keys( "password" )
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
