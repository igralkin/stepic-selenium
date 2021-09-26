from selenium import webdriver
import time 
import os

link = "http://suninjuly.github.io/file_input.html"
file_name = "text.txt"

try:
    browser = webdriver.Chrome(executable_path= "C:\\chromedriver\\chromedriver.exe")
    browser.get(link)

    firstname = browser.find_element_by_css_selector("[name='firstname']")
    firstname.send_keys("First name")
    lastname = browser.find_element_by_css_selector("[name='lastname']")
    lastname.send_keys("Last name")
    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys("em@em.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, file_name)          # добавляем к этому пути имя файла 
    with open(file_path, "w") as file:
        file.write("automationbypython")
        print(file_path)
    time.sleep(1)
    element = browser.find_element_by_id("file")
    print('sending', file_path)
    element.send_keys(file_path)
    # time.sleep(5)
    #os.remove(file_name)

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла