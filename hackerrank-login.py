from selenium import webdriver
from getpass import getpass

username = input("Enter Username: \n")
password = getpass("Enter Password: \n")

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.hackerrank.com/auth/login?h_l=body_middle_left_button&h_r=login")

username_textbox = driver.find_element_by_id("input-1")
username_textbox.send_keys(username)
password_textbox = driver.find_element_by_id("input-2")
password_textbox.send_keys(password)

login_button = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/form/div[4]/button").click()