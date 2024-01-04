from selene import browser, have, be
import requests

response = requests.get('http://f0900261.xsph.ru/theveil/')
status = response.status_code

browser.open("http://f0900261.xsph.ru/theveil/")
def test_start():
    print('')
    print('Загрузка страницы')
    if status is 200:
        print('Статус код: ', status, ' OK')
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()

def test_menu():
    print('')
    print('Наличие элементов: меню: кнопки')
    browser.all('[class="mainmenu mobile-menu"]>ul>li').should(have.size(5))
def test_active_button():
    print('')
    print('Наличие элементов: меню: подсветка разделов')
    browser.element('[class="mainmenu mobile-menu"]>ul>li[class="active"]').should(be.present)
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[4].should(have.no.css_class("active"))
def test_Title():
    print('')
    print('Наличие элементов: шапка: текст, изображение')
    browser.all('[class="hero-section"]').should(have.attribute("id","ttl_tx"))
    browser.all('[class="hero-section"]').should(have.attribute("data-setbg", "img/hero-slider/hero-1.jpg"))

def test_Secion():
    print('')
    print('Наличие элементов: разделы: разделитель: заглавие, тексты, изображение')
    browser.all('[class="class-title set-bg"]').should(have.attribute("class","section-title pl-lg-4 pr-lg-4 pl-0 pr-0"))
    browser.all('[class="class-title set-bg"]').should(have.attribute("data-setbg","img/classes-title-bg.jpg"))
