from selenium import webdriver
import time 



try:
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")  # <- Путь до файла хромдрайвера
    browser.get(link)

    input1 = browser.find_element_by_tag_name(By.TAG_NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    driver.close()
    
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
