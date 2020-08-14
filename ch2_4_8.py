from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

price = "$100"

#start every thing
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    driver = webdriver.Chrome()
    driver.get(link)

    #find price and wait until it become $100
    priceEq = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), price)
    )
    #find the button and click
    button = driver.find_element_by_id("book").click()
    
    #find x
    x_element = driver.find_element_by_id("input_value")
    x = x_element.text
    driver.execute_script("return arguments[0].scrollIntoView(true);", x_element)
    y = calc(x)
    inputField = driver.find_element_by_id("answer")
    inputField.send_keys(y)

    #find submit button and click
    submitButton = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    submitButton.click()
    time.sleep(3)

    #find token number and copy it to var 'token'
    alert = driver.switch_to.alert
    alert_text = alert.text.split()
    alert.accept()
    token = alert_text[-1]
    #print(alert_text)
    print(token)          #just to see what it is
    

    #go to stepic website
    
    driver.get('https://stepik.org/catalog?auth=login&language=ru')
    time.sleep(5)

    #log in
    driver.find_element_by_id('id_login_email').send_keys('pripotnev@gmail.com')  # здесь вводится e-mail
    driver.find_element_by_id('id_login_password').send_keys('$t@pStavla')  # здесь вводится пароль

    #find and click the login button
    driver.find_element_by_class_name('sign-form__btn').click()
    time.sleep(3)

    #go to the lesson's page
    link2 = "https://stepik.org/lesson/181384/step/8?unit=156009"
    driver.get(link2)
    answer_input = driver.find_element_by_css_selector('textarea')
    driver.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
    print(answer_input)
    time.sleep(3)
    answer_input.send_keys(token)

    #find submit button and click
    button = driver.find_element_by_class_name("submit-submission")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    time.sleep(1)
    button.click()

    time.sleep(1)
    #would be nice to wait for confirmation here
    message_correct = driver.find_element_by_class_name("attempt-message_correct")
    print(message_correct.text) #will print button cuption in the console "Right."

    #find button next-> click
    button = driver.find_element_by_class_name('lesson__next-btn')
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    time.sleep(1)
    button.click()
    
    #catch a new window
    new_window_again = driver.window_handles[1]
    driver.switch_to.window(new_window_again)
    time.sleep(10)

finally:
    # closing everything

    driver.quit()

    #last line in the code
