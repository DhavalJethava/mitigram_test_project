import os
import time

from mains.driver_utils import DriverUtils
from mains.element_helper import ElementHelper
from mains import config_utils
from tests.locators import mitigram_locators

class HomePage:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(HomePage, cls).__new__(cls)
            cls.driver_utils = DriverUtils()
            cls.element_helper = ElementHelper()
            cls.config = config_utils.read_base_config_file()

        return cls.instance

    def open_app_home_page(self):
        if self.driver_utils.get_driver_object() is None:
            self.driver_utils.set_driver_object(self.driver_utils.create_driver())
        self.element_helper.set_driver_object()
        str_url = self.config['website_url']
        self.element_helper.navigate(str_url)

        assert self.element_helper.get_url().__contains__(str_url), \
                    "Failed to open application: " + str_url

    def navigate_to(self, page_name: str):
        str_url = self.config['website_url'] + os.sep + page_name
        self.element_helper.navigate(str_url)


    def login_to_portal(self, user_name: str, password: str):
        self.element_helper.click(mitigram_locators.btn_login)
        if not user_name.__eq__("<BLANK>"):
            self.element_helper.type(mitigram_locators.input_email, user_name)
        if not password.__eq__("<BLANK>"):
            self.element_helper.type(mitigram_locators.input_password, password)
        self.element_helper.click(mitigram_locators.input_login_btn)

    def verify_login_failed(self, noti_msg: str):
        assert self.element_helper.is_element_displayed(mitigram_locators.div_notification),  \
                "Login failure notification is not displayed."

        message = self.element_helper.get_element_text(mitigram_locators.div_notification)

        assert message == noti_msg, \
            "Notification message does not contain expected message. \n" + \
            "Expected: " + noti_msg + "\n" + \
            "Actual: " + message

    def verify_page_title(self, page_title: str):
        title = self.element_helper.get_page_title().strip().lower()
        assert title == page_title.strip().lower(), \
            "Page title is not as per expected. \n" + \
            "Expected: " + page_title + "\n" + \
            "Actual: " + title

    def verify_section_displayed(self, section_name):
        result = False
        if section_name.lower() == "open positions":
            result = self.element_helper.is_element_displayed(mitigram_locators.div_open_positions)

        assert result, section_name + " section is not displayed on page."

    def verify_open_positions(self, dict_open_positions: dict):

        result = False
        lst_open_positions = dict_open_positions.get('open positions')

        for temp in range(lst_open_positions.__len__()):
            lst_open_positions[temp] = lst_open_positions[temp].strip().lower()

        lst_displayed = self.element_helper.get_element_list(mitigram_locators.div_positions)
        assert lst_displayed.__len__() > 0, "No open positions displayed on page."

        lst_displayed_positions = []
        for _position in lst_displayed:
            lst_displayed_positions.append(self.element_helper.get_element_text(_position).strip().lower())

        for _position in lst_open_positions:
            result = _position in lst_displayed_positions

            if not result:
                break

        assert result, "Displayed open positions are not same as expected open positions. \n" + \
            "Expected open positions: " + str(lst_open_positions) + "\n" + \
            "Displayed open positions:" + str(lst_displayed_positions)

    def click_section_under_open_positions(self, section_name):
        self.element_helper.click(mitigram_locators.btn_position_group, section_name)

