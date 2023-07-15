#https://linns.novascotia.ca/LINNSDB/index$.Startup

#https://user:password%40www.example.com

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import csv
import time

def tester(driver, streetName, streetType):

    #Accessing the register account webpage 	
    browser.get("https://USERNAME:PASSWORD@linns.novascotia.ca/LINNSDB/index$.Startup")

    #Clicking on the link to query page because we can't access it directly for some reason
    myLink = driver.find_element(By.PARTIAL_LINK_TEXT, 'Access Parcel and Assessment Information')
    myLink.click()

    #Switching to the next tab
    # Get the current window handle
    current_window = driver.current_window_handle
    # Get the handles of all open windows
    all_windows = driver.window_handles
    # Loop through all window handles
    for window in all_windows:
    # Switch to the next tab
        if window != current_window:
            driver.switch_to.window(window)
            break  # Break the loop after switching to the next tab

    #Using the name attribute to find the text box and inputting the value
    street_name = browser.find_element(By.NAME, "streetName")
    street_name.send_keys(streetName)

    #Entering the street type from the dropdown menu
    try:
        streetDropdown = browser.find_element(By.NAME, "streetType")
        select = Select(streetDropdown)
        select.select_by_visible_text(streetType)
    except:
        print("Problem with the street type input")

    #Increases results per page to 250
    try:
        dropdown = browser.find_element(By.XPATH, value="//select[@name='maximumNumberOfRecords']")
        dropdown.click()  # Click the dropdown to expand the options
        option = browser.find_element(By.XPATH, value="//option[@value='250']")
        option.click()  # Click the desired option
    except:
        print("something went wrong with number of records")
        #username = input("Enter username:")

    #Click the Submit Query button
    submitButton = browser.find_element(By.XPATH, value="//input[@value='Submit Query']")
    submitButton.click()

    #Save the webpage into html file
    html_content = driver.page_source
    file_path = 'webpages/' + streetName + streetType + '.html'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)        
    
    #Close the current browser window
    browser.quit()

    #dummy username prompt so python script doesn't close and close the browser
    #username = input("Enter username:")
    #print("Username is: " + username)

filename = 'NShousing/street-list-csv.csv'
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        time.sleep(5)
        print(row)
        streetName = row[0]
        streetType = row[1]
        #print(streetType)
        try:
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#streetName = 'A Y JACKSON'
#streetType = 'COURT'
            tester(browser, streetName, streetType)
        except:
            print("there was a problem with the above row")