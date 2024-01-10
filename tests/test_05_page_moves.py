from selene import browser, have, query, be
import requests
from selene.core.wait import Command
import time
from selenium import webdriver

def test_start():
    status = requests.get('http://localhost/theveil/theveil/moves.html').status_code
    if status is 200:
        print('')
        print('Статус код: 200 OK')
        browser.config.timeout = 6
        browser.open("/theveil/moves.html")
    else:
        print('')
        print('Страница не открыта. Код: ', status)
        browser.config.timeout = 0.1

def test_click_on_breadcrumbs():
    print('')
    print('"moves"->"index" через breadcrumbs')
    browser.should(have.url_containing('/theveil/moves.html'))
    browser.element('[class="fa fa-home"]').click()
    browser.should(have.url_containing('/theveil/index.html'))

def scroll(x: int, y: int) -> Command:
    return Command(
        f'scroll page by x {x} y {y}',
        lambda browser: browser.driver.execute_script(
            f'window.scrollBy({x}, {y});'
        )
    )

link = 'C:/_test_screenshots/The_Veil_site_func_tests/test_05_page_moves/'

def test_scroll_down_up():
    print('')
    print('"playbooks":Скроллирование')
    link1 = '01_test_scroll_down_up_'
    browser.open('/theveil/moves.html')
    browser.should(have.url_containing('/theveil/moves.html'))
    browser.perform(scroll(0, 10000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}_1_down.png'))
    browser.perform(scroll(0, -20000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}2_up.png'))
    browser.perform(scroll(1000, 0))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}3_right.png'))
    browser.perform(scroll(-2000, 0))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}4_left.png'))

link2 = '02_test_sector_'
def test_sector_01():
    print('')
    print('"moves":Основные ходы')
    browser.perform(scroll(0,350))
    browser.all('[name="sct_smv"]>div')[0].hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}01_basic_1_hover_sector.png'))
    browser.element('[id="mvs1"]').hover()
    browser.get(query.screenshot_saved(f'{link}{link2}01_basic_2_hover_button.png'))
    browser.element('[id="mvs1"]').should(have.attribute('target','_blank'))
    browser.element('[id="mvs1"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/BASIC_MOVES.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)

def test_sector_02():
    print('')
    print('"moves":Основные ходы')
    browser.all('[name="sct_smv"]>div')[1].hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}02_humanity_1_hover_sector.png'))
    browser.element('[id="mvs2"]').hover()
    browser.get(query.screenshot_saved(f'{link}{link2}02_humanity_2_hover_button.png'))
    browser.element('[id="mvs2"]').should(have.attribute('target','_blank'))
    browser.element('[id="mvs2"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/HUMANITY_HARM.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)

def test_sector_03():
    print('')
    print('"moves":Основные ходы')
    browser.all('[name="sct_smv"]>div')[2].hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}03_setting_1_hover_sector.png'))
    browser.element('[id="mvs3"]').hover()
    browser.get(query.screenshot_saved(f'{link}{link2}03_setting_2_hover_button.png'))
    browser.element('[id="mvs3"]').should(have.attribute('target','_blank'))
    browser.element('[id="mvs3"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/SETTING_PLAYBOOK.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)

def test_download_button():
    print('')
    print('"moves":Кнопка "download"')
    link3 = 'http://localhost/theveil/veil_moves.pdf'
    browser.element('[name="dwn1"]').should(have.attribute('href',link3))
    browser.element('[name="dwn1"]').should(have.attribute('download'))
    browser.element('[name="dwn1"]>img[alt="Скачать буклеты"]').should(be.present)
    driver = webdriver.Chrome()
    driver.get(link3)
    time.sleep(2)
    driver.save_screenshot(f'{link}04_test_download_button_to_url.png')
    driver.close()

def test_up_button():
    print('')
    print('"moves":Кнопка "Наверх"')
    browser.open('/theveil/moves.html')
    browser.should(have.url_containing('/theveil/moves.html'))
    browser.perform(scroll(0, 10000))
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/moves.html#'))
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/moves.html#'))