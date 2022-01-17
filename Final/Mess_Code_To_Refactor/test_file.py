from selenium.webdriver.common.keys import Keys
import pytest
import json

class Course(driver):

    def registration(driver):
    
        driver.get('https://courses.ultimateqa.com/')
        driver.find_element_by_xpath("//section[@class='header__user-menu']//a[contains(text(), 'Sign In')]").click()
        driver.find_element_by_xpath("//a[contains(text(), 'Create a new account')]").click()
        driver.find_element_by_id("user[first_name]").send_keys("test_name")
        driver.find_element_by_id("user[last_name]").send_keys("test_lastname")
        driver.find_element_by_id("user[email]").send_keys("test125@gmail.com")
        driver.find_element_by_id("user[password]").send_keys("123456789")
        with open('cred.json') as f:
            data = json.load(f)
        data['email'] = "an.harutyunova@gmail"
        data['password'] = "123456789"
        with open('cred.json', 'w') as f:
            json.dump(data, f)
        driver.find_element_by_id("user[terms]").click()
        driver.find_element_by_xpath("// input[ @ value = 'Sign up']").click()


    def test_login(driver):
        with open('cred.json') as f:
            data = json.load(f)
        if data["email"] == '' or data["password"] == '':
            registration(driver)
        else:
            driver.get('https://courses.ultimateqa.com/users/sign_in')
            driver.find_element_by_id("user[email]").send_keys(data["email"])
            driver.find_element_by_id("user[password]").send_keys(data["password"])
            driver.find_element_by_id("user[remember_me]").click()
            driver.find_elements_by_xpath("//input[@type='submit']").click()



# we have to check for 2 data - selenium adn python
    @pytest.mark.parametrize("config_name", ['selenium', 'python'])
    def test_check_title(driver, config_name):
        """1 Go to page
        2. Search Any course
        3. Check searched course in found titles """
        driver.get('https://courses.ultimateqa.com/')
        driver.find_element_by_xpath("//a/img[@title='Ultimate QA']").click()
        driver.find_element_by_xpath("//input[@type='search']").send_keys(config_name)
        item_text_list = []
        page_elements = driver.find_elements_by_xpath(
            "//li[@class='products__list-item']//div[@class='course-card__body']/h3")
        for item in page_elements:
            (item_text_list.append(item.text))
        while len(driver.find_elements_by_xpath("//a[@aria-label='Next page']")) > 0:
            driver.find_element_by_xpath("//a[@aria-label='Next page']").click()
            page_elements = driver.find_elements_by_xpath(
                "//li[@class='products__list-item']//div[@class='course-card__body']/h3")
            for item in page_elements:
                (item_text_list.append(item.text))
            for title in item_text_list:
                assert config_name in title, title


    def test_no_result_case(driver):
        """1. Go to Page
        2. Search not existing course
        3. Verify No Result Found message is visible"""
        driver.get('https://courses.ultimateqa.com/')
        driver.find_element_by_xpath("//a/img[@title='Ultimate QA']").click()
        driver.find_element_by_xpath("//input[@type='search']").send_keys("123")
        driver.find_element_by_xpath("//input[@type='search']").send_keys(Keys.ENTER)
        result = driver.find_elements_by_xpath("//p[contains(@class, 'no-results')]")
        assert len(result) > 0


    def get_page_item_count(driver):
        page_items = len(driver.find_elements_by_xpath(
            "//li[@class='products__list-item']//div[@class='course-card__body']/h3"))
        return page_items


    def get_pagination(driver):
        driver.get('https://courses.ultimateqa.com/')
        driver.find_element_by_xpath("//a/img[@title='Ultimate QA']").click()
        page_items = get_page_item_count(driver)
        assert page_items > 0
        page = 1
        while len(driver.find_elements_by_xpath("//a[@aria-label='Next page']")) > 0:
            driver.find_element_by_xpath("//a[@aria-label='Next page']").click()
            page_items = get_page_item_count(driver)
            page += 1

