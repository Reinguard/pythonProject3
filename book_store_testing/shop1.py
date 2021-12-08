from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
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
html = driver.find_element_by_css_selector("#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19 > a")
html.click()
count_elements = len(driver.find_elements_by_tag_name("h3"))


