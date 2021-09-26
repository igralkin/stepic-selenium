from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(executable_path= "C:\\chromedriver\\chromedriver.exe")
    browser.get(link)

    button1 = browser.find_element_by_class_name("trollface")
    button1.click()

    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла