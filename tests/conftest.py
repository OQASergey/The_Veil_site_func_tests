import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='module', autouse=True)
def browser_conditions():
    browser.config.driver_name = 'chrome'
    browser.config.timeout = 6
    browser.config.window_width = 1280
    browser.config.window_height = 1024
    driver_options = webdriver.ChromeOptions()
    #driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    browser.config.base_url = "http://localhost/theveil"

    browser.open()
    print('')
    print('**Начало исполнения тестового набора**')

    yield

    browser.quit()
    print('')
    print('**Завершение исполнения тестового набора**')
    print('Скриншоты сохранены: C:/_test_screenshots/The_Veil_site_func_tests/')