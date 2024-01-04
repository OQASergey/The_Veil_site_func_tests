import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='module', autouse=True)
def browser_conditions():
    browser.config.driver_name = 'chrome'
    browser.config.timeout = 3

    driver_options = webdriver.ChromeOptions()
    #driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options

    browser.open()
    print('')
    print('Браузер открыт')
    print('**Начало исполнения тестового набора**')

    yield

    browser.quit()
    print('')
    print('Браузер закрыт')
    print('**Завершение исполнения тестового набора**')