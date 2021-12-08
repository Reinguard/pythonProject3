from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()

driver.execute_script("window.scrollTo(0,600);")
book = driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.woocommerce-LoopProduct-link > h3")
book.click()
rev = driver.find_element_by_css_selector("#product-160 > div.woocommerce-tabs.wc-tabs-wrapper > ul > li.reviews_tab > a")
rev.click()
driver.execute_script("window.scrollTo(0,600);")
stars = driver.find_element_by_css_selector("#commentform > p.comment-form-rating > p > span > a.star-5")
stars.click()
pole = driver.find_element_by_css_selector("#comment").send_keys("Nice book!")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
name = driver.find_element_by_css_selector("#author").send_keys("Edward")
email = driver.find_element_by_css_selector("#email").send_keys("edw@or.rs")
submit = driver.find_element_by_name("submit")
submit.clik()




