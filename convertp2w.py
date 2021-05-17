from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def WordtoPDF():
        driver = webdriver.Chrome()
        driver.get('https://document.online-convert.com/convert/doc-to-pdf')
        wait = WebDriverWait(driver,10)
        field1 = wait.until(lambda driver: driver.find_element_by_id('fileUploadButton'))
        driver.find_element_by_id('fileUploadButton').send_keys("C:\\Users\\Reena\\Downloads\\OST_23_8.doc")
        field4 = wait.until(lambda driver: driver.find_element_by_id('multifile-submit-button-main'))
        driver.find_element_by_id('multifile-submit-button-main').click()
        field2 = wait.until(lambda driver: driver.find_element_by_id('download-list-form'))
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[4]/div[2]/div[2]/div/div[2]/div[2]/div[6]/div[3]/form/div[2]/div[3]/a').click()
        import anything