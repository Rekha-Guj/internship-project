from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage(BasePage):

    USER_NAME = (By.ID, 'Full-Name')
    PHONE_NUMBER = (By.XPATH, "//input[@id='phone2']")
    EMAIL = (By.XPATH, "//input[@id='Email-3']")
    PASSWORD = (By.XPATH, "//input[@id='field']")
    COMPANY_NAME = (By.ID, "//input[@id='Company-website']")
    USER_SIDE_REPRESENT = (By.XPATH, "//option[text()='Developer']")
    POSITION = (By.XPATH, "//select[@id='Position']")
    COUNTRY = (By.XPATH, "//option[text()='United States of America']")
    COMPANY_SIZE = (By.ID, 'Agents-amount-2')
    CREATE_ACCOUNT_BTN = (By.XPATH, "//a[@class='login-button w-button']")
    url = 'https://soft.reelly.io/sign-up'

    def open(self):
        self.driver.get(self.url)
        time.sleep(2)

    def fill_registration_form(self):
        self.input_text('test rekhaguj careerist',  *self.USER_NAME)
        time.sleep(1)
        self.input_text('+971 test careerist', *self.PHONE_NUMBER)
        time.sleep(1)
        self.input_text('test@gmail.com', *self.EMAIL)
        time.sleep(1)
        self.input_text('testpassword', *self.PASSWORD)
        time.sleep(1)
        self.input_text('Test', *self.COMPANY_NAME)
        time.sleep(1)

        # Representative Dropdown
        self.wait.until(EC.element_to_be_clickable((By.ID, 'Role'))).click()
        self.wait.until(EC.element_to_be_clickable(*self.USER_SIDE_REPRESENT)).click()

        # Country dropdown
        self.wait.until(EC.element_to_be_clickable((By.ID, 'country-select'))).click()
        self.wait.until(EC.element_to_be_clickable(*self.COUNTRY)).click()

        self.click( *self.CREATE_ACCOUNT_BTN)

    def verify_registration_form(self):
        user_name_in_app = self.driver.find_element(By.XPATH, "//div[@class='name_text_account']").text
        user_name_while_reg = self.driver.find_element(By.ID, 'Full-Name').text
        assert user_name_in_app == user_name_while_reg,\
            f"Error: Expected '{user_name_in_app}' not matching with '{user_name_while_reg}'"




