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
book = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[4]/a[2]")
book.click()
quantity = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a/span[1]")
quantity_get_text = quantity.text
assert quantity_get_text == "1 Item"
price = driver.find_element_by_css_selector("#wpmenucartli > a > span.amount")
price_get_text = price.text
assert price_get_text == "₹180.00"
basket = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a/i")
basket.click()
time.sleep(5)
subtotal = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > div > div > table > tbody > tr.cart-subtotal > td > span")
subtotal_get_text = subtotal.text
assert subtotal_get_text == "₹180.00"
time.sleep(5)
total = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > div > div > table > tbody > tr.order-total > td > strong > span")
total_get_text = total.text
assert total_get_text == "₹189.00"

