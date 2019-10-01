from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try: 
    link = " http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(executable_path=r"C:\Chromedriver\chromedriver.exe")
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element_by_tag_name("div div [placeholder='Input your first name']")
    input1.send_keys("Ivan")

    input1 = browser.find_element_by_tag_name("div div [placeholder='Input your last name']")
    input1.send_keys("Petrov")

    input1 = browser.find_element_by_tag_name("div div [placeholder='Input your email']")
    input1.send_keys("I.Petrov@mail.ru")

    input1 = browser.find_element_by_tag_name("div div [placeholder='Input your phone:']")
    input1.send_keys("+7 903 903 00 00")

    input1 = browser.find_element_by_tag_name("div div [placeholder='Input your address:']")
    input1.send_keys("Moscow")


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()