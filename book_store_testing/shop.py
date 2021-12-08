from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()

mam = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()
edl = driver.find_element_by_css_selector("#username").send_keys("reinguard@mail.ru")
pdl = driver.find_element_by_css_selector("#password").send_keys("jokker100500_")
log = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]")
log.click()
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.clik()
book = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[3]/a[1]/h3")
book.click()
element = driver.find_element_by_css_selector("#product-181 > div.summary.entry-summary > h1")
element_get_text = element.text
assert element_get_text == "HTML5 Forms"