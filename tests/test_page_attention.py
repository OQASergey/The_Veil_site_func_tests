from selene import browser, have, be

def test_start():
    print('')
    print('**Начало исполнения тестового набора**')
    browser.open("http://f0900261.xsph.ru/")

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
def test_open_site():
    print('')
    print('Переход на основной сайт')
    browser.element('[class="opbut"]').click()
    browser.should(have.url_containing('http://f0900261.xsph.ru/theveil/'))