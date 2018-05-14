import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ConfigParser
import unittest


class TestSignUp(unittest.TestCase):
    def setUp(self):
        self.config = ConfigParser.RawConfigParser()
        self.config.read('test.properties')
        chromedriver = self.config.get('Selenium', 'chromedriver')
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window() 

    def test_sign_up(self):
        self.driver.get("https://www.shipt.com/")
        
        if not (self.driver.find_element_by_id('offer-pop') is None):
            wait = WebDriverWait(self.driver, 10) 
            pop_close = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[3]/div/div/div/div/section/button')))
            pop_close.click()
            wait = WebDriverWait(self.driver, 15) 
            wait.until_not(EC.visibility_of_element_located((By.ID, 'offer-pop')))
            button_primary = self.driver.find_element_by_xpath("//*[contains(text(), 'Get Started')]")
            button_primary.click()
        else:
            wait = WebDriverWait(self.driver, 10)
            button_primary = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Sign up')]")))
            button_primary.click()
       
        wait = WebDriverWait(self.driver, 10)
        email = wait.until(EC.visibility_of_element_located((By.ID,'email')))
        email.clear()
        p_email = self.config.get('SignUpTest', 'email')
        email.send_keys(p_email)
        zip_code = self.driver.find_element_by_id('zip')
        zip_code.clear()
        p_zip = self.config.get('SignUpTest', 'zipCode')
        zip_code.send_keys(p_zip)   
        button_submit = self.driver.find_element_by_xpath("//*[contains(text(), 'Redeem Code')]")   
        button_submit.click()
    
        plan = self.driver.find_element_by_xpath("//*[contains(text(), 'Start Annual Plan')]")
        plan.click()
        
        wait = WebDriverWait(self.driver, 10)
        full_name = wait.until(EC.visibility_of_element_located((By.ID, 'name')))
        full_name.clear()
        p_full_name = self.config.get('SignUpTest', 'fullName')
        full_name.send_keys(p_full_name)
        mobile_number = self.driver.find_element_by_id('phone')
        mobile_number.clear()
        p_mobile_number = self.config.get('SignUpTest', 'mobileNumber')
        mobile_number.send_keys(p_mobile_number)
        password = self.driver.find_element_by_id('password')
        password.clear()
        p_password = self.config.get('SignUpTest', 'password')
        password.send_keys(p_password) 
        
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Payment Info')]")))
        self.driver.switch_to.frame(self.driver.find_element_by_name("__privateStripeFrame4"))
        card_number = self.driver.find_element_by_name("cardnumber")
        p_card_number = self.config.get('SignUpTest', 'cardNumber')
        card_number.send_keys(p_card_number) 
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element_by_name("__privateStripeFrame5"))
        exp_date = self.driver.find_element_by_name("exp-date")
        exp_date.clear()
        p_exp_date = self.config.get('SignUpTest', 'exp-date')
        exp_date.send_keys(p_exp_date) 
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element_by_name("__privateStripeFrame6"))
        security_code = self.driver.find_element_by_name('cvc')
        security_code.clear()
        p_security_code = self.config.get('SignUpTest', 'securityCode')
        security_code.send_keys(p_security_code) 
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(self.driver.find_element_by_name("__privateStripeFrame7"))
        zip_code = self.driver.find_element_by_name('postal') 
        zip_code.clear()
        p_zip = self.config.get('SignUpTest', 'zipCode')
        zip_code.send_keys(p_zip)    
        self.driver.switch_to_default_content()
        button_start_membership = self.driver.find_element_by_xpath("//*[contains(text(), 'Start Membership')]")
        button_start_membership.click()   
        message = self.driver.find_element_by_xpath("//p[contains(@class, 'error') and contains(@class, 'ng-binding') and contains(@class, 'ng-scope')]")
        self.assertEqual(message.text, 'Your card was declined. Your request was in live mode, but used a known test card.')           

    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()