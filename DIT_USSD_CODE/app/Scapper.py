import csv
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.conf import settings
from selenium.webdriver.chrome.service import Service
import requests
from bs4 import BeautifulSoup as bs
from getpass import getpass

def extractingResults(result_type, username, password):
    # Set up Chrome driver
    print('running')
    chrome_path = settings.STATICFILES_DIRS[0] +r'\chromedriver_win32 (1)\chromedriver.exe'

    # Set up the ChromeDriver service
    service = Service(chrome_path)

    # Set up Chrome driver with the specified service
    driver = webdriver.Chrome(service=service)

    # Navigate to SOMA login page
    driver.get("https://soma.dit.ac.tz/login")

    # Enter email and password
    email_input = driver.find_element(By.ID, "username-soma")
    email_input.send_keys(username)
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)

    # Click login button
    login_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-block')
    login_button.click()
    # Wait for page to load
    time.sleep(5)

    # Navigate to Result page with comments
    driver.get("https://soma.dit.ac.tz/class-progress/student")
    # Wait for page to load
    time.sleep(5)

    # Wait for page to load
    time.sleep(5)

    if result_type == 1:
        # Click result button
        login_button = driver.find_element(By.XPATH, '//*[@id="nav-view-results0tab"]')
        login_button.click()


        # Wait for the table to be visible
        time.sleep(5)

        table_element = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#viewStudentResults0Tab > div > div.card-body"))
        )

        # Now you can interact with the table_element
        # For example, you can retrieve the text content of the element
        table_text = table_element.text
        driver.quit()
        return table_text

    if result_type == 2:
        # Navigate to Result page with comments
        driver.get("https://soma.dit.ac.tz/class-progress/student")
        # Wait for page to load
        time.sleep(5)

        # Wait for page to load
        time.sleep(5)


        # Click result button
        login_button = driver.find_element(By.XPATH, '//*[@id="nav-view-results1tab"]')
        login_button.click()


        # Wait for the table to be visible
        time.sleep(5)

        table_element = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#viewStudentResults1Tab > div > div.card-body"))
        )

        # Now you can interact with the table_element
        # For example, you can retrieve the text content of the element
        table_text = table_element.text
        driver.quit()
        return table_text

    if result_type == 3:
        # Navigate to Result page with comments
        driver.get("https://soma.dit.ac.tz/class-progress/student")
        # Wait for page to load
        time.sleep(5)

        # Wait for page to load
        time.sleep(5)


        # Click result button
        login_button = driver.find_element(By.XPATH, '//*[@id="nav-view-results2tab"]')
        login_button.click()


        # Wait for the table to be visible
        time.sleep(5)

        table_element = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#viewStudentResults2Tab > div > div.card-body"))
        )

        # Now you can interact with the table_element
        # For example, you can retrieve the text content of the element
        table_text = table_element.text
        driver.quit()
        return table_text

    if result_type == 4:
        # Navigate to Result page with comments
        driver.get("https://soma.dit.ac.tz/class-progress/student")
        # Wait for page to load
        time.sleep(5)

        # Wait for page to load
        time.sleep(5)


        # Click result button
        login_button = driver.find_element(By.XPATH, '//*[@id="nav-view-results3tab"]')
        login_button.click()


        # Wait for the table to be visible
        time.sleep(5)

        table_element = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#viewStudentResults3Tab > div > div.card-body"))
        )

        # Now you can interact with the table_element
        # For example, you can retrieve the text content of the element
        table_text = table_element.text
        driver.quit()
        return table_text

def checking_registration(email, password):
    statement = ''
    payment = False
    registration = False
    confirmation = False
    
    login_url = 'https://soma.dit.ac.tz/login'
    secure_url = 'https://soma.dit.ac.tz/'
    session = requests.Session()
    secure_url = 'https://soma.dit.ac.tz/'
    request = session.get(login_url).content
    soup = bs(request,'html.parser')
    csrf = soup.find('input',{'name':'csrf'}).get('value')
    payload = {
            'email': email,
            'password': password,
            'csrf': csrf,
            }
    p = session.post(login_url,data=payload)
    print('ok')
    if 'Welcome, you have successfully logged into your account' in p.text:
        print('login successful')
        t = session.get(secure_url)

        soup = bs(t.text, "html.parser")

        result_url = (f'https://soma.dit.ac.tz/admission/registrationct')
        admision_status = session.get(result_url).text
        admision_statuss = bs(admision_status,'html.parser')
        link =admision_statuss.select('div.row i')
        for index, data in enumerate(link[:3]):
            results = data.get('class')[1]
            if results == 'fa-check-circle':
                if index == 0:
                    payment = True
                elif index == 1:
                    registration = True
                else:
                    confirmation = True
    if confirmation:
         statement = 'You are registered.'
    elif registration and not confirmation:
        statement = 'Please visit admission office for confirmation.'
    elif payment and not registration:
        statement = 'Please just register your modules.'
    else:
        statement = 'Please accomplish tution fee.'
    return statement