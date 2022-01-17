from selenium.webdriver.common.keys import Keys
from Helper import helpers
from Pages import sign_up
from Pages import sign_in
from Pages import search
import conftest
import pytest
import time


@pytest.mark.parametrize("config_name", ['SELENIUM'])
def test_check_title(driver, config_name):

    conftest.logger("-------test_search_existing_course_starts---------")
    helpers.go_to_page(driver, sign_up.data['url'])
    sign_in.login_user(driver)

    helpers.find_and_send_keys(driver, search.search_area, config_name)
    helpers.find_and_send_keys(driver, search.search_area, Keys.ENTER)
    time.sleep(1)

    for handle in driver.window_handles:
        driver.switch_to.window(handle)
    page_items = helpers.find_all(driver, search.page_content)

    courses = []
    for link in page_items:
        course = link.text
        courses.append(course)
    conftest.logger(courses)

    for title in courses:
        assert config_name in title, f"Excpected all to contain {config_name}"

    conftest.logger("-------test_search_existing_course_finished------------")


if __name__ == '__main__':
    test_check_title(driver, config_name)
