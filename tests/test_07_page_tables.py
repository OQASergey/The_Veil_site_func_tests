from selene import browser, have, query, be
import requests
from selene.core.wait import Command
import time

def test_start():
    status = requests.get('http://localhost/theveil/theveil/tables_custom.html').status_code
    if status == 200:
        print('')
        print('Статус код: 200 OK')
        browser.config.timeout = 6
        browser.open("/theveil/tables_custom.html")
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

link = 'C:/_test_screenshots/The_Veil_site_func_tests/test_07_page_tables/'

def test_scroll_custom():
    print('')
    print('"tables_custom":Скроллирование')
    link1 = '01_test_scroll_down_up_custom_'
    browser.open('/theveil/tables_custom.html')
    browser.should(have.url_containing('/theveil/tables_custom.html'))
    browser.perform(scroll(0, 10000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}1_down.png'))
    browser.perform(scroll(0, -20000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}2_up.png'))
    browser.perform(scroll(0,400))
    time.sleep(0.2)
    browser.get(query.screenshot_saved(f'{link}{link1}3_middle.png'))
    browser.perform(scroll(1000, 0))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}4_right.png'))
    browser.perform(scroll(-2000, 0))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}5_left.png'))

def test_tables_custom():
    print('')
    print('"tables_custom":Структура таблицы "custom"')
    browser.all('[class="classtime-table"]>table').should(have.size(5))
    browser.all('[id="tbl2_1"]>tr').should(have.size(4))
    browser.all('[id="tbl2_2"]>tr').should(have.size(6))
    browser.all('[id="tbl2_3"]>a')[0].click()
    browser.should(have.url_containing('/theveil/tables_gun.html#gun'))
    browser.open('/theveil/tables_custom.html#custom')
    browser.should(have.url_containing('/theveil/tables_custom.html#custom'))
    browser.all('[id="tbl2_3"]>a')[1].click()
    browser.should(have.url_containing('/theveil/tables_tech.html#tech'))
    browser.open('/theveil/tables_custom.html#custom')
    browser.should(have.url_containing('/theveil/tables_custom.html#custom'))

def test_up_button_custom():
    print('')
    print('"tables_custom":Кнопка "Наверх"')
    browser.perform(scroll(0, 10000))
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/tables_custom.html#'))
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/tables_custom.html#'))

def test_click_on_breadcrumbs_custom():
    print('')
    print('"tables_custom#"->"index" через breadcrumbs')
    browser.should(have.url_containing('/theveil/tables_custom.html#'))
    browser.element('[class="fa fa-home"]').click()
    browser.should(have.url_containing('/theveil/index.html'))

def test_scroll_gun():
    print('')
    print('"tables_gun":Скроллирование')
    link1 = '02_test_scroll_down_up_gun_'
    browser.open('/theveil/tables_gun.html#gun')
    browser.should(have.url_containing('/theveil/tables_gun.html#gun'))
    browser.perform(scroll(0, 10000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}1_down.png'))
    browser.perform(scroll(0, -20000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}2_up.png'))
    browser.perform(scroll(0,400))
    time.sleep(0.2)
    browser.get(query.screenshot_saved(f'{link}{link1}3_middle.png'))
    browser.perform(scroll(1000, 0))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}4_right.png'))
    browser.perform(scroll(-2000, 0))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}5_left.png'))

def test_tables_gun():
    print('')
    print('"tables_gun":Структура таблицы "gun"')
    browser.all('[class="classtime-table"]>table').should(have.size(4))
    browser.all('[id="tbl2_1"]>tr').should(have.size(13))
    browser.all('[id="tbl2_2"]>tr').should(have.size(4))

def test_up_button_gun():
    print('')
    print('"tables_gun":Кнопка "Наверх"')
    browser.perform(scroll(0, 10000))
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/tables_gun.html#'))
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/tables_gun.html#'))

def test_click_on_breadcrumbs_gun():
    print('')
    print('"tables_gun#"->"index" через breadcrumbs')
    browser.should(have.url_containing('/theveil/tables_gun.html#'))
    browser.element('[class="fa fa-home"]').click()
    browser.should(have.url_containing('/theveil/index.html'))

def test_scroll_tech():
    print('')
    print('"tables_tech":Скроллирование')
    link1 = '03_test_scroll_down_up_tech_'
    browser.open('/theveil/tables_tech.html#tech')
    browser.should(have.url_containing('/theveil/tables_tech.html#tech'))
    browser.perform(scroll(0, 10000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}1_down.png'))
    browser.perform(scroll(0, -20000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}2_up.png'))
    browser.perform(scroll(0,800))
    time.sleep(0.2)
    browser.get(query.screenshot_saved(f'{link}{link1}3_middle.png'))
    browser.perform(scroll(1000, 0))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}4_right.png'))
    browser.perform(scroll(-2000, 0))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}5_left.png'))

def test_tables_tech():
    print('')
    print('"tables_tech":Структура таблицы "tech"')
    browser.all('[class="classtime-table"]>table').should(have.size(4))
    browser.all('[id="tbl2_1"]>tr').should(have.size(26))
    browser.all('[id="tbl2_2"]>tr').should(have.size(6))

def test_up_button_tech():
    print('')
    print('"tables_tech":Кнопка "Наверх"')
    browser.perform(scroll(0, 10000))
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/tables_tech.html#'))
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/tables_tech.html#'))

def test_click_on_breadcrumbs_tech():
    print('')
    print('"tables_tech#"->"index" через breadcrumbs')
    browser.should(have.url_containing('/theveil/tables_tech.html#'))
    browser.element('[class="fa fa-home"]').click()
    browser.should(have.url_containing('/theveil/index.html'))

def test_scroll_cred():
    print('')
    print('"tables_cred":Скроллирование')
    link1 = '04_test_scroll_down_up_cred_'
    browser.open('/theveil/tables_cred.html#cred')
    browser.should(have.url_containing('/theveil/tables_cred.html#cred'))
    browser.perform(scroll(0, 10000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}1_down.png'))
    browser.perform(scroll(0, -20000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}2_up.png'))
    browser.perform(scroll(1000, 0))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}3_right.png'))
    browser.perform(scroll(-2000, 0))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}4_left.png'))

def test_tables_cred():
    print('')
    print('"tables_cred":Структура таблицы "cred"')
    browser.all('[class="classtime-table"]>table>thead').should(have.size(3))
    browser.all('[class="classtime-table"]>table>tbody').should(have.size(3))
    browser.all('[id="tbl2_1"]>tr').should(have.size(4))
    browser.all('[id="tbl2_2"]>tr').should(have.size(5))
    browser.all('[id="tbl2_3"]>tr').should(have.size(4))

def test_up_button_cred():
    print('')
    print('"tables_cred":Кнопка "Наверх"')
    browser.perform(scroll(0, 10000))
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/tables_cred.html#'))
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/tables_cred.html#'))

def test_click_on_breadcrumbs_cred():
    print('')
    print('"tables_cred#"->"index" через breadcrumbs')
    browser.should(have.url_containing('/theveil/tables_cred.html#'))
    browser.element('[class="fa fa-home"]').click()
    browser.should(have.url_containing('/theveil/index.html'))