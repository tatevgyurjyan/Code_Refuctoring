from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import conftest
import string
import random


def go_to_page(driver, url, new_window=False):
    if new_window:
        driver.execute_script(f"window.open('{url}')")
    else:
        driver.get(url)
        driver.maximize_window()


def find_and_click(driver, loc, timeout=3):
    try:
        elem = find(driver, loc, timeout)
        elem.click()
        conftest.logger("The element was successfully found and clicked")
    except Exception as e:
        conftest.logger(e, True)


def find_and_send_keys(driver, loc, inp_text, timeout=3, click=False):
    try:
        elem = find(driver, loc, timeout)
        if click:
            elem.send_keys(inp_text, Keys.ENTER)
        else:
            elem.send_keys(inp_text)
        conftest.logger("The data was successfully sent")
    except Exception as e:
        conftest.logger(e, True)


def find(driver, loc, timeout=3, get_text="", get_attribute=""):
    try:
        elem = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(loc))
        conftest.logger("The element was successfully presented")
        if get_text:
            return elem.text
        elif get_attribute:
            return elem.get_attribute(get_attribute)
        return elem
    except Exception as e:
        conftest.logger(e, True)


def find_all(driver, loc, timeout=10):
    try:
        elements = WebDriverWait(driver, timeout).until(
                                EC.presence_of_all_elements_located(loc),
                                message=f"Elements '{loc}' not found!")
    except Exception as e:
        conftest.logger(e, True)
        return False
    return elements


def email_generator(driver):
    try:
        email_providers = ["gmail", "yahoo", "mail", "hotmail"]
        domains = [".com", ".de", ".ru", ".org", ".net"]
        str_email_name = "".join([string.ascii_letters, string.digits])
        email_address = "".join(random.choices(str_email_name, k=10)) + \
            "@" + random.choice(email_providers) + random.choice(domains)
        return email_address
    except Exception as e:
        conftest.logger(e, True)


def password_generator(driver):
    try:
        str_password = "".join(
            [string.ascii_letters, string.digits, '!', '.', '$', '&', '#'])
        my_password = "".join(random.choices(str_password, k=10))
        return my_password
    except Exception as e:
        conftest.logger(e, True)
