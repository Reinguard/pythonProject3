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
basket = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a/span[1]")
basket.click()
time.sleep(5)
proceed = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > div > div > div > a")
proceed.click()
time.sleep(5)
first_name = driver.find_element_by_css_selector("#billing_first_name").send_keys("Ivan")
last_name = driver.find_element_by_css_selector("#billing_last_name").send_keys("Ivanov")
email = driver.find_element_by_css_selector("#billing_email").send_keys("reinguard@mail.ru")
phone = driver.find_element_by_css_selector("#billing_phone").send_keys("89160000000")
driver.execute_script("window.scrollTo(0,600);")
address = driver.find_element_by_css_selector("#billing_address_1").send_keys("Letchika Ulianina")
apartment = driver.find_element_by_css_selector("#billing_address_2").send_keys("3")
town = driver.find_element_by_css_selector("#billing_city").send_keys("Voronezh")
state = driver.find_element_by_css_selector("#billing_state").send_keys("Sortirovka")
postcode = driver.find_element_by_css_selector("#billing_postcode").send_keys("690382")
driver.execute_script("window.scrollTo(0,600);")
time.sleep(5)
check = driver.find_element_by_css_selector("#payment_method_cheque").click()
order = driver.find_element_by_css_selector("#place_order").click()
time.sleep(5)
some_element = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-35 > div > div.woocommerce > p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
some_element = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-35 > div > div.woocommerce > table > tfoot > tr:nth-child(3) > th"), "Check Payments"))

