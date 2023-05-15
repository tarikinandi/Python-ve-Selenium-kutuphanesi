from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from constants import globalConstants 

class Test_SwagLabs:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    def test_invalid_login(self):
        
        WebDriverWait(self.driver , 5).until(ec.visibility_of_element_located((By.ID , "user-name")))
        username = self.driver.find_element(By.ID , "user-name")
        password = self.driver.find_element(By.ID , "password")
        WebDriverWait(self.driver , 5).until(ec.visibility_of_element_located((By.ID , "password")))
        username.send_keys("standard_user")
        password.send_keys("11") 
        logButton = self.driver.find_element(By.ID ,"login-button" )
        logButton.click()
        errorMessage = self.driver.find_element(By.XPATH , "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Test sonucu : {testResult}")
    
    def test_valid_login(self):
        self.driver.get(globalConstants.URL)
        WebDriverWait(self.driver , 5).until(ec.visibility_of_element_located((By.ID , "user-name")))
        username = self.driver.find_element(By.ID , "user-name")
        password = self.driver.find_element(By.ID , "password")
        WebDriverWait(self.driver , 5).until(ec.visibility_of_element_located((By.ID , "password")))
        #Action Chains
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(username , "standard_user")
        actions.send_keys_to_element(password , "secret_sauce")
        actions.perform()
        # username.send_keys("standard_user")
        # password.send_keys("secret_sauce") 
        logButton = self.driver.find_element(By.ID ,"login-button" )
        logButton.click()
        self.driver.execute_script("window.scrollTo(0,500)")




testClass = Test_SwagLabs()
testClass.test_invalid_login()
testClass.test_valid_login()