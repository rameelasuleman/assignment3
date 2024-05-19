from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


class MyAppTests:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_login(self):
        self.driver.get("http://3.89.113.67:3000/login")
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        email_input.send_keys("muhammadumarrasheed68@gmail.com")
        password_input.send_keys("123456")
        submit_button.click()

        time.sleep(5)  # Wait for the page to load
        assert "Dashboard" in self.driver.page_source

    def test_register(self):
        self.driver.get("http://3.89.113.67:3000/register")

        name_input = self.driver.find_element(By.ID, "name")
        email_input = self.driver.find_element(By.ID, "email")
        password_input = self.driver.find_element(By.ID, "password")
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        name_input.send_keys("Test User")
        email_input.send_keys("testuser1@example.com")
        password_input.send_keys("testpassword")
        submit_button.click()

        time.sleep(5)  
        assert "Login" in self.driver.page_source

    def close_browser(self):
        self.driver.quit()


if __name__ == "__main__":
    tests = MyAppTests()
    tests.test_login()
    tests.test_register()
    tests.close_browser()
