from selenium.webdriver.common.by import By


search_area = (By.XPATH, "//input[@name='q']")
page_content = (
    By.XPATH, "//li[@class='products__list-item']//div[@class='course-card__body']/h3")
no_result_txt = (By.XPATH, "//p[contains(@class, 'no-results')]")
