from selene import browser, have, be, query
import requests
from selene.core.wait import Command
import time
from selenium import webdriver

def test_start():
    status = requests.get('http://localhost/theveil/theveil/gallery.html').status_code
    if status is 200:
        print('')
        print('Статус код: 200 OK')
        browser.config.timeout = 6
        browser.open("/theveil/gallery.html")
    else:
        print('')
        print('Страница не открыта. Код: ', status)
        browser.config.timeout = 0.1

def test_click_on_breadcrumbs():
    print('')
    print('"gallery"->"index" через breadcrumbs')
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.element('[class="fa fa-home"]').click()
    browser.should(have.url_containing('/theveil/index.html'))

def scroll(x: int, y: int) -> Command:
    return Command(
        f'scroll page by x {x} y {y}',
        lambda browser: browser.driver.execute_script(
            f'window.scrollBy({x}, {y});'
        )
    )

link = 'C:/_test_screenshots/The_Veil_site_func_tests/test_08_page_gallery/'

def test_scroll_down_up():
    print('')
    print('"gallery":Скроллирование')
    link1 = '01_test_scroll_down_up_'
    browser.open('/theveil/gallery.html')
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.perform(scroll(0, 10000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}1_down.png'))
    browser.perform(scroll(0, -20000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}2_up.png'))
    browser.perform(scroll(0,500))
    time.sleep(0.2)
    browser.get(query.screenshot_saved(f'{link}{link1}3_middle_1.png'))
    browser.perform(scroll(0,500))
    time.sleep(0.2)
    browser.get(query.screenshot_saved(f'{link}{link1}3_middle_2.png'))
    browser.perform(scroll(1000, 0))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}4_right.png'))
    browser.perform(scroll(-2000, 0))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}5_left.png'))
