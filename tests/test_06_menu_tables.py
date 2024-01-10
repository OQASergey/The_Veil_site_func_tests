from selene import browser, have, query, be
import requests
from selene.core.wait import Command
import time


def test_start():
    status = requests.get('http://localhost/theveil/theveil/tables_custom.html').status_code
    if status is 200:
        print('')
        print('Статус код: 200 OK')
        browser.config.timeout = 6
        browser.open("/theveil/tables_custom.html")
    else:
        print('')
        print('Код: ', status)
        browser.config.timeout = 0.1

def scroll(x: int, y: int) -> Command:
    return Command(
        f'scroll page by x {x} y {y}',
        lambda browser: browser.driver.execute_script(
            f'window.scrollBy({x}, {y});'
        )
    )

link = 'C:/_test_screenshots/The_Veil_site_func_tests/test_06_menu_tables/'

def test_hover_tables_menu_custom_from_main_menu():
    print('')
    print('Меню таблицы:"main_menu"->"tables_custom":Подсветка разделов при наведении')
    link1 = '00_test_hover_tables_menu_custom_from_main_menu_'
    time.sleep(1)
    browser.perform(scroll(0,350))
    browser.element('[id="cst1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link1}1.png'))
    browser.element('[id="gn1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link1}2.png'))
    browser.element('[id="tch1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link1}3.png'))
    browser.element('[id="crd1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link1}4.png'))

def test_active_button():
    print('')
    print('Меню таблицы:"tables_custom"->"tables_custom"')
    browser.element('[id="cst1"]').click()
    browser.should(have.url_containing('/theveil/tables_custom.html#custom'))
    browser.element('[name="menu1"]>ul>li[class="active"]').should((be.present))
    browser.all('[name="menu1"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[3].should(have.no.css_class("active"))
    #Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.no.css_class("active"))

def test_hover_tables_menu_custom():
    print('')
    print('Меню таблицы:"tables_custom":Подсветка разделов при наведении')
    link1 = '01_test_hover_tables_menu_custom_'
    browser.element('[id="cst1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link1}1.png'))
    browser.element('[id="gn1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link1}2.png'))
    browser.element('[id="tch1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link1}3.png'))
    browser.element('[id="crd1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link1}4.png'))

def test_click_on_menu_gun():
    print('')
    print('Меню таблицы:"tables_custom"->"tables_gun"')
    browser.element('[id="gn1"]').click()
    browser.should(have.url_containing('/theveil/tables_gun.html#gun'))
    browser.all('[name="menu1"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[1].should(have.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[3].should(have.no.css_class("active"))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.no.css_class("active"))

def test_hover_tables_menu_gun():
    print('')
    print('Меню таблицы:"tables_gun":Подсветка разделов при наведении')
    link2 = '02_test_hover_tables_menu_gun_'
    browser.element('[id="cst1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}1.png'))
    browser.element('[id="gn1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}2.png'))
    browser.element('[id="tch1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}3.png'))
    browser.element('[id="crd1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}4.png'))

def test_click_on_menu_tech():
    print('')
    print('Меню таблицы:"tables_custom"->"tables_tech"')
    browser.element('[id="cst1"]').click()
    browser.should(have.url_containing('/theveil/tables_custom.html#custom'))
    browser.element('[id="tch1"]').click()
    browser.should(have.url_containing('/theveil/tables_tech.html#tech'))
    browser.all('[name="menu1"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[2].should(have.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[3].should(have.no.css_class("active"))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.no.css_class("active"))

def test_hover_tables_menu_tech():
    print('')
    print('Меню таблицы:"tables_tech":Подсветка разделов при наведении')
    link2 = '03_test_hover_tables_menu_tech_'
    browser.element('[id="cst1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}1.png'))
    browser.element('[id="gn1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}2.png'))
    browser.element('[id="tch1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}3.png'))
    browser.element('[id="crd1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}4.png'))

def test_click_on_menu_cred():
    print('')
    print('Меню таблицы:"tables_custom"->"tables_cred"')
    browser.element('[id="cst1"]').click()
    browser.should(have.url_containing('/theveil/tables_custom.html#custom'))
    browser.element('[id="crd1"]').click()
    browser.should(have.url_containing('/theveil/tables_cred.html#cred'))
    browser.all('[name="menu1"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[3].should(have.css_class("active"))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.no.css_class("active"))

def test_hover_tables_menu_cred():
    print('')
    print('Меню таблицы:"tables_cred":Подсветка разделов при наведении')
    browser.open('/theveil/tables_cred.html#cred')
    link2 = '04_test_hover_tables_menu_cred_'
    browser.element('[id="cst1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}1.png'))
    browser.element('[id="gn1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}2.png'))
    browser.element('[id="tch1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}3.png'))
    browser.element('[id="crd1"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}4.png'))

def test_cross_click_on_tables_menu():
    print('')
    print('Меню таблицы:Кросс-переходы')
    browser.element('[id="cst1"]').click()
    browser.should(have.url_containing('/theveil/tables_custom.html#custom'))
    browser.open('/theveil/tables_gun.html#gun')
    browser.element('[id="gn1"]').click()
    browser.should(have.url_containing('/theveil/tables_gun.html#gun'))
    browser.all('[name="menu1"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[1].should(have.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[3].should(have.no.css_class("active"))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.no.css_class("active"))
    browser.element('[id="tch1"]').click()
    browser.should(have.url_containing('/theveil/tables_tech.html#tech'))
    browser.element('[id="tch1"]').click()
    browser.should(have.url_containing('/theveil/tables_tech.html#tech'))
    browser.all('[name="menu1"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[2].should(have.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[3].should(have.no.css_class("active"))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.no.css_class("active"))
    browser.element('[id="crd1"]').click()
    browser.should(have.url_containing('/theveil/tables_cred.html#cred'))
    browser.element('[id="crd1"]').click()
    browser.should(have.url_containing('/theveil/tables_cred.html#cred'))
    browser.all('[name="menu1"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[name="menu1"]>ul>li')[3].should(have.css_class("active"))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.no.css_class("active"))
    browser.element('[id="gn1"]').click()
    browser.should(have.url_containing('/theveil/tables_gun.html#gun'))
    browser.element('[id="crd1"]').click()
    browser.should(have.url_containing('/theveil/tables_cred.html#cred'))
    browser.element('[id="tch1"]').click()
    browser.should(have.url_containing('/theveil/tables_tech.html#tech'))
    browser.element('[id="gn1"]').click()
    browser.should(have.url_containing('/theveil/tables_gun.html#gun'))
