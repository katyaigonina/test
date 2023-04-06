from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 

    browser = webdriver.Chrome()
    browser.execute_script("alert('Robots at work');")


    link = " https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Ваш код, который заполняет обязательные поля
    span1 = browser.find_element(By.ID, 'num1')
    span1 = span1.text

    span2 = browser.find_element(By.ID, 'num2')
    span2 = span2.text
  
    y = int(span1) + int(span2)
    print(y)
    value1='"[value1'+str(y)+']"'
    print(value1)

    select = Select (browser.find_element(By.TAG_NAME, "select").click()
    select.select_by_value(str(y))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()




    #people_radio = browser.find_element(By.ID, "peopleRule")

    #people_checked = people_radio.get_attribute("checked")
    #print("value of people radio: ", people_checked)
    #assert people_checked is not None, "People radio is not selected by default"

    #robots_radio = browser.find_element(By.ID, "robotsRule")
    #robots_checked = robots_radio.get_attribute("checked")
    #assert robots_checked is None

    #robots_radio = browser.find_element(By.CSS_SELECTOR, "button.btn")
    #robots_checked = robots_radio.get_attribute ('disabled="disabled"')
    #assert robots_checked is None

    
    # Отправляем заполненную форму
    
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)
    # находим элемент, содержащий текст

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()