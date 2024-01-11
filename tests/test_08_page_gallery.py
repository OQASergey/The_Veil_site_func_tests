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

def test_active_button_allpics():
    print('')
    print('Меню галереи:"All"->"All"')
    browser.perform(scroll(0,-600))
    browser.all('[class ="gallery-controls"]>ul>li')[0].click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.no.css_class("active"))
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}02_test_active_button_allpics.png'))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))

def test_active_button_landscape():
    print('')
    print('Меню галереи:"All"->"landscape"')
    browser.all('[class ="gallery-controls"]>ul>li')[1].click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.no.css_class("active"))
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}03_test_active_button_landscape.png'))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))

def test_active_button_characters():
    print('')
    print('Меню галереи:"All"->"characters"')
    browser.all('[class ="gallery-controls"]>ul>li')[2].click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.no.css_class("active"))
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}04_test_active_button_characters.png'))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))

def test_active_button_other():
    print('')
    print('Меню галереи:"All"->"other"')
    browser.all('[class ="gallery-controls"]>ul>li')[3].click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.css_class("active"))
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}05_test_active_button_other.png'))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))