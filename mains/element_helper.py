from selenium.common import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException, \
    ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from mains import config_utils
from mains.driver_utils import DriverUtils


class ElementHelper:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ElementHelper, cls).__new__(cls)
            cls.config = config_utils.read_base_config_file()
            cls.driver_utils = DriverUtils()

        return cls.instance

    def __init__(self):
        self.driver = self.driver_utils.get_driver_object()
        self.wait = WebDriverWait(self.driver, self.config['default_explicit_wait'])

    def get_wait_object(self):
        return self.wait

    def set_driver_object(self):
        self.driver = self.driver_utils.get_driver_object()
        self.wait = WebDriverWait(self.driver, self.config['default_explicit_wait'])

    def get_locator_strategy(self, locator, str_to_replace=None):
        if str_to_replace and str(locator).__contains__("{}"):
            locator = str(locator).replace("{}", str_to_replace)

        locator_details = locator.split('=', 1)
        locator_details[0] = getattr(By, locator_details[0].upper())
        return locator_details

    def set_implicit_wait(self, wait_seconds):
        self.driver.implicitly_wait()

    def reset_implicit_wait(self):
        self.driver.implicitly_wait(int(self.config['default_implicit_wait']))

    def get_element(self, locator, str_to_replace=None):
        if type(locator) == WebElement:
            return locator
        else:
            locator_details = self.get_locator_strategy(locator, str_to_replace)
            return self.driver.find_element(locator_details[0], locator_details[1])

    def get_element_list(self, locator, str_to_replace=None):
        try:
            locator_details = self.get_locator_strategy(locator, str_to_replace)
            return self.driver.find_elements(locator_details[0], locator_details[1])
        except NoSuchElementException as e:
            print("Element not found")
            raise e
        except Exception as e:
            print("Exception occurred: " + str(e))
            raise e

    def type(self, locator, text, str_to_replace=None):
        self.get_element(locator, str_to_replace).send_keys(text)

    def set_value(self, locator, value, str_to_replace=None):
        element = self.get_element(locator, str_to_replace)
        element.clear()
        element.set_value(value)

    def action_type(self, text):
        actions = ActionChains(self.driver)
        actions.send_keys(text).perform()

    def navigate(self, url):
        self.driver.get(url)

    def click(self, locator, str_to_replace=None):
        try:
            self.get_element(locator, str_to_replace).click()
        except ElementClickInterceptedException as e:
            if e.msg.__contains__("Other element would receive the click: <div id=\"coiOverlay\" role=\"banner\""):
                banner_button = "xpath=//button[text()='JAG GODKÄNNER']"
                self.get_element(banner_button).click()
                self.wait_for_invisibility_of(banner_button)
                self.get_element(locator, str_to_replace).click()
        except Exception as e:
            print("There is an error clicking on the element located by " + str(locator))
            print(str(e))

    def get_element_text(self, locator, str_to_replace=None):
        try:
            return self.get_element(locator, str_to_replace).text
        except StaleElementReferenceException as e:
            return ''
        except NoSuchElementException as e:
            return ''

    def back(self):
        self.driver.back()

    def is_element_displayed(self, locator, str_to_replace=None):
        try:
            element = self.get_element(locator, str_to_replace)
            if type(element) is WebElement:
                return element.is_displayed()
            else:
                return False
        except ElementNotInteractableException as e:
            print("Element " + locator + " is not accessible.")
            return False
        except NoSuchElementException as e:
            print("Element " + locator + " is not available.")
            return False
        except StaleElementReferenceException as e:
            print("Element " + locator + " is not accessible.")
            return False

    def is_element_enabled(self, locator, str_to_replace=None):
        try:
            element = self.get_element(locator, str_to_replace)
            if type(element) is WebElement:
                return element.is_enabled()
            else:
                return False
        except ElementNotInteractableException as e:
            print("Element " + locator + " is not accessible.")
            return False
        except NoSuchElementException as e:
            print("Element " + locator + " is not available.")
            return False

    def get_attribute(self, locator, attr_name):
        try:
            element = self.get_element(locator)
            attribute = element.get_attribute(attr_name)
            if attribute is None:
                return ''
            else:
                return attribute
        except Exception as e:
            return ''

    def get_url(self):
        try:
            return self.driver.current_url
        except Exception as e:
            return ''

    def get_page_title(self):
        return self.driver.title

    def wait_for_element_displayed(self, locator):
        try:
            if type(locator) == WebElement:
                self.wait.until(EC.visibility_of(locator))
                return True
            else:
                locator_details = self.get_locator_strategy(locator)
                self.wait.until(EC.visibility_of_element_located((locator_details[0], locator_details[1])))
                return True
        except TimeoutException:
            return False

    def wait_for_staleness_of(self, locator):
        try:
            element = self.get_element(locator)
            self.wait.until(EC.staleness_of(element))
            return True
        except Exception as e:
            print(e.msg)
            return False

    def wait_for_invisibility_of(self, locator):
        try:
            element = self.get_element(locator)
            self.wait.until(EC.invisibility_of_element(element))
            return True
        except NoSuchElementException as e:
            return True
        except Exception as e:
            print(e.msg)
            return False
