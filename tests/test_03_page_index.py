from selene import browser, have, query
import requests
from selene.core.wait import Command
import time

def test_start():
    status = requests.get('http://localhost/theveil/theveil/').status_code
    if status is 200:
        print('')
        print('Статус код: 200 OK')
        browser.config.timeout = 6
        browser.open("/theveil/")
    else:
        print('')
        print('Страница не открыта. Код: ', status)
        browser.config.timeout = 0.1

def scroll(x: int, y: int) -> Command:
    return Command(
        f'scroll page by x {x} y {y}',
        lambda browser: browser.driver.execute_script(
            f'window.scrollBy({x}, {y});'
        )
    )

link = 'C:/_test_screenshots/The_Veil_site_func_tests/test_03_page_index/'

def test_scroll_down_up():
    print('')
    print('"index":Скролл вниз на 10 000 px')
    browser.should(have.url_containing('/theveil/'))
    browser.perform(scroll(0, 10000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}01_test_scroll_down_up_1_down.png'))
    print('"index":Скролл вверх на 20 000 px')
    browser.perform(scroll(0, -20000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}01_test_scroll_down_up_2_up.png'))
    print('"index":Скролл вправа на 1 000 px')
    browser.perform(scroll(1000, 0))
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}01_test_scroll_down_up_3_right.png'))
    print('"index":Скролл влево на 2 000 px')
    browser.perform(scroll(-2000, 0))
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}01_test_scroll_down_up_4_left.png'))

def test_sector_01():
    print('')
    print('"index":Раздел 1')
    browser.perform(scroll(0,450))
    browser.all('[name="sctr"]>div')[0].hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}02_test_sector_1_hover_sector.png'))
    browser.element('[id="plb1"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}02_test_sector_2_hover_button.png'))
    browser.element('[class="primary-btn class-btn"][id="plb1"]').click()
    browser.should(have.url_containing('/theveil/playbooks.html'))

def test_sector_02():
    print('')
    print('"index":Раздел 2')
    browser.open('/theveil/')
    browser.should(have.url_containing('/theveil/'))
    browser.perform(scroll(0,450))
    browser.all('[name="sctr"]>div')[1].hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}03_test_sector_1_hover_sector.png'))
    browser.element('[id="mvs1"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}03_test_sector_2_hover_button.png'))
    browser.element('[class="primary-btn class-btn"][id="mvs1"]').click()
    browser.should(have.url_containing('/theveil/moves.html'))

def test_sector_03():
    print('')
    print('"index":Раздел 3')
    browser.open('/theveil/')
    browser.should(have.url_containing('/theveil/'))
    browser.perform(scroll(0,450))
    browser.all('[name="sctr"]>div')[2].hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}04_test_sector_1_hover_sector.png'))
    browser.element('[id="tbl1"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}04_test_sector_2_hover_button.png'))
    browser.element('[class="primary-btn class-btn"][id="tbl1"]').click()
    browser.should(have.url_containing('/theveil/tables_custom.html'))

def test_sector_04():
    print('')
    print('"index":Раздел 4')
    browser.open('/theveil/')
    browser.should(have.url_containing('/theveil/'))
    browser.perform(scroll(0,450))
    browser.all('[name="sctr"]>div')[3].hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}05_test_sector_1_hover_sector.png'))
    browser.element('[id="glr1"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}05_test_sector_2_hover_button.png'))
    browser.element('[class="primary-btn class-btn"][id="glr1"]').click()
    browser.should(have.url_containing('/theveil/gallery.html'))

def test_up_button():
    print('')
    print('"index":Кнопка "Наверх"')
    browser.open('/theveil/')
    browser.should(have.url_containing('/theveil/'))
    browser.perform(scroll(0, 10000))
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/#'))
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/#'))
