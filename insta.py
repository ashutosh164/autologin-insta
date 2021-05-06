from conf import INSTA_PASSWORD, INSTA_USERNAM
from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='C:\chromdriver\chromedriver.exe')
url = 'http://www.instagam.com'
browser.get(url)

time.sleep(2)
username_el = browser.find_element_by_name('username')
username_el.send_keys(INSTA_USERNAM)

password_el = browser.find_element_by_name('password')
password_el.send_keys(INSTA_PASSWORD)

time.sleep(2)
submit_btn = browser.find_element_by_css_selector("button[type='submit']")
submit_btn.click()




