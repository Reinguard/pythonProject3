from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()

mam = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()
ea = driver.find_element_by_css_selector("#reg_email").send_keys("edw@org.rs")
password = driver.find_element_by_css_selector("#reg_password").send_keys("jokker100500_")
reg = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[3]/input[3]")
reg.click()