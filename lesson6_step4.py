from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "C:/Users/111/testqa/3.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Михаил")

    
    button = browser.find_element(By.CSS_CELECTOR, 'button.btn' )
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

