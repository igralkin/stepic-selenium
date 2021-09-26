from selenium import webdriver
import time 
import math

links = [
        "http://suninjuly.github.io/registration1.html",
        "http://suninjuly.github.io/registration2.html"
]

try:
    # browser = webdriver.Chrome(executable_path= "C:\\chromedriver\\chromedriver.exe")
    browser = webdriver.Chrome()  # вариант для Степика 
    for link in links:
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_block = browser.find_element_by_class_name("first_block")

        # Ввод имени
        first_name = first_block.find_element_by_class_name("first")
        first_name.send_keys("Ivan")
        # Ввод фамилии
        second_name = first_block.find_element_by_class_name("second")
        second_name.send_keys("Petrov")
        # Ввод почты
        email = first_block.find_element_by_class_name("third")
        email.send_keys("ivan@petrov.ru")
        # Отправка формы
        submit = browser.find_element_by_tag_name('button')

        time.sleep(2)
        submit.click()

        time.sleep(2)

        welcome_text = browser.find_element_by_tag_name('h1').text
        assert 'Congratulations' in welcome_text

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
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла