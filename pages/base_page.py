from selenium.webdriver.support.wait import WebDriverWait
from sample_script import driver
from selenium.webdriver.support import expected_conditions as EC
from support.logger import logger

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.base_url = 'https://soft.reelly.io/sign-up'

    def open_url(self, end_url=''):
        url = f'{self.base_url}{end_url}'
        logger.info(f'Opening url: {url}')
        self.driver.get(url)

    def find_element(self, *locator):
        logger.info(f"Finding element with locator: {locator}")
        return self.driver.find_element(*locator)

    def click(self, *locator):
        logger.info(f"Clicking on element with locator: {locator}")
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        logger.info(f"Enter '{text}' with in Locator {locator}")
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element_click(self, *locator):
        logger.info(f"Waiting and clicking on element: {locator}")
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} not clickable'
        ).click()

    def wait_for_element(self, *locator):
        logger.info(f"Waiting for element: {locator}")
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} not visible'
        )

    def wait_for_element_disappear(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element by {locator} still visible'
        )

    def wait_for_url_contains(self, partial_url):
        self.wait.until(EC.url_contains(partial_url), message=f'Expected {partial_url} not in url')

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert actual_text == expected_text, '....'

    def verify_text1(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f"Expected text: {expected_text}, did not match Actual text: {actual_text}"

    def verify_partial_text(self, expected_partial_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_partial_text in actual_text, f"Expected text: {expected_partial_text}, not in Actual text: {actual_text}"

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Expected url: {expected_url}, did not match Actual url: {actual_url}"