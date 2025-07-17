from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from sample_script import driver


class RegistrationPage(BasePage):

    USER_NAME = (By.ID, 'Full-Name')
    PHONE_NUMBER = (By.ID, 'Phone2')
    EMAIL = (By.ID, 'Email-3')
    PASSWORD = (By.ID, 'field')
    COMPANY_NAME = (By.ID, 'Company-website')
    USER_SIDE_REPRESENT = (By.XPATH, "//option[text()='Developer'")
    POSITION = (By.ID, 'Position')
    COUNTRY = (By.XPATH, "//option[text()='United States of America']")
    COMPANY_SIZE = (By.ID, 'Agents-amount-2')
    CREATE_ACCOUNT_BTN = (By.XPATH, "//a[@class='login-button w-button']")
    url = 'https://soft.reelly.io/sign-up'

    def open(self):
        self.driver.get(self.url)

    def form_fill(self):
        self.input_text('test rekhaguj careerist',  *self.USER_NAME)
        self.input_text('+971 test careerist', *self.PHONE_NUMBER)
        self.input_text('test@gmail.com', *self.EMAIL)
        self.input_text('testpassword', *self.PASSWORD)
        self.input_text('Test', *self.COMPANY_NAME)

        # Representative Dropdown
        driver.find_element(By.ID, 'Role').click()
        self.click(*self.USER_SIDE_REPRESENT)

        # Country dropdown
        driver.find_element(By.ID, 'country-select').click()
        self.click(*self.COUNTRY)

        self.click( *self.CREATE_ACCOUNT_BTN)

    def verify_registration_form(self):
        user_name_in_app = self.driver.find_element(By.XPATH, "//div[@class='name_text_account']").text
        user_name_while_reg = self.driver.find_element(By.ID, 'Full-Name').text
        assert user_name_in_app == user_name_while_reg,\
            f"Error: Expected '{user_name_in_app}' not matching with '{user_name_while_reg}'"

