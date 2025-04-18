from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By

from dotenv import load_dotenv
import os

def configure():
    load_dotenv()


text_message = "Hey [person.first_name] it's Mark from Fit19. With Summer only 8 weeks away, we are letting 10 members work with a coach with 0 RISK! There is no commitment, no cancellation fee, and no money down! These spots are limited and will go fast! Let me know if you're interested, and we can explain how it works."

configure()

def send_member_a_text():
    ### SETTING MEMBER TEXT INFO ###
    time.sleep(1)

    table = driver.find_element('class name', "table")
    time.sleep(.3)
    link =  table.find_element('class name', 'link')
    a_tag = link.find_element(By.TAG_NAME, "a")
    a_tag.click()

    # Wait for the page to load
    time.sleep(1.5)

    try:
        sms_link = driver.find_element(By.XPATH, "//a[normalize-space(text())='SMS']")
        sms_link.click()
        time.sleep(1)
    except Exception as e:
        print("SMS button not found:", e)
        return

    text_input = driver.find_element(By.ID, 'text')

    # Clear any existing text and send the new message
    text_input.clear()
    text_input.send_keys(text_message)

    time.sleep(1)

    # Find the label associated with the radio button and click its span
    later_label = driver.find_element(By.XPATH, "//label[@for='scheduled_true']")
    later_span = later_label.find_element(By.TAG_NAME, 'span')
    later_span.click()

    time.sleep(1)

    # Fi
    date_box = driver.find_element(By.ID, 'date')
    date_box.click()

    time.sleep(1)

    # Locate the div containing the date picker
    ui_date_table = driver.find_element(By.ID, 'ui-datepicker-div')

    # Find the <td> element with the text "21" inside the <a> tag
    day_element = ui_date_table.find_element(By.XPATH, ".//td[contains(., '21')]")

    # Click the <a> tag inside that <td> element
    day_element.find_element(By.TAG_NAME, 'a').click()

    time.sleep(1)

    #Send Elements
    send_button = driver.find_element(By.XPATH, "//button[@data-form-button='primary']")
    send_button.click()

    time.sleep(2)


def free_member_from_queue():

    ### CLEARING MEMBER FROM QUEUE ###

    # Go back using the browser's back function
    driver.back()
    time.sleep(1)

    checkbox = driver.find_element(By.XPATH, "//input[starts-with(@id, 'complete_')]/following-sibling::label/span")
    checkbox.click()


    time.sleep(1)

    containers = driver.find_elements(By.CLASS_NAME, 'container')
    main_box = containers[2]
    
    label = main_box.find_element(By.CSS_SELECTOR, 'label[for="outcome_left_message"]')

    # Find the span inside the label and click it
    span = label.find_element(By.TAG_NAME, 'span')
    span.click()

    time.sleep(1)

    # Find the Save button inside the main_box and click it
    save_button = main_box.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary[data-form-button="primary"]')
    save_button.click()

    time.sleep(1)





# Set up Selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Start at the base URL
url = 'https://login.gymsales.net/calendar/today'
driver.get(url)

time.sleep(1)  # Wait for page

form_divs = driver.find_elements("class name", "form-controls")

email_input = driver.find_element(By.ID, "user_email")
email_input.clear()
email_input.send_keys(f"{os.getenv('username')}")

# Locate the password input field by its ID and enter the password
password_input = driver.find_element(By.ID, "user_password")
password_input.clear()
password_input.send_keys(f"{os.getenv('password')}")

sign_in_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-block")
sign_in_button.click()

time.sleep(2.5)

# Find the <ul> element containing the nav tabs
nav_tabs = driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs")

# Find all <li> elements inside the nav_tabs
li_elements = nav_tabs.find_elements(By.TAG_NAME, "li")

# Loop through the <li> elements and click the <a> tag inside the <li> with specific text
for li in li_elements:
    a_tag = li.find_element(By.TAG_NAME, "a")
    if "Overdue" in a_tag.text:  # Replace 'Overdue' with the text you're looking for
        a_tag.click()  # Click on the <a> tag
        break

for i in range(1000):  
    send_member_a_text()
    free_member_from_queue()
        
