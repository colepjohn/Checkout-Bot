# Checkout bot to quickly buy GPUs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome( PATH )
test_url = "https://www.bestbuy.com/site/insignia-2-1-channel-80w-soundbar-system-with-wireless-subwoofer-black/6335126.p?skuId=6335126"
gpu_url = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"
c_out_url = "https://www.bestbuy.com/cart"

driver.get( gpu_url )
check = False

while check is False:
    try:
        atcBtn = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable( ( By.CSS_SELECTOR, ".add-to-cart-button" ) )
        )
        check = True
    except:
        driver.refresh()


atcBtn.click()

driver.get( c_out_url )

try:
    coutBtn = WebDriverWait( driver, 10 ).until(
        EC.element_to_be_clickable( ( By.CSS_SELECTOR, ".btn-primary" ) )
    ) 
    coutBtn.click()
except:
    driver.refresh()

time.sleep(2)

email = driver.find_element_by_name( "fld-e" )
email.send_keys( "colepjohnston1@gmail.com" )
password = driver.find_element_by_name( "fld-p1" )
password.send_keys( "Calilynne99" )
password.send_keys( Keys.RETURN )

time.sleep(2)

try:
    payBtn = WebDriverWait( driver, 10 ).until(
        EC.element_to_be_clickable( ( By.CSS_SELECTOR, ".btn-secondary" ) )
    ) 
    payBtn.click()
    time.sleep(3)
except:
    driver.refresh()

try:
    cvv = WebDriverWait( driver, 10 ).until(
        EC.presence_of_element_located( ( By.ID, "credit-card-cvv" ) )
    )
    cvv.send_keys( "123" )
    Fname = WebDriverWait( driver, 10 ).until(
        EC.presence_of_element_located( ( By.ID, "payment.billingAddress.firstName" ) )
    )
    Fname.send_keys( "Cole" )
    Lname = WebDriverWait( driver, 10 ).until(
        EC.presence_of_element_located( ( By.ID, "payment.billingAddress.lastName" ) )
    )
    Lname.send_keys( "Johnston" )
    Address = WebDriverWait( driver, 10 ).until(
        EC.presence_of_element_located( ( By.ID, "payment.billingAddress.street" ) )
    )
    Address.send_keys( "1730 Woods Lane, Denver NC" )
    Address.send_keys( Keys.ARROW_DOWN )
    Address.send_keys( Keys.RETURN )
    time.sleep(1)
    driver.find_element_by_class_name( "btn-lg" ).click()
    time.sleep(300)
except:
    driver.refresh()