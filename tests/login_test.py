
import unittest
from selenium import webdriver

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'/home/eugene/first_test/drivers/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_user_login(self):
        driver = self.driver
        driver.get("https://locations.film/log-in")
        email_field = driver.find_element_by_xpath("//section[@id='main']/div/div/div/div/form/div/div/input")
        email_field.clear()
        email_field.send_keys("autotest23@zhenua.com")
        password_field = driver.find_element_by_xpath("//input[@id='password']")
        password_field.clear()
        password_field.send_keys("123456789")
        button_login = driver.find_element_by_xpath("//section[@id='main']/div/div/div/div/form/div[3]/button/b")
        button_login.click()
        assert driver.find_element_by_xpath("//small[contains(text(),'autotest23@zhenua.com')]")

    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()