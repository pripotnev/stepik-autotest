from selenium import webdriver
import time
import math
import os
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

#start every thing
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    driver = webdriver.Chrome()
    driver.get(link)

    #find the button and click
    button = driver.find_element_by_class_name("btn").click()
    
    #find the new window 
    new_window = driver.window_handles[1]
    #old_window = driver.window_handles[0]     #This is just for practice
    #print(old_window)
    driver.switch_to.window(new_window)

    #find x and apply to formula
    x = driver.find_element_by_id("input_value").text
    y = calc(x)
    inputField = driver.find_element_by_id("answer")
    inputField.send_keys(y)

    #find submit button and click
    submitButton = driver.find_element_by_class_name("btn")
    submitButton.click()

    #find token number and copy it to var 'token'
    alert = driver.switch_to.alert
    alert_text = alert.text.split()
    alert.accept()
    token = alert_text[-1]
    #print(alert_text)
    #print(token)          #just to see what it is
    

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
    link2 = "https://stepik.org/lesson/184253/step/6?unit=158843"
    driver.get(link2)
    time.sleep(3)

    #find text for right answer input, scroll down if needed
    answer_input = driver.find_element_by_css_selector('textarea')
    driver.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
    answer_input.send_keys(token)

    #find submit button and click
    button = driver.find_element_by_class_name('submit-submission')
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
