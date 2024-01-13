from selene import browser, have, query, be
import requests
from selene.core.wait import Command
import time
import random

sa = 12 #size of all pics
sl = 9 #size of landscape pics
sc = 7 #size of characters pics
so = 3 #size of other pics
def pic_number(a, b):
    return random.randint(a, b)

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
    browser.open('/theveil/gallery.html#gallery')
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
    browser.all('[class="row gallery-filter"]>[class*="landscape"][style*="display: none;"]').should(
        have.size(0)
    )
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
    browser.all('[class="row gallery-filter"]>[class*="landscape"][style*="display: none;"]').should(
        have.size(0)
    )
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
    browser.all('[class="row gallery-filter"]>[class*="characters"][style*="display: none;"]').should(
        have.size(0)
    )
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
    browser.all('[class="row gallery-filter"]>[class*="characters"][style*="display: none;"]').should(
        have.size(0)
    )
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
    browser.all('[class="row gallery-filter"]>[class*="other"][style*="display: none;"]').should(
        have.size(0)
    )
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
    browser.all('[class="row gallery-filter"]>[class*="other"][style*="display: none;"]').should(
        have.size(0)
    )
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
    browser.all('[class="row gallery-filter"]>[class*="characters"][style*="display: none;"]').should(
        have.size(0)
    )
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
    browser.all('[class="row gallery-filter"]>[class*="landscape"][style*="display: none;"]').should(
        have.size(0)
    )
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
    browser.all('[class="row gallery-filter"]>[class*="other"][style*="display: none;"]').should(
        have.size(0)
    )
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
    browser.all('[class="row gallery-filter"]>[class*="characters"][style*="display: none;"]').should(
        have.size(0)
    )
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
    browser.all('[class="row gallery-filter"]>[class*="other"][style*="display: none;"]').should(
        have.size(0)
    )
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
    browser.all('[class="row gallery-filter"]>[class*="landscape"][style*="display: none;"]').should(
        have.size(0)
    )
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

def test_popup_pictures_all():
    print('')
    print('"gallery":Изображения:"all":Pop-up')
    link3 = '06_test_popup_pictures_all_'
    browser.open('/theveil/gallery.html')
    browser.open('/theveil/gallery.html#gallery')
    browser.all('[class ="gallery-controls"]>ul>li')[0].click()
    # Проверка наведения и открытия на первые 6 изображений (для удобного отображения на скриншоте)
    randsix = pic_number(0,5)
    time.sleep(1.5)
    browser.all('[id="pic"]')[randsix].hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link3}1_hover_pic_area_randsix(номер_картинки#{randsix+1}).png'))
    browser.all('[class="gi-hover"]')[randsix].element('[class="image-popup"]').should(have.attribute
        ('href',f'http://localhost/theveil/theveil/img/gallery/gallery-{randsix+1}.jpg')
    )
    browser.all('[class="gi-hover"]')[randsix].element('[class="image-popup"]').click()
    browser.element('[class="mfp-figure"]').should(be.present)
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}{link3}2_popup_pic_randsix(номер_картинки#{randsix+1}).png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-figure"]').should(be.absent)
    # Проверка открытия другого случайного изображения
    randall = pic_number(0,sa-1)
    while randall == randsix:
         randall = pic_number(0,sa-1)
    browser.all('[id="pic"]')[randall].hover()
    time.sleep(1)
    browser.all('[class="gi-hover"]')[randall].element('[class="image-popup"]').click()
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}{link3}3_popup_pic_randall(номер_картинки#{randall+1}).png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-figure"]').should(be.absent)

def test_popup_pictures_land():
    print('')
    print('"gallery":Изображения:"landscape":Pop-up')
    link3 = '07_test_popup_pictures_land_'
    browser.open('/theveil/gallery.html')
    browser.open('/theveil/gallery.html#gallery')
    browser.all('[class ="gallery-controls"]>ul>li')[1].click()
    # Проверка наведения и открытия на первые 6 изображений (для удобста отображения на скриншоте)
    randsix = pic_number(0,5)
    time.sleep(1.5)
    browser.all('[class*="landscape"]')[randsix].element('[id="pic"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link3}1_hover_pic_area_randsix(номер_картинки#{randsix+1}).png'))
    browser.all('[class*="landscape"]')[randsix].element('[class="image-popup"]').click()
    browser.element('[class="mfp-figure"]').should(be.present)
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}{link3}2_popup_pic_randsix(номер_картинки#{randsix+1}).png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-figure"]').should(be.absent)
    # Проверка открытия изображения вне визуального отображения
    randall = pic_number(0, sl-1)
    while randall == randsix:
        randall = pic_number(0,sl-1)
    browser.all('[class*="landscape"]')[randall].element('[id="pic"]').hover()
    time.sleep(1)
    browser.all('[class*="landscape"]')[randall].element('[class="image-popup"]').click()
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}{link3}3_popup_pic_randall(номер_картинки#{randall+1}).png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-figure"]').should(be.absent)

def test_popup_pictures_char():
    print('')
    print('"gallery":Изображения:"characters":Pop-up')
    link3 = '08_test_popup_pictures_char_'
    browser.open('/theveil/gallery.html')
    browser.open('/theveil/gallery.html#gallery')
    browser.all('[class ="gallery-controls"]>ul>li')[2].click()
    time.sleep(1.5)
    randsix = pic_number(0,5)
    browser.all('[class*="characters"]')[randsix].element('[id="pic"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link3}1_hover_pic_area_randsix(номер_картинки#{randsix+1}).png'))
    browser.all('[class*="characters"]')[randsix].element('[class="image-popup"]').click()
    browser.element('[class="mfp-figure"]').should(be.present)
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}{link3}2_popup_pic_randsix(номер_картинки#{randsix+1}).png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-figure"]').should(be.absent)
    randall = pic_number(0,sc-1)
    while randall == randsix:
        randall = pic_number(0,sc-1)
    browser.all('[class*="characters"]')[randall].element('[id="pic"]').hover()
    time.sleep(1)
    browser.all('[class*="characters"]')[randall].element('[class="image-popup"]').click()
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}{link3}3_popup_pic_randall(номер_картинки#{randall+1}).png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-figure"]').should(be.absent)

def test_popup_pictures_other():
    print('')
    print('"gallery":Изображения:"other":Pop-up')
    link3 = '09_test_popup_pictures_other_'
    browser.open('/theveil/gallery.html')
    browser.open('/theveil/gallery.html#gallery')
    browser.all('[class ="gallery-controls"]>ul>li')[3].click()
    rand = pic_number(0,so-1)
    time.sleep(1.5)
    browser.all('[class*="other"]')[rand].element('[id="pic"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link3}1_hover_pic_area(номер_картинки#{rand+1}).png'))
    browser.all('[class*="other"]')[rand].element('[class="image-popup"]').click()
    browser.element('[class="mfp-figure"]').should(be.present)
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}{link3}2_popup_pic(номер_картинки#{rand+1}).png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-figure"]').should(be.absent)

def test_video():
    print('')
    print('"gallery":Видео"')
    browser.element('[class="mfp-iframe"]').should(be.absent)
    browser.element('[class="play-btn video-popup"]').click()
    time.sleep(1)
    browser.element('[class="mfp-iframe"]').should(
        have.attribute('src','http://www.youtube.com/embed/NjlGjkAFD2w?autoplay=1')
    )
    time.sleep(2)
    browser.get(query.screenshot_saved(f'{link}10_test_video.png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-iframe"]').should(be.absent)

def test_up_button_gallery():
    print('')
    print('"gallery":Кнопка "Наверх"')
    browser.perform(scroll(0, 10000))
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/gallery.html#'))
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/gallery.html#'))

#TODO1: проверка закрытия изображения на область вне картинки
#TODO2: проверка закрытия видео на область вне картинки