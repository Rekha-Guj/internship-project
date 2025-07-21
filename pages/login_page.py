from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class LoginPage(BasePage):

    url = "https://soft.reelly.io/sign-in"

    EMAIL = (By.XPATH, "//input[@id='email-2']")
    PASSWORD = (By.XPATH, "//input[@id='field']")
    LOGIN_BTN = (By.XPATH, "//a[@wized='loginButton']")
    LOGOUT_BTN = (By.XPATH, "//div[@wized='LogoutButton']")

    def open(self):
        self.driver.get(self.url)
        time.sleep(1)
        print("Login Page Opened")

    def login(self):
        self.input_text('test rek2 careerist',*self.EMAIL)
        self.input_text('rek2password',*self.PASSWORD)
        time.sleep(2)
        print("User credentials are entered")

    def verify_user_login(self):
        self.click(*self.LOGIN_BTN)
        time.sleep(1)
        print("User login is verified")

    def logout(self):
        self.click(*self.LOGOUT_BTN)
        print("User successfully logOut")

