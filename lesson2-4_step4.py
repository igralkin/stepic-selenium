from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/cats.html"


try:
    browser = webdriver.Chrome(executable_path= "C:\\chromedriver\\chromedriver.exe")
    browser.implicitly_wait(5)
    browser.get(link)

    button = browser.find_element_by_id("button")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла