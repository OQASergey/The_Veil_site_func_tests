from selene import browser, have, query
import requests
from selene.core.wait import Command
import time
from selenium import webdriver

sa = 12 #size of all pics
sl = 9 #size of landscape pics
sc = 7 #size of characters pics
so = 3 #size of other pics

def test_start():
    status = requests.get('http://localhost/theveil/theveil/gallery.html').status_code
    if status == 200:
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

def test_scroll():
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

def test_active_button_all2all():
    print('')
    print('Меню галереи:"all"->"all"')
    browser.perform(scroll(0,-600))
    browser.all('[class ="gallery-controls"]>ul>li')[0].click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.no.css_class("active"))
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}02_test_active_button_all.png'))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))
    # Отображение изображений ("all")
    browser.all('[class="row gallery-filter"]>div').should(have.size(sa))
    browser.all('[class="row gallery-filter"]>[style*="display: none;"]').should(have.size(0))

def test_active_button_all2land():
    print('')
    print('Меню галереи:"all"->"landscape"')
    browser.all('[class ="gallery-controls"]>ul>li')[1].click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.no.css_class("active"))
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}03_test_active_button_land.png'))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))
    # Отображение изображений ("landscape")
    browser.all('[class="row gallery-filter"]>div').should(have.size(sa))
    browser.all('[class="row gallery-filter"]>[class*="landscape"]').should(have.size(sl))
    browser.all('[class="row gallery-filter"]>[class*="landscape"][style*="display: none;"]').should(have.size(0))
    hide = sa - sl
    browser.all('[class="row gallery-filter"]>[style="display: none;"]').should(have.size(hide))

def test_active_button_land2land():
    print('')
    print('Меню галереи:"landscape"->"landscape"')
    browser.all('[class ="gallery-controls"]>ul>li')[1].click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.no.css_class("active"))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))
    # Отображение изображений ("landscape")
    browser.all('[class="row gallery-filter"]>div').should(have.size(sa))
    browser.all('[class="row gallery-filter"]>[class*="landscape"]').should(have.size(sl))
    browser.all('[class="row gallery-filter"]>[class*="landscape"][style*="display: none;"]').should(have.size(0))
    hide = sa - sl
    browser.all('[class="row gallery-filter"]>[style="display: none;"]').should(have.size(hide))

def test_active_button_land2char():
    print('')
    print('Меню галереи:"landscape"->"characters"')
    browser.all('[class ="gallery-controls"]>ul>li')[2].click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.no.css_class("active"))
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}04_test_active_button_char.png'))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))
    # Отображение изображений ("characters")
    browser.all('[class="row gallery-filter"]>div').should(have.size(sa))
    browser.all('[class="row gallery-filter"]>[class*="characters"]').should(have.size(sc))
    browser.all('[class="row gallery-filter"]>[class*="characters"][style*="display: none;"]').should(have.size(0))
    hide = sa - sc
    browser.all('[class="row gallery-filter"]>[style="display: none;"]').should(have.size(hide))

def test_active_button_char2char():
    print('')
    print('Меню галереи:"characters"->"characters"')
    browser.all('[class ="gallery-controls"]>ul>li')[2].click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.no.css_class("active"))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))
    # Отображение изображений ("characters")
    browser.all('[class="row gallery-filter"]>div').should(have.size(sa))
    browser.all('[class="row gallery-filter"]>[class*="characters"]').should(have.size(sc))
    browser.all('[class="row gallery-filter"]>[class*="characters"][style*="display: none;"]').should(have.size(0))
    hide = sa - sc
    browser.all('[class="row gallery-filter"]>[style="display: none;"]').should(have.size(hide))

def test_active_button_char2other():
    print('')
    print('Меню галереи:"characters"->"other"')
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
    # Отображение изображений ("other")
    browser.all('[class="row gallery-filter"]>div').should(have.size(sa))
    browser.all('[class="row gallery-filter"]>[class*="other"]').should(have.size(so))
    browser.all('[class="row gallery-filter"]>[class*="other"][style*="display: none;"]').should(have.size(0))
    hide = sa - so
    browser.all('[class="row gallery-filter"]>[style="display: none;"]').should(have.size(hide))

def test_active_button_other2other():
    print('')
    print('Меню галереи:"other"->"other"')
    browser.all('[class ="gallery-controls"]>ul>li')[3].click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.css_class("active"))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))
    # Отображение изображений ("other")
    browser.all('[class="row gallery-filter"]>div').should(have.size(sa))
    browser.all('[class="row gallery-filter"]>[class*="other"]').should(have.size(so))
    browser.all('[class="row gallery-filter"]>[class*="other"][style*="display: none;"]').should(have.size(0))
    hide = sa - so
    browser.all('[class="row gallery-filter"]>[style="display: none;"]').should(have.size(hide))

def test_active_button_other2all():
    print('')
    print('Меню галереи:"other"->"all"')
    browser.all('[class ="gallery-controls"]>ul>li')[0].click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.no.css_class("active"))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))
    # Отображение изображений ("all")
    browser.all('[class="row gallery-filter"]>div').should(have.size(sa))
    browser.all('[class="row gallery-filter"]>[style*="display: none;"]').should(have.size(0))

def test_active_button_all2char():
    print('')
    print('Меню галереи:"all"->"char"')
    browser.all('[class ="gallery-controls"]>ul>li')[2].click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.no.css_class("active"))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))
    # Отображение изображений ("characters")
    browser.all('[class="row gallery-filter"]>div').should(have.size(sa))
    browser.all('[class="row gallery-filter"]>[class*="characters"]').should(have.size(sc))
    browser.all('[class="row gallery-filter"]>[class*="characters"][style*="display: none;"]').should(have.size(0))
    hide = sa - sc
    browser.all('[class="row gallery-filter"]>[style="display: none;"]').should(have.size(hide))

def test_active_button_char2land():
    print('')
    print('Меню галереи:"char"->"land"')
    browser.all('[class ="gallery-controls"]>ul>li')[1].click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.no.css_class("active"))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))
    # Отображение изображений ("landscape")
    browser.all('[class="row gallery-filter"]>div').should(have.size(sa))
    browser.all('[class="row gallery-filter"]>[class*="landscape"]').should(have.size(sl))
    browser.all('[class="row gallery-filter"]>[class*="landscape"][style*="display: none;"]').should(have.size(0))
    hide = sa - sl
    browser.all('[class="row gallery-filter"]>[style="display: none;"]').should(have.size(hide))

def test_active_button_land2other():
    print('')
    print('Меню галереи:"land"->"other"')
    browser.all('[class ="gallery-controls"]>ul>li')[3].click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.css_class("active"))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))
    # Отображение изображений ("other")
    browser.all('[class="row gallery-filter"]>div').should(have.size(sa))
    browser.all('[class="row gallery-filter"]>[class*="other"]').should(have.size(so))
    browser.all('[class="row gallery-filter"]>[class*="other"][style*="display: none;"]').should(have.size(0))
    hide = sa - so
    browser.all('[class="row gallery-filter"]>[style="display: none;"]').should(have.size(hide))

def test_active_button_other2char():
    print('')
    print('Меню галереи:"other"->"char"')
    browser.all('[class ="gallery-controls"]>ul>li')[2].click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.no.css_class("active"))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))
    # Отображение изображений ("characters")
    browser.all('[class="row gallery-filter"]>div').should(have.size(sa))
    browser.all('[class="row gallery-filter"]>[class*="characters"]').should(have.size(sc))
    browser.all('[class="row gallery-filter"]>[class*="characters"][style*="display: none;"]').should(have.size(0))
    hide = sa - sc
    browser.all('[class="row gallery-filter"]>[style="display: none;"]').should(have.size(hide))

def test_active_button_char2all():
    print('')
    print('Меню галереи:"char"->"all"')
    browser.all('[class ="gallery-controls"]>ul>li')[0].click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.no.css_class("active"))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))
    # Отображение изображений ("all")
    browser.all('[class="row gallery-filter"]>div').should(have.size(sa))
    browser.all('[class="row gallery-filter"]>[style*="display: none;"]').should(have.size(0))

def test_active_button_all2other():
    print('')
    print('Меню галереи:"all"->"other"')
    browser.all('[class ="gallery-controls"]>ul>li')[3].click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.css_class("active"))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))
    # Отображение изображений ("other")
    browser.all('[class="row gallery-filter"]>div').should(have.size(sa))
    browser.all('[class="row gallery-filter"]>[class*="other"]').should(have.size(so))
    browser.all('[class="row gallery-filter"]>[class*="other"][style*="display: none;"]').should(have.size(0))
    hide = sa - so
    browser.all('[class="row gallery-filter"]>[style="display: none;"]').should(have.size(hide))

def test_active_button_other2land():
    print('')
    print('Меню галереи:"other"->"land"')
    browser.all('[class ="gallery-controls"]>ul>li')[1].click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.no.css_class("active"))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))
    # Отображение изображений ("landscape")
    browser.all('[class="row gallery-filter"]>div').should(have.size(sa))
    browser.all('[class="row gallery-filter"]>[class*="landscape"]').should(have.size(sl))
    browser.all('[class="row gallery-filter"]>[class*="landscape"][style*="display: none;"]').should(have.size(0))
    hiden = sa - sl
    browser.all('[class="row gallery-filter"]>[style="display: none;"]').should(have.size(hiden))

def test_active_button_land2all():
    print('')
    print('Меню галереи:"land"->"all"')
    browser.all('[class ="gallery-controls"]>ul>li')[0].click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.no.css_class("active"))
    # Проверка подсветки кнопок главного меню
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))
    # Отображение изображений ("all")
    browser.all('[class="row gallery-filter"]>div').should(have.size(sa))
    browser.all('[class="row gallery-filter"]>[style*="display: none;"]').should(have.size(0))

#TODO0: рандомизаторы от 0 до значений sa, sl, sc и so
#TODO1: проверка открытия рандомного изображения в каждой категории изображений
#TODO2: проверка закрытие изображения на крестик
#TODO3: проверка закрытия изображения на область вне картинки
#TODO4: проверка видео (+ скриншот)
#TODO5: проверка закрытие видео на крестик
#TODO6: проверка закрытия видео на область вне картинки
#TODO7: проверка клика по кнопке "Наверх"

def test_popup_pictures():
    pass




