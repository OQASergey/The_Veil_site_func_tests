from selene import browser, have, query
import requests
from selene.core.wait import Command

response1 = requests.get('http://localhost/theveil/')
status1 = response1.status_code
link = 'C:/_test_screenshots/test_01_page_attention/'

def scroll(x: int, y: int) -> Command:
    return Command(
        f'scroll page by x {x} y {y}',
        lambda browser: browser.driver.execute_script(
            f'window.scrollBy({x}, {y});'
        )
    )

def test_start():
    browser.open("/")
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
    browser.element('[id="at1"]').should(have.text("ПРЕДУПРЕЖДЕНИЕ"))
def test_attention_text():
    print('')
    print('Наличие текста предупреждения')
    browser.element('[id="at2"]').should(have.text("Данный сайт является небольшим справочным ресурсом для личного использования по настольной ролевой игре the Veil (авторы: Фрейзер и Кайл Симмонс). Сайт ничего не пропогандирует и не распространяет. Публиковать ссылку на текущий домен, поддомены и страницы на домене или поддомене в любом другом ресурсе строго воспрещается."))

def test_scroll_down_up():
    print('')
    print('Скролл вниз на 10 000 px')
    browser.perform(scroll(0, 10000))
    browser.get(query.screenshot_saved(f'{link}test_scroll_down_up_1_down.png'))
    print('Скролл вверх на 20 000 px')
    browser.perform(scroll(0, -20000))
    browser.get(query.screenshot_saved(f'{link}test_scroll_down_up_2_up.png'))

response2 = requests.get('http://localhost/theveil/theveil/')
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
    browser.should(have.url_containing('/theveil/'))
