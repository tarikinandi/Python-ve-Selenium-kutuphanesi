from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

class Test:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.google.com/intl/tr/gmail/about/")
    
    def teardown_method(self):
        self.driver.quit()



    def test_valid_login(self):
        clickAccount =self.driver.find_element(By.XPATH,"/html/body/header/div/div/div/a[2]")
        clickAccount.click()
        
        sleep(5)
        mail = self.driver.find_element(By.CSS_SELECTOR,"#identifierId").send_keys("kisiselgelisimim02@gmail.com")
        sleep(5)
        clickNext = self.driver.find_element(By.CSS_SELECTOR,"#identifierNext > div > button > span")
        clickNext.click()
        sleep(5)
        password = self.driver.find_element(By.NAME,"Passwd").send_keys("Sanane0201")
        sleep(5)
        clickNext2 = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
        clickNext2.click()
        sleep(20)




    def waitForElementVisible(self , locator , timeout=5):
        WebDriverWait(self.driver , timeout).until(ec.visibility_of_element_located(locator))
        

    