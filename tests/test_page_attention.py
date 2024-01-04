from selene import browser, have, be
import requests

response1 = requests.get('http://f0900261.xsph.ru/')
status1 = response1.status_code

browser.open("http://f0900261.xsph.ru/")
def test_start():
    print('')
    print('Загрузка страницы')
    if status1 is 200:
        print('Статус код: ', status1, ' OK')
    else:
        print('Код: ', status1)
        browser.element('[id="reload-button"]').click()
def test_attention_title():
    print('')
    print('Наличие предупреждения')
    browser.element('[id="at1"]').should(be.present)
def test_attention_text():
    print('')
    print('Наличие текста предупреждения')
    browser.element('[id="at2"]').should(be.present)
def test_button():
    print('')
    print('Наличие кнопки')
    browser.element('[class="opbut"]').should(be.present)

response2 = requests.get('http://f0900261.xsph.ru/theveil/')
status2 = response2.status_code
def test_open_site():
    print('')
    print('Переход на основной сайт')
    browser.element('[class="opbut"]').click()
    if status2 is 200:
        print('Статус код: ', status2, ' OK')
    else:
        print('Код: ', status2)
        browser.element('[id="reload-button"]').click()
    browser.should(have.url_containing('http://f0900261.xsph.ru/theveil/'))
