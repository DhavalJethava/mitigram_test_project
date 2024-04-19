import os, platform
import time
from datetime import datetime

from mains import config_utils
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class DriverUtils:

    def __init__(self):
        self.driver = None
        self.wait = None
        self.config = config_utils.read_base_config_file()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DriverUtils, cls).__new__(cls)
            cls.config = config_utils.read_base_config_file()

        return cls.instance

    def create_driver(self):
        driver_file_path = None
        driver_path = config_utils.get_project_path() + os.sep + 'support' + os.sep + 'driver_executables' + os.sep
        implicit_wait = int(self.config['default_implicit_wait'])
        system = platform.system()

        if self.config['web_browser'].lower() == 'chrome':
            if system.__eq__("Windows"):
                driver_file_path = driver_path + "chromedriver.exe"
            elif system.__eq__("Darwin") or system.__eq__("Linux"):
                driver_file_path = driver_path + "chromedriver_mac64_1" + os.sep + "chromedriver"

            service = Service(executable_path=driver_file_path)
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.implicitly_wait(implicit_wait)
            self.driver.maximize_window()

        return self.driver

    def get_driver_object(self):
        return self.driver

    def set_driver_object(self, driver):
        self.driver = driver

    def teardown_driver(self):
        time.sleep(2)
        self.driver.quit()
        self.driver = None

    def take_screenshot(self):
        image_path = config_utils.get_project_path() + os.sep + "reports" + os.sep + "screenshots" + os.sep
        if not os.path.exists(image_path):
            os.makedirs(image_path)

        image_name = datetime.now().strftime("screenshot_%d%m%Y%H%M%S.png")
        image_file = image_path + image_name
        self.driver.save_screenshot(image_file)
        return image_file

