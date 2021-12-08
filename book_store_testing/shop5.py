from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
driver.implicitly_wait(10)

shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()
driver.execute_script("window.scrollTo(0,300);")
first_book = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[4]/a[2]")
first_book.click()
time.sleep(5)
second_book = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[5]/a[2]")
second_book.click()
basket = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a/span[1]")
basket.click()
time.sleep(5)
delete = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-remove > a")
delete.click()
time.sleep(5)
undo = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > div.woocommerce-message > a")
undo.click()
quantity = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input")
quantity.clear()
three = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input")
three.send_keys("3")
update = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(3) > td > input.button")
update.click()
quantity = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr.cart_item > td.product-quantity > div > input")
quantity_get_text = quantity.text
assert quantity_get_text == "3"
time.sleep(5)
apply = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(2) > td > div > input.button")
apply.click()
time.sleep(5)
coupon = driver.find_element_by_css_selector("#coupon_code")
coupon_get_text = coupon.text
assert coupon_get_text == "Coupon code"

