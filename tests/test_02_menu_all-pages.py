from selene import browser, have, be, query
import requests
import time

def test_start():
    response = requests.get('http://localhost/theveil/theveil/')
    status = response.status_code
    browser.open("/theveil/")
    print('')
    print('Главное меню:Загрузка страницы')
    if status is 200:
        print('Статус код: ', status, ' OK')
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()

def test_active_button():
    print('')
    print('Главное меню:Дефолтная подсветка разделов')
    browser.element('[class="mainmenu mobile-menu"]>ul>li[class="active"]').should(be.present)
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[4].should(have.no.css_class("active"))

link = 'C:/_test_screenshots/The_Veil_site_func_tests/test_02_menu_all-pages/'

def test_hover_buttons_index():
    print('')
    print('Главное меню:"index":Подсветка разделов при наведении')
    link1 = '01_test_hover_buttons_index_'
    browser.element('[id="ind0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link1}1.png'))
    browser.element('[id="plb0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link1}2.png'))
    browser.element('[id="mvs0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link1}3.png'))
    browser.element('[id="tbl0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link1}4.png'))
    browser.element('[id="glr0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link1}5.png'))

def test_click_on_menu_ind():
    print('')
    print('Главное меню:"index"->"index"')
    browser.element('[id="ind0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/index.html'))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[0].should(have.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[4].should(have.no.css_class("active"))

def test_click_on_menu_plb():
    print('')
    print('Главное меню:"index"->"playbooks"')
    browser.element('[id="plb0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/playbooks.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/playbooks.html'))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[1].should(have.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[4].should(have.no.css_class("active"))

def test_hover_buttons_playbooks():
    print('')
    print('Главное меню:"playbooks":Подсветка разделов при наведении')
    link2 = '02_test_hover_buttons_playbooks_'
    browser.element('[id="ind0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}1.png'))
    browser.element('[id="plb0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}2.png'))
    browser.element('[id="mvs0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}3.png'))
    browser.element('[id="tbl0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}4.png'))
    browser.element('[id="glr0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}5.png'))
    browser.element('[id="ind0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/index.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/index.html'))

def test_click_on_menu_mvs():
    print('')
    print('Главное меню:"index"->"moves"')
    browser.element('[id="mvs0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/moves.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/moves.html'))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[2].should(have.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[4].should(have.no.css_class("active"))

def test_hover_buttons_moves():
    print('')
    print('Главное меню:"moves":Подсветка разделов при наведении')
    link3 = '03_test_hover_buttons_moves_'
    browser.element('[id="ind0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link3}1.png'))
    browser.element('[id="plb0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link3}2.png'))
    browser.element('[id="mvs0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link3}3.png'))
    browser.element('[id="tbl0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link3}4.png'))
    browser.element('[id="glr0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link3}5.png'))
    browser.element('[id="ind0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/index.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/index.html'))


def test_click_on_menu_tbl():
    print('')
    print('Главное меню:"index"->"tables_custom"')
    browser.element('[id="tbl0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/tables_custom.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/tables_custom.html'))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.no.css_class("active"))
    #Проверка подсветки кнопок меню таблицы
    browser.all('[class="mainmenu mobile-menu"][name=menu1]>ul>li')[0].should(have.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu1]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu1]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu1]>ul>li')[3].should(have.no.css_class("active"))

def test_hover_buttons_tables_custom():
    print('')
    print('Главное меню:"tables_custom":Подсветка разделов при наведении')
    link4 = '04_test_hover_buttons_tables_custom_'
    browser.element('[id="ind0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link4}1.png'))
    browser.element('[id="plb0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link4}2.png'))
    browser.element('[id="mvs0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link4}3.png'))
    browser.element('[id="tbl0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link4}4.png'))
    browser.element('[id="glr0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link4}5.png'))
    browser.element('[id="ind0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/index.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/index.html'))

def test_click_on_menu_glr():
    print('')
    print('Главное меню:"index"->"gallery"')
    browser.element('[id="glr0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/gallery.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))
    #Проверка подсветки контрольных кнопок меню галереи
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.no.css_class("active"))

def test_hover_buttons_gallery():
    print('')
    print('Главное меню:"gallery":Подсветка разделов при наведении')
    link5 = '05_test_hover_buttons_gallery_'
    browser.element('[id="ind0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link5}1.png'))
    browser.element('[id="plb0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link5}2.png'))
    browser.element('[id="mvs0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link5}3.png'))
    browser.element('[id="tbl0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link5}4.png'))
    browser.element('[id="glr0"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link5}5.png'))
    browser.element('[id="ind0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/index.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/index.html'))

def test_cross_click_on_menu():
    print('')
    print('Главное меню:Кросс-переходы')
    browser.open('/theveil/playbooks.html')
    browser.element('[id="plb0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/playbooks.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/playbooks.html'))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[1].should(have.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[4].should(have.no.css_class("active"))
    browser.element('[id="mvs0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/moves.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/moves.html'))
    browser.element('[id="mvs0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/moves.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/moves.html'))
    browser.element('[id="tbl0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/tables_custom.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/tables_custom.html'))
    browser.element('[id="tbl0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/tables_custom.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/tables_custom.html'))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu1]>ul>li')[0].should(have.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu1]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu1]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu1]>ul>li')[3].should(have.no.css_class("active"))
    browser.element('[id="glr0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/gallery.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.element('[id="glr0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/gallery.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"][name=menu0]>ul>li')[4].should(have.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[0].should(have.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class ="gallery-controls"]>ul>li')[3].should(have.no.css_class("active"))
    browser.element('[id="mvs0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/moves.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/moves.html'))
    browser.element('[id="plb0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/playbooks.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/playbooks.html'))
    browser.element('[id="glr0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/gallery.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.element('[id="tbl0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/tables_custom.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/tables_custom.html'))
    browser.element('[id="mvs0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/moves.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/moves.html'))
    browser.element('[id="glr0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/gallery.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.element('[id="plb0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/playbooks.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/playbooks.html'))
    browser.element('[id="tbl0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/tables_custom.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/tables_custom.html'))
    browser.element('[id="plb0"]').click()
    #Проверка загрузки
    status = requests.get('http://localhost/theveil/theveil/playbooks.html').status_code
    if status is 200:
        pass
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()
        #Конец проверки загрузки
    browser.should(have.url_containing('/theveil/playbooks.html'))

