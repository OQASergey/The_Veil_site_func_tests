from selene import browser, have, be
import requests

response = requests.get('http://localhost/theveil/theveil/')
status = response.status_code

def test_start():
    browser.open("/theveil/")
    print('')
    print('Загрузка страницы')
    if status is 200:
        print('Статус код: ', status, ' OK')
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()

def test_active_button():
    print('')
    print('Меню: подсветка разделов')
    browser.element('[class="mainmenu mobile-menu"]>ul>li[class="active"]').should(be.present)
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[4].should(have.no.css_class("active"))
def test_click_on_menu_ind():
    print('')
    print('Переходы через меню: "Главная"')
    browser.element('[id="ind0"]').click()
    browser.should(have.url_containing('/theveil/index.html'))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[0].should(have.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[4].should(have.no.css_class("active"))
def test_click_on_menu_plb():
    print('')
    print('Переходы через меню: "Главная"')
    browser.element('[id="plb0"]').click()
    browser.should(have.url_containing('/theveil/playbooks.html'))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[0].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[1].should(have.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[4].should(have.no.css_class("active"))
    browser.element('[id="ind0"]').click()
    browser.should(have.url_containing('/theveil/index.html'))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[0].should(have.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[1].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[2].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[3].should(have.no.css_class("active"))
    browser.all('[class="mainmenu mobile-menu"]>ul>li')[4].should(have.no.css_class("active"))