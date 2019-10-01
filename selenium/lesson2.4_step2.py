from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome(executable_path=r"C:\Chromedriver\chromedriver.exe")
    browser.get(link)

   # element = WebDriverWait(browser, 15).until(
       # EC.text_to_be_present_in_element((By.ID, "price"), "$100")
   # )
    # print(element)

    button = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    
    # button.click()

# button = WebDriverWait(browser, 15).until(
#        EC.element_to_be_clickable((By.ID, "book"))
#    )
    button = browser.find_element_by_id("book")
    button.click()    


    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
  

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_id("solve")
    button.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()