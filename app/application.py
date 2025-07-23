from selenium import webdriver
from pages.registration_page import RegistrationPage

class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.registration_page = RegistrationPage(self.driver)

