import self as self
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()

mam = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()
edl = driver.find_element_by_css_selector("#username").send_keys("reinguard@mail.ru")
pdl = driver.find_element_by_css_selector("#password").send_keys("jokker100500_")
log = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]")
log.click()






