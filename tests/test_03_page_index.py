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

def test_click_on_sectors():
    print('')
    print('Переходы через кнопки разделов')
    browser.element('[class="primary-btn class-btn"][id="plb1"]').click()
    browser.should(have.url_containing('/theveil/playbooks.html'))
    browser.open('/theveil/index.html')
    browser.element('[class="primary-btn class-btn"][id="mvs1"]').click()
    browser.should(have.url_containing('/theveil/moves.html'))
    browser.open('/theveil/')
    browser.element('[class="primary-btn class-btn"][id="tbl1"]').click()
    browser.should(have.url_containing('/theveil/tables_custom.html'))
    browser.open('/theveil/index.html')
    browser.element('[class="primary-btn class-btn"][id="glr1"]').click()
    browser.should(have.url_containing('/theveil/gallery.html'))
    browser.open('/theveil/')

def test_up_buton():
    print('')
    print('Клик на кнопку "Наверх"')
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/#'))
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/#'))
