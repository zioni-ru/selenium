import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

#'224592'
try:
    link = "http://suninjuly.github.io/find_link_text"
    browser = webdriver.Chrome(executable_path=r"C:\Chromedriver\chromedriver.exe")  # <- Путь до файла хромдрайвера
    browser.get(link)

    link = browser.find_element_by_partial_link_text('224592')
    link.click()

    input1 = browser.find_element_by_tag_name('.container input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    time.sleep(30)
    browser.close()
    browser.quit()