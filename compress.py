from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("/home/ruvin27/Downloads/chromedriver")
driver.get("https://www.sejda.com/compress-pdf")
filebox=driver.find_element_by_xpath("/html/body/section/section[2]/section[1]/section[2]/div[2]/div/div/div[2]/span/form/input[2]")
filebox.send_keys("/home/ruvin27/Downloads/OST exp6 45.pdf")
WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/section[2]/div[2]/form/div/div[2]/button"))).click()
