from selene import browser, have, query
import requests
from selene.core.wait import Command
import time

def test_start():
    status = requests.get('http://localhost/theveil/').status_code
    if status is 200:
        print('')
        print('Статус код: 200 OK')
        browser.config.timeout = 6
        browser.open("/")
    else:
        print('')
        print('Код: ', status)
        browser.config.timeout = 0.1

def test_attention_title():
    print('')
    print('Приветственная страница:Наличие предупреждения')
    browser.element('[id="at1"]').should(have.text("ПРЕДУПРЕЖДЕНИЕ"))

def test_attention_text():
    print('')
    print('Приветственная страница:Наличие текста предупреждения')
    browser.element('[id="at2"]').should(have.text("Данный сайт является небольшим справочным ресурсом для личного использования по настольной ролевой игре the Veil (авторы: Фрейзер и Кайл Симмонс). Сайт ничего не пропогандирует и не распространяет. Публиковать ссылку на текущий домен, поддомены и страницы на домене или поддомене в любом другом ресурсе строго воспрещается."))

def scroll(x: int, y: int) -> Command:
    return Command(
        f'scroll page by x {x} y {y}',
        lambda browser: browser.driver.execute_script(
            f'window.scrollBy({x}, {y});'
        )
    )

link = 'C:/_test_screenshots/The_Veil_site_func_tests/test_01_page_attention/'

def test_scroll_down_up():
    print('')
    print('Скроллирование')
    browser.perform(scroll(0, 10000))
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}test_scroll_down_up_1_down.png'))
    browser.perform(scroll(0, -20000))
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}test_scroll_down_up_2_up.png'))
    browser.perform(scroll(1000, 0))
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}test_scroll_down_up_3_right.png'))
    browser.perform(scroll(-2000, 0))
    time.sleep(0.5)
    browser.get(query.screenshot_saved(f'{link}test_scroll_down_up_4_left.png'))

def test_open_site():
    print('')
    print('Приветственная страница:Переход основной сайт')
    browser.element('[class="opbut"]').click()
    browser.should(have.url_containing('/theveil/'))

