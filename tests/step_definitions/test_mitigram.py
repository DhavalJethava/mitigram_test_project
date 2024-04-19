import os

import pytest
from pytest_bdd import scenario, given, when, then, parsers
from tests.page_objects.home_page import HomePage
from support import support_utils


@pytest.fixture()
def obj_home_page():
    return HomePage()


@scenario('..' + os.sep + 'features' + os.sep + 'mitigram_tests.feature',
          'Invalid login attempt to the portal')
def test_invalid_login():
    print('Invalid login attempt to the portal')


@scenario('..' + os.sep + 'features' + os.sep + 'mitigram_tests.feature',
          'Verify careers page displayed')
def test_verify_careers_page():
    print("Verify careers page displayed")


@scenario('..' + os.sep + 'features' + os.sep + 'mitigram_tests.feature',
          'Verify different open positions')
def test_verify_open_positions():
    print("Verify different open positions")


@given("User is on the application home page")
@when("User is on the application home page")
def open_app_home_page(obj_home_page):
    obj_home_page.open_app_home_page()


@when(parsers.cfparse('User navigates to the "{page_name}" page'))
def navigate_to_page(obj_home_page, page_name: str):
    obj_home_page.navigate_to(page_name)


@then(parsers.cfparse('User should see the page title as "{page_title}"'))
def verify_page_title(obj_home_page, page_title: str):
    obj_home_page.verify_page_title(page_title)


@then(parsers.cfparse('User should see "{section_name}" section displayed'))
def verify_section_displayed(obj_home_page, section_name: str):
    obj_home_page.verify_section_displayed(section_name)


@when(parsers.cfparse('User performs login with "{user_name}" and "{password}"'))
def login_to_portal(obj_home_page, user_name: str, password: str):
    obj_home_page.login_to_portal(user_name, password)


@then(parsers.cfparse('Login attempt should fail with the message "{notification}"'))
def verify_login_failed(obj_home_page, notification: str):
    obj_home_page.verify_login_failed(notification)


@then(parsers.cfparse('User should see the following open positions:\n{open_positions}'))
def verify_open_positions(obj_home_page, open_positions):
    dict_open_positions = support_utils.parse_str_table(open_positions)
    obj_home_page.verify_open_positions(dict_open_positions)


@when(parsers.cfparse('User click on "{section_name}" section under open positions'))
def click_section_under_open_positions(obj_home_page, section_name: str):
    obj_home_page.click_section_under_open_positions(section_name)

