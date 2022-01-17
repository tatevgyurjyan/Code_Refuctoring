from selenium.webdriver.common.keys import Keys
from Helper import helpers
from Pages import sign_in
from Pages import sign_up
from Pages import search
import conftest
import pytest


@pytest.mark.parametrize("config_name", ['python'])
def test_no_result(driver, config_name):

    conftest.logger("-------test_search_non_existing_course_starts--------")
    helpers.go_to_page(driver, sign_up.data['url'])
    sign_in.login_user(driver)

    helpers.find_and_send_keys(driver, search.search_area, config_name)
    helpers.find_and_send_keys(driver, search.search_area, Keys.ENTER)

    no_result_message = helpers.find(driver, search.no_result_txt)
    assert no_result_message, f"Expected {no_result_message.text} but failed"
    conftest.logger(f"Success! Message {no_result_message.text} is displayed")

    conftest.logger("-------test_search_non_existing_course_finished--------")


if __name__ == '__main__':
    test_no_result(driver, config_name)
