from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



def browser_init(context):
    """
    :param context: Behave context
    """

    ######### Chrome ###########

    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)

    ######### Gecko / Firefox ###########

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)

    ########### HeadLess Mode ############

    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    context.driver = webdriver.Chrome(
        options = options,
    )


    # browser = context.config.userdata.get("browser", "chrome").lower()
    # headless = context.config.userdata.get("headless", "true").lower() == "true"
    #
    # print("Received config:", context.config.userdata)
    # print(f"Launching browser: {browser}, headless: {headless}")
    #
    # if browser == "chrome":
    #     options = ChromeOptions()
    #     if headless:
    #         options.add_argument("--headless")
    #         options.add_argument("--disable-gpu")
    #         options.add_argument("--window-size=1920,1080")
    #
    #     service = ChromeService(ChromeDriverManager().install())
    #     context.driver = webdriver.Chrome(service=service, options=options)
    #
    # elif browser == "firefox":
    #     options = FirefoxOptions()
    #     if headless:
    #         options.add_argument("--headless")
    #
    #     service = FirefoxService(GeckoDriverManager().install())
    #     context.driver = webdriver.Firefox(service=service, options=options)
    #
    # else:
    #     raise ValueError(f"Unsupported browser: {browser}")
    #
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(10)

def before_scenario(context, scenario):

    print('\nStarted scenario: ', scenario.name)
    browser_init(context)

    #### Chrome #####
    # context.driver = webdriver.Chrome()

    #### Firefox #####
    # context.driver = webdriver.Firefox()

    print("\nStarted scenario:", scenario.name)
    try:
        browser_init(context)
    except Exception as e:
        print(f"Error during browser initialization: {e}")
        raise

def before_step(context, step):
    print('\nStarted step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)

def after_scenario(context, feature):
    if hasattr(context, "driver"):
        context.driver.quit()


