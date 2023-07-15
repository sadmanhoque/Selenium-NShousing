from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def tester(driver):
    #chrome_options = Options()
    #chrome_options.add_experimental_option("detach", True)
    #driver = webdriver.Chrome(chrome_options=chrome_options)

    #accessing the register account webpage 	
    browser.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")

    #finding the first name text input field using its ID and saving it to a variable
    first_name = browser.find_element(By.NAME, "firstname")

    #using the variable to interact with the element and doing the text input 	
    first_name.send_keys("FirstNamekljnl")

    #finding the element for last name, telephone and email
    last_name = browser.find_element(By.ID, "input-lastname")
    telephone = browser.find_element(By.ID, "input-telephone")
    email = browser.find_element(By.ID, "input-email")

    #using the var to provide the text inputs	
    last_name.send_keys("LastName")
    email.send_keys("your-email@example.com")
    telephone.send_keys("+351999888777")

    #the same thing as before, but for the two password input fields now
    password = browser.find_element(By.ID, "input-password")
    password_confirm = browser.find_element(By.ID, "input-confirm")
    password.send_keys("123456")
    password_confirm.send_keys("123456")

    #We are using xpath to find the subscribe 'yes' button as the element does not have an id
    #This means that we are looking for an element in the page, that is a “label” that has an attribute called “for” 
    # with the value “input-newsletter-yes”.
    newsletter = browser.find_element(By.XPATH, value="//label[@for='input-newsletter-yes']")
    #To click the 'yes' button 	
    newsletter.click()

    #We do the same thing as above but for the checkbox agreeing to the privacy policy now	
    terms = browser.find_element(By.XPATH, value="//label[@for='input-agree']")
    terms.click()

    #This clicks on the 'continue' button at the end of the form
    continue_button = browser.find_element(By.XPATH, value="//input[@value='Continue']")
    continue_button.click()
    
    # Save the webpage
    html_content = driver.page_source

    # Save the HTML content to a file
    file_path = 'webpages/webpage.html'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
    
    #bogus input prompt so python doesn't close the webpage
    username = input("Enter username:")
    print("Username is: " + username)

    #Checks if the title for the browser tab changes to this specific text which ensures that the above commands all
    # worked
    #assert browser.title == "Your Account Has Been Created!"

#installing the Chrome browser specific dependencies
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
tester(browser)
