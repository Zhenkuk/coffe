import datetime
import unittest
from selenium import webdriver

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'/home/eugene/first_test/drivers/chromedriver')
        print ("Run Started at :"+str(datetime.datetime.now()))
        print("Chrome Environment Set Up")
        print("------------------------------------------------------------------")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def test_user_registration(self):
        driver = self.driver
        driver.get("https://locations.film")
        check_this = driver.find_element_by_xpath("//ul[@class='uk-navbar-nav uk-hidden-small']//li[3]//a[1]")
        check_this.click()
        first_name_field = driver.find_element_by_xpath("//input[@id='first_name']")
        first_name_field.send_keys("autotest1")
        last_name_field = driver.find_element_by_xpath("//input[@id='last_name']")
        last_name_field.send_keys("autotest2")
        email_field = driver.find_element_by_xpath("//input[@id='email']")
        email_field.send_keys("autotest29@zhenua.com")
        password_field = driver.find_element_by_xpath("//input[@id='password']")
        password_field.send_keys("123456789")
        password_confirmation_field = driver.find_element_by_xpath("//div[5]/input")
        password_confirmation_field.send_keys("123456789")
        button_login = driver.find_element_by_xpath("//section[@id='main']/div/div/div/div/form/div[6]/button/b")
        button_login.click()
        assert driver.find_element_by_xpath("//*[contains(text(),'Welcome to Easy Locations')]")
        assert driver.find_element_by_xpath("//small[contains(text(),'utotest2345678@zhenua.com')]")

    def tearDown(self):
     if (self.driver!=None):
        print("------------------------------------------------------------------")
        print("Test Environment Destroyed")
        print("Run Completed at :" + str(datetime.datetime.now()))
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()