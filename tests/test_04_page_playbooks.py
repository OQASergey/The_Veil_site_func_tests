from selene import browser, have, query, be
import requests
from selene.core.wait import Command
import time

response = requests.get('http://localhost/theveil/theveil/playbooks.html')
status = response.status_code
link = 'C:/_test_screenshots/test_04_page_playbooks/'

def scroll(x: int, y: int) -> Command:
    return Command(
        f'scroll page by x {x} y {y}',
        lambda browser: browser.driver.execute_script(
            f'window.scrollBy({x}, {y});'
        )
    )

def test_start():
    browser.open("/theveil/playbooks.html")
    print('')
    print('"playbooks":Загрузка страницы')
    if status is 200:
        print('Статус код: ', status, ' OK')
    else:
        print('Код: ', status)
        browser.element('[id="reload-button"]').click()

def test_click_on_breadcrumbs():
    print('')
    print('"playbooks"->"index" через breadcrumbs')
    browser.element('[class="fa fa-home"]').click()
    browser.should(have.url_containing('/theveil/index.html'))
    browser.open('/theveil/playbooks.html')

def test_scroll_down_up():
    print('')
    print('"playbooks":Скролл вниз на 10 000 px')
    link1 = '01_test_scroll_down_up_'
    browser.perform(scroll(0, 10000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}_1_down.png'))
    print('"playbooks":Скролл вверх на 20 000 px')
    browser.perform(scroll(0, -20000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}2_up.png'))
    print('"playbooks":Скролл вправа на 1 000 px')
    browser.perform(scroll(1000, 0))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}3_right.png'))
    print('"playbooks":Скролл влево на 2 000 px')
    browser.perform(scroll(-2000, 0))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}4_left.png'))

def test_hover_booklets():
    print('')
    print('"playbooks":Наведение на буклеты')
    link2 = '02_test_hover_booklets_'
    #Первый уровень
    browser.perform(scroll(0,350))
    browser.all('[name="flr1"]>div')[0].element('[class="ti-pic"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}01.png'))
    browser.all('[name="flr1"]>div')[1].element('[class="ti-pic"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}02.png'))
    browser.all('[name="flr1"]>div')[2].element('[class="ti-pic"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}03.png'))
    browser.all('[name="flr1"]>div')[3].element('[class="ti-pic"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}04.png'))
    #Второй уровень
    browser.perform(scroll(0,350))
    browser.all('[name="flr2"]>div')[0].element('[class="ti-pic"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}05.png'))
    browser.all('[name="flr2"]>div')[1].element('[class="ti-pic"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}06.png'))
    browser.all('[name="flr2"]>div')[2].element('[class="ti-pic"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}07.png'))
    browser.all('[name="flr2"]>div')[3].element('[class="ti-pic"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}08.png'))
    #Третий уровень
    browser.perform(scroll(0,350))
    browser.all('[name="flr3"]>div')[0].element('[class="ti-pic"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}09.png'))
    browser.all('[name="flr3"]>div')[1].element('[class="ti-pic"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}10.png'))
    browser.all('[name="flr3"]>div')[2].element('[class="ti-pic"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}11.png'))
    browser.all('[name="flr3"]>div')[3].element('[class="ti-pic"]').hover()
    time.sleep(1.5)
    browser.get(query.screenshot_saved(f'{link}{link2}12.png'))
    browser.perform(scroll(0,-10000))

def test_click_on_booklets_button():
    print('')
    print('"playbooks":Открытие буклета')
    link3 = '03_test_click_on_booklets_button_'
    browser.perform(scroll(0,350))
    #Первый уровень
    #Первый буклет
    browser.all('[name="flr1"]>div')[0].element('[class="primary-btn f-btn"]').should(have.attribute('target','_blank'))
    browser.all('[name="flr1"]>div')[0].element('[class="primary-btn f-btn"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link3}01.png'))
    browser.all('[name="flr1"]>div')[0].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/APPARATUS.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)
    #Второй буклет
    browser.all('[name="flr1"]>div')[1].element('[class="primary-btn f-btn"]').should(have.attribute('target','_blank'))
    browser.all('[name="flr1"]>div')[1].element('[class="primary-btn f-btn"]').click()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link3}02.png'))
    browser.all('[name="flr1"]>div')[1].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/ARCHITECT.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)
    #Третий буклет
    browser.all('[name="flr1"]>div')[2].element('[class="primary-btn f-btn"]').should(have.attribute('target','_blank'))
    browser.all('[name="flr1"]>div')[2].element('[class="primary-btn f-btn"]').click()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link3}03.png'))
    browser.all('[name="flr1"]>div')[2].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/ATTACHED.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)
    #Четвёртый буклет
    browser.all('[name="flr1"]>div')[3].element('[class="primary-btn f-btn"]').should(have.attribute('target','_blank'))
    browser.all('[name="flr1"]>div')[3].element('[class="primary-btn f-btn"]').click()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link3}04.png'))
    browser.all('[name="flr1"]>div')[3].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/CATABOLIST.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)
    #Второй уровень
    #Пятый буклет
    browser.all('[name="flr2"]>div')[0].element('[class="primary-btn f-btn"]').should(have.attribute('target','_blank'))
    browser.all('[name="flr2"]>div')[0].element('[class="primary-btn f-btn"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link3}05.png'))
    browser.all('[name="flr2"]>div')[0].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/DYING.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)
    #Шестой буклет
    browser.all('[name="flr2"]>div')[1].element('[class="primary-btn f-btn"]').should(have.attribute('target','_blank'))
    browser.all('[name="flr2"]>div')[1].element('[class="primary-btn f-btn"]').click()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link3}06.png'))
    browser.all('[name="flr2"]>div')[1].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/EMPATH.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)
    #Седьмой буклет
    browser.all('[name="flr2"]>div')[2].element('[class="primary-btn f-btn"]').should(have.attribute('target','_blank'))
    browser.all('[name="flr2"]>div')[2].element('[class="primary-btn f-btn"]').click()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link3}07.png'))
    browser.all('[name="flr2"]>div')[2].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/EXECUTIVE.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)
    #Восьмой буклет
    browser.all('[name="flr2"]>div')[3].element('[class="primary-btn f-btn"]').should(have.attribute('target','_blank'))
    browser.all('[name="flr2"]>div')[3].element('[class="primary-btn f-btn"]').click()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link3}08.png'))
    browser.all('[name="flr2"]>div')[3].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/HONED.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)
    #Третий уровень
    #Девятый буклет
    browser.all('[name="flr3"]>div')[0].element('[class="primary-btn f-btn"]').should(have.attribute('target','_blank'))
    browser.all('[name="flr3"]>div')[0].element('[class="primary-btn f-btn"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link3}09.png'))
    browser.all('[name="flr3"]>div')[0].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/HONORBOUND.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)
    #Десятый буклет
    browser.all('[name="flr3"]>div')[1].element('[class="primary-btn f-btn"]').should(have.attribute('target','_blank'))
    browser.all('[name="flr3"]>div')[1].element('[class="primary-btn f-btn"]').click()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link3}10.png'))
    browser.all('[name="flr3"]>div')[1].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/ONOMASTIC.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)
    #Одинадцатый буклет
    browser.all('[name="flr3"]>div')[2].element('[class="primary-btn f-btn"]').should(have.attribute('target','_blank'))
    browser.all('[name="flr3"]>div')[2].element('[class="primary-btn f-btn"]').click()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link3}11.png'))
    browser.all('[name="flr3"]>div')[2].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/SEEKER.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)
    #Двенадцатый буклет
    browser.all('[name="flr3"]>div')[3].element('[class="primary-btn f-btn"]').should(have.attribute('target','_blank'))
    browser.all('[name="flr3"]>div')[3].element('[class="primary-btn f-btn"]').click()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link3}12.png'))
    browser.all('[name="flr3"]>div')[3].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/WAYWARD.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)
    browser.perform(scroll(0,-10000))

