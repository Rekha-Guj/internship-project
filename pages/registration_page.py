from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage(BasePage):

    url = 'https://soft.reelly.io/sign-up'

    USER_NAME = (By.ID, 'Full-Name')
    PHONE_NUMBER = (By.XPATH, "//input[@id='phone2']")
    EMAIL = (By.XPATH, "//input[@id='Email-3']")
    PASSWORD = (By.XPATH, "//input[@id='field']")
    COMPANY_NAME = (By.XPATH, "//input[@id='Company-website']")
    USER_SIDE_REPRESENT = (By.XPATH, "//option[text()='Developer']")
    POSITION = (By.XPATH, "//select[@id='Position']")
    COUNTRY = (By.XPATH, "//option[text()='United States of America']")
    COMPANY_SIZE = (By.XPATH, " //option[@value='I work alone']")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//a[@class='login-button w-button']")

    USER_NAME_AFTER_LOGIN = (By.XPATH, "//div[@class='name_text_account']")

    def open(self):
        self.driver.get(self.url)
        time.sleep(2)

    def fill_registration_form(self):
        self.input_text('test rek3 careerist',  *self.USER_NAME)
        time.sleep(1)
        self.input_text('+951 test careerist', *self.PHONE_NUMBER)
        time.sleep(1)
        self.input_text('rek3@gmail.com', *self.EMAIL)
        time.sleep(1)
        self.input_text('rek3password', *self.PASSWORD)
        time.sleep(1)
        self.input_text('Test', *self.COMPANY_NAME)
        time.sleep(1)

        # Representative Dropdown
        self.wait.until(EC.element_to_be_clickable((By.ID, 'Role'))).click()
        self.wait.until(EC.element_to_be_clickable(self.USER_SIDE_REPRESENT)).click()
        time.sleep(1)

        # Country dropdown
        self.wait.until(EC.element_to_be_clickable((By.ID, 'country-select'))).click()
        self.wait.until(EC.element_to_be_clickable(self.COUNTRY)).click()
        time.sleep(1)

        # Company Size dropdown
        self.wait.until(EC.element_to_be_clickable((By.ID, 'Agents-amount-2'))).click()
        self.wait.until(EC.element_to_be_clickable(self.COMPANY_SIZE)).click()
        time.sleep(1)

        self.click( *self.CREATE_ACCOUNT_BTN)
        time.sleep(5)

    def verify_registration_form(self):

        user_name_after_login = self.driver.find_element(*self.USER_NAME_AFTER_LOGIN).text
        user_name_while_reg = "test rek3 careerist"

        assert user_name_after_login == user_name_while_reg,\
            f"Error: Expected '{user_name_after_login}' not matching with '{user_name_while_reg}'"


