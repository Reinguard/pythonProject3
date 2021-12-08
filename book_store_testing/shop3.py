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
book = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[1]/a[1]/h3").click()
element = driver.find_element_by_css_selector("#product-169 > div.summary.entry-summary > div:nth-child(2) > p > del > span")
element_get_text = element.text
assert element_get_text == "₹600.00"
new = driver.find_element_by_css_selector("#product-169 > div.summary.entry-summary > div:nth-child(2) > p > ins > span")
new_get_text = new.text
assert new_get_text == "₹450.00"
time.sleep(5)
cover = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[1]/a/img")
cover.click()
time.sleep(5)
x = driver.find_element_by_css_selector("body > div.pp_pic_holder.pp_woocommerce > div.pp_content_container > div > div > div > div.pp_fade > div.pp_details > a")
x.click()



