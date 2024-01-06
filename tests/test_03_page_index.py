from selene import browser, have, query, be
import requests
from selene.core.wait import Command
import time

response = requests.get('http://localhost/theveil/theveil/')
status = response.status_code
link = 'C:/_test_screenshots/The_Veil_site_func_tests/test_03_page_index/'

def scroll(x: int, y: int) -> Command:
    return Command(
        f'scroll page by x {x} y {y}',
        lambda browser: browser.driver.execute_script(
            f'window.scrollBy({x}, {y});'
        )
    )

def test_start():
    browser.open("/theveil/")
    print('')
    print('"index":Загрузка страницы')
    if status is 200:
        print('Статус код: ', status, ' OK')
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()

def test_click_on_sectors():
    print('')
    print('"index":Переходы через кнопки разделов')
    browser.element('[class="primary-btn class-btn"][id="plb1"]').click()
    browser.should(have.url_containing('/theveil/playbooks.html'))
    browser.open('/theveil/index.html')
    browser.element('[class="primary-btn class-btn"][id="mvs1"]').click()
    browser.should(have.url_containing('/theveil/moves.html'))
    browser.open('/theveil/')
    browser.element('[class="primary-btn class-btn"][id="tbl1"]').click()
    browser.should(have.url_containing('/theveil/tables_custom.html'))
    browser.open('/theveil/index.html')
    browser.element('[class="primary-btn class-btn"][id="glr1"]').click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.open('/theveil/')

def test_scroll_down_up():
    print('')
    print('"index":Скролл вниз на 10 000 px')
    browser.perform(scroll(0, 10000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}test_scroll_down_up_1_down.png'))
    print('"index":Скролл вверх на 20 000 px')
    browser.perform(scroll(0, -20000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}test_scroll_down_up_2_up.png'))
    print('"index":Скролл вправа на 1 000 px')
    browser.perform(scroll(1000, 0))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}test_scroll_down_up_3_right.png'))
    print('"index":Скролл влево на 2 000 px')
    browser.perform(scroll(-2000, 0))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}test_scroll_down_up_4_left.png'))

def test_up_buton():
    print('')
    print('"index":Клик на кнопку "Наверх"')
    browser.perform(scroll(0, 10000))
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/#'))
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/#'))
