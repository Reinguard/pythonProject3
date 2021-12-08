from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
driver.implicitly_wait(10)

mam = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()
edl = driver.find_element_by_css_selector("#username").send_keys("reinguard@mail.ru")
pdl = driver.find_element_by_css_selector("#password").send_keys("jokker100500_")
log = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]")
log.click()
shop = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a").click()
close_btn_text = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#content > form > select"), "Default sorting"))
sort_by_price = driver.find_element_by_class_name("orderby").click()
time.sleep(5)
high_to_low = driver.find_element_by_css_selector("#content > form > select").click()
price_element = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#content > form > select"), "Sort by price: high to low"))

