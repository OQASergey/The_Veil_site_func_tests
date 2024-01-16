from selene import browser, have, query, be
import requests
from selene.core.wait import Command
import time
from selenium import webdriver

core_link = 'http://localhost/theveil'

def test_start():
    status = requests.get(f'{core_link}/theveil/playbooks.html').status_code
    if status == 200:
        print('')
        print('Статус код: 200 OK')
        browser.config.timeout = 6
        browser.open("/theveil/playbooks.html")
    else:
        print('')
        print('Страница не открыта. Код: ', status)
        browser.config.timeout = 0.1

def test_click_on_breadcrumbs():
    print('')
    print('"playbooks"->"index" через breadcrumbs')
    browser.should(have.url_containing('/theveil/playbooks.html'))
    browser.element('[class="fa fa-home"]').click()
    browser.should(have.url_containing('/theveil/index.html'))

def scroll(x: int, y: int) -> Command:
    return Command(
        f'scroll page by x {x} y {y}',
        lambda browser: browser.driver.execute_script(
            f'window.scrollBy({x}, {y});'
        )
    )

link = 'C:/_test_screenshots/The_Veil_site_func_tests/test_04_page_playbooks/'

def test_scroll():
    print('')
    print('"playbooks":Скроллирование')
    link1 = '01_test_scroll_down_up_'
    browser.open('/theveil/playbooks.html')
    browser.should(have.url_containing('/theveil/playbooks.html'))
    browser.perform(scroll(0, 10000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}1_down.png'))
    browser.perform(scroll(0, -20000))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}2_up.png'))
    browser.perform(scroll(1000, 0))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}3_right.png'))
    browser.perform(scroll(-2000, 0))
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link1}4_left.png'))

link2 = '02_test_playbook_'
#Первый уровень
def test_playbook_01():
    print('')
    print('"playbooks":Буклет_01')
    browser.perform(scroll(0,350))
    browser.all('[name="flr1"]>div')[0].element('[class="ti-pic"]').hover()
    browser.all('[name="flr1"]>div')[0].element('[id="plus1"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}01_1_hover_popup.png'))
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr1"]>div')[0].element('[id="plus1"]').click()
    browser.element('[class="mfp-img"]').should(
        have.attribute(
            'src', f'{core_link}/theveil/img/booklet/preview/APPARATUS.jpg'
        )
    )
    time.sleep(0.3)
    browser.get(query.screenshot_saved(f'{link}{link2}01_2_click_popup.png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr1"]>div')[0].element('[class="ti-pic"]').hover()
    browser.all('[name="flr1"]>div')[0].element('[id="lang1"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}01_3_hover_rus.png'))
    browser.all('[name="flr1"]>div')[0].element('[id="lang1"]').should(
        have.attribute('target','_blank'
        )
    )
    browser.all('[name="flr1"]>div')[0].element('[id="lang1"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/APPARATUS_rus.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)
    browser.all('[name="flr1"]>div')[0].element('[class="primary-btn f-btn"]').should(
        have.attribute('target','_blank'
        )
    )
    browser.all('[name="flr1"]>div')[0].element('[class="primary-btn f-btn"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}01_4_hover_button.png'))
    browser.all('[name="flr1"]>div')[0].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/APPARATUS.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)

def test_playbook_02():
    print('')
    print('"playbooks":Буклет_02')
    browser.all('[name="flr1"]>div')[1].element('[class="ti-pic"]').hover()
    browser.all('[name="flr1"]>div')[1].element('[id="plus1"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}02_1_hover_popup.png'))
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr1"]>div')[1].element('[id="plus1"]').click()
    browser.element('[class="mfp-img"]').should(
        have.attribute(
            'src', f'{core_link}/theveil/img/booklet/preview/ARCHITECT.jpg'
        )
    )
    time.sleep(0.3)
    browser.get(query.screenshot_saved(f'{link}{link2}02_2_click_popup.png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr1"]>div')[1].element('[class="ti-pic"]').hover()
    browser.all('[name="flr1"]>div')[1].element('[id="lang1"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}02_3_hover_rus.png'))
    browser.all('[name="flr1"]>div')[1].element('[id="lang1"]').should(
        have.attribute('target', '_blank'
                       )
    )
    browser.all('[name="flr1"]>div')[1].element('[id="lang1"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/ARCHITECT_rus.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)
    browser.all('[name="flr1"]>div')[1].element('[class="primary-btn f-btn"]').should(
        have.attribute('target','_blank'
        )
    )
    browser.all('[name="flr1"]>div')[1].element('[class="primary-btn f-btn"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}02_4_hover_button.png'))
    browser.all('[name="flr1"]>div')[1].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/ARCHITECT.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)

def test_playbook_03():
    print('')
    print('"playbooks":Буклет_03')
    browser.all('[name="flr1"]>div')[2].element('[class="ti-pic"]').hover()
    browser.all('[name="flr1"]>div')[2].element('[id="plus1"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}03_1_hover_popup.png'))
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr1"]>div')[2].element('[id="plus1"]').click()
    browser.element('[class="mfp-img"]').should(
        have.attribute(
            'src', f'{core_link}/theveil/img/booklet/preview/ATTACHED.jpg'
        )
    )
    time.sleep(0.3)
    browser.get(query.screenshot_saved(f'{link}{link2}03_2_click_popup.png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr1"]>div')[2].element('[class="ti-pic"]').hover()
    browser.all('[name="flr1"]>div')[2].element('[id="lang1"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}03_3_hover_rus.png'))
    browser.all('[name="flr1"]>div')[2].element('[id="lang1"]').should(
        have.attribute('target', '_blank'
                       )
    )
    browser.all('[name="flr1"]>div')[2].element('[id="lang1"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/ATTACHED_rus.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)
    browser.all('[name="flr1"]>div')[2].element('[class="primary-btn f-btn"]').should(
        have.attribute('target','_blank'
        )
    )
    browser.all('[name="flr1"]>div')[2].element('[class="primary-btn f-btn"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}03_4_hover_button.png'))
    browser.all('[name="flr1"]>div')[2].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/ATTACHED.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)

def test_playbook_04():
    print('')
    print('"playbooks":Буклет_04')
    browser.all('[name="flr1"]>div')[3].element('[class="ti-pic"]').hover()
    browser.all('[name="flr1"]>div')[3].element('[id="plus1"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}04_1_hover_popup.png'))
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr1"]>div')[3].element('[id="plus1"]').click()
    browser.element('[class="mfp-img"]').should(
        have.attribute(
            'src', f'{core_link}/theveil/img/booklet/preview/CATABOLIST.jpg'
        )
    )
    time.sleep(0.3)
    browser.get(query.screenshot_saved(f'{link}{link2}04_2_popup.png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr1"]>div')[3].element('[class="ti-pic"]').hover()
    browser.all('[name="flr1"]>div')[3].element('[id="lang1"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}04_3_hover_rus.png'))
    browser.all('[name="flr1"]>div')[3].element('[id="lang1"]').should(
        have.attribute('target', '_blank'
                       )
    )
    browser.all('[name="flr1"]>div')[3].element('[id="lang1"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/CATABOLIST_rus.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)
    browser.all('[name="flr1"]>div')[3].element('[class="primary-btn f-btn"]').should(
        have.attribute('target','_blank'
        )
    )
    browser.all('[name="flr1"]>div')[3].element('[class="primary-btn f-btn"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}04_4_hover_button.png'))
    browser.all('[name="flr1"]>div')[3].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/CATABOLIST.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)

#Второй уровень
def test_playbook_05():
    print('')
    print('"playbooks":Буклет_05')
    browser.perform(scroll(0,350))
    browser.all('[name="flr2"]>div')[0].element('[class="ti-pic"]').hover()
    browser.all('[name="flr2"]>div')[0].element('[class="ti-links"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}05_1_hover_popup.png'))
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr2"]>div')[0].element('[class="ti-links"]').click()
    browser.element('[class="mfp-img"]').should(
        have.attribute(
            'src', f'{core_link}/theveil/img/booklet/preview/DYING.jpg'
        )
    )
    time.sleep(0.3)
    browser.get(query.screenshot_saved(f'{link}{link2}05_2_popup.png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr2"]>div')[0].element('[class="primary-btn f-btn"]').should(
        have.attribute('target','_blank'
        )
    )
    browser.all('[name="flr2"]>div')[0].element('[class="primary-btn f-btn"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}05_3_hover_button.png'))
    browser.all('[name="flr2"]>div')[0].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/DYING.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)

def test_playbook_06():
    print('')
    print('"playbooks":Буклет_06')
    browser.all('[name="flr2"]>div')[1].element('[class="ti-pic"]').hover()
    browser.all('[name="flr2"]>div')[1].element('[class="ti-links"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}06_1_hover_popup.png'))
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr2"]>div')[1].element('[class="ti-links"]').click()
    browser.element('[class="mfp-img"]').should(
        have.attribute(
            'src', f'{core_link}/theveil/img/booklet/preview/EMPATH.jpg'
        )
    )
    time.sleep(0.3)
    browser.get(query.screenshot_saved(f'{link}{link2}06_2_popup.png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr2"]>div')[1].element('[class="primary-btn f-btn"]').should(
        have.attribute('target','_blank'
        )
    )
    browser.all('[name="flr2"]>div')[1].element('[class="primary-btn f-btn"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}06_3_hover_button.png'))
    browser.all('[name="flr2"]>div')[1].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/EMPATH.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)

def test_playbook_07():
    print('')
    print('"playbooks":Буклет_07')
    browser.all('[name="flr2"]>div')[2].element('[class="ti-pic"]').hover()
    browser.all('[name="flr2"]>div')[2].element('[class="ti-links"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}07_1_hover_popup.png'))
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr2"]>div')[2].element('[class="ti-links"]').click()
    browser.element('[class="mfp-img"]').should(
        have.attribute(
            'src', f'{core_link}/theveil/img/booklet/preview/EXECUTIVE.jpg'
        )
    )
    time.sleep(0.3)
    browser.get(query.screenshot_saved(f'{link}{link2}07_2_popup.png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr2"]>div')[2].element('[class="primary-btn f-btn"]').should(
        have.attribute('target','_blank'
        )
    )
    browser.all('[name="flr2"]>div')[2].element('[class="primary-btn f-btn"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}07_3_hover_button.png'))
    browser.all('[name="flr2"]>div')[2].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/EXECUTIVE.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)

def test_playbook_08():
    print('')
    print('"playbooks":Буклет_08')
    browser.all('[name="flr2"]>div')[3].element('[class="ti-pic"]').hover()
    browser.all('[name="flr2"]>div')[3].element('[class="ti-links"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}08_1_hover_popup.png'))
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr2"]>div')[3].element('[class="ti-links"]').click()
    browser.element('[class="mfp-img"]').should(
        have.attribute(
            'src', f'{core_link}/theveil/img/booklet/preview/HONED.jpg'
        )
    )
    time.sleep(0.3)
    browser.get(query.screenshot_saved(f'{link}{link2}08_2_popup.png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr2"]>div')[3].element('[class="primary-btn f-btn"]').should(
        have.attribute('target','_blank'
        )
    )
    browser.all('[name="flr2"]>div')[3].element('[class="primary-btn f-btn"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}08_3_hover_button.png'))
    browser.all('[name="flr2"]>div')[3].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/HONED.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)

#Третий уровень
def test_playbook_09():
    print('')
    print('"playbooks":Буклет_09')
    browser.perform(scroll(0,350))
    browser.all('[name="flr3"]>div')[0].element('[class="ti-pic"]').hover()
    browser.all('[name="flr3"]>div')[0].element('[class="ti-links"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}09_1_hover_popup.png'))
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr3"]>div')[0].element('[class="ti-links"]').click()
    browser.element('[class="mfp-img"]').should(
        have.attribute(
            'src', f'{core_link}/theveil/img/booklet/preview/HONORBOUND.jpg'
        )
    )
    time.sleep(0.3)
    browser.get(query.screenshot_saved(f'{link}{link2}09_2_popup.png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr3"]>div')[0].element('[class="primary-btn f-btn"]').should(
        have.attribute('target','_blank'
        )
    )
    browser.all('[name="flr3"]>div')[0].element('[class="primary-btn f-btn"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}09_3_hover_button.png'))
    browser.all('[name="flr3"]>div')[0].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/HONORBOUND.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)

def test_playbook_10():
    print('')
    print('"playbooks":Буклет_10')
    browser.all('[name="flr3"]>div')[1].element('[class="ti-pic"]').hover()
    browser.all('[name="flr3"]>div')[1].element('[class="ti-links"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}10_1_hover_popup.png'))
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr3"]>div')[1].element('[class="ti-links"]').click()
    browser.element('[class="mfp-img"]').should(
        have.attribute(
            'src', f'{core_link}/theveil/img/booklet/preview/ONOMASTIC.jpg'
        )
    )
    time.sleep(0.3)
    browser.get(query.screenshot_saved(f'{link}{link2}10_2_popup.png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr3"]>div')[1].element('[class="primary-btn f-btn"]').should(
        have.attribute('target','_blank'
        )
    )
    browser.all('[name="flr3"]>div')[1].element('[class="primary-btn f-btn"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}10_3_hover_button.png'))
    browser.all('[name="flr3"]>div')[1].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/ONOMASTIC.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)

def test_playbook_11():
    print('')
    print('"playbooks":Буклет_11')
    browser.all('[name="flr3"]>div')[2].element('[class="ti-pic"]').hover()
    browser.all('[name="flr3"]>div')[2].element('[class="ti-links"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}11_1_hover_popup.png'))
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr3"]>div')[2].element('[class="ti-links"]').click()
    browser.element('[class="mfp-img"]').should(
        have.attribute(
            'src', f'{core_link}/theveil/img/booklet/preview/SEEKER.jpg'
        )
    )
    time.sleep(0.3)
    browser.get(query.screenshot_saved(f'{link}{link2}11_2_popup.png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr3"]>div')[2].element('[class="primary-btn f-btn"]').should(
        have.attribute('target','_blank'
        )
    )
    browser.all('[name="flr3"]>div')[2].element('[class="primary-btn f-btn"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}11_3_hover_button.png'))
    browser.all('[name="flr3"]>div')[2].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/SEEKER.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)

def test_playbook_12():
    print('')
    print('"playbooks":Буклет_12')
    browser.all('[name="flr3"]>div')[3].element('[class="ti-pic"]').hover()
    browser.all('[name="flr3"]>div')[3].element('[class="ti-links"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}12_1_hover_popup.png'))
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr3"]>div')[3].element('[class="ti-links"]').click()
    browser.element('[class="mfp-img"]').should(
        have.attribute(
            'src', f'{core_link}/theveil/img/booklet/preview/WAYWARD.jpg'
        )
    )
    time.sleep(0.3)
    browser.get(query.screenshot_saved(f'{link}{link2}12_2_popup.png'))
    browser.element('[title="Close (Esc)"]').click()
    browser.element('[class="mfp-img"]').should(be.absent)
    browser.all('[name="flr3"]>div')[3].element('[class="primary-btn f-btn"]').should(
        have.attribute('target','_blank'
        )
    )
    browser.all('[name="flr3"]>div')[3].element('[class="primary-btn f-btn"]').hover()
    time.sleep(1)
    browser.get(query.screenshot_saved(f'{link}{link2}12_3_hover_button.png'))
    browser.all('[name="flr3"]>div')[3].element('[class="primary-btn f-btn"]').click()
    browser.switch_to_next_tab()
    browser.should(have.url_containing('/theveil/img/booklet/png/WAYWARD.png'))
    browser.close_current_tab()
    browser.switch_to_tab(0)

def test_download_button():
    print('')
    print('"playbooks":Кнопка "download"')
    link3 = 'http://localhost/theveil/veil_playbooks.pdf'
    browser.element('[name="dwn1"]').should(have.attribute('href',link3))
    browser.element('[name="dwn1"]').should(have.attribute('download'))
    browser.element('[name="dwn1"]>img[alt="Скачать буклеты"]').should(be.present)
    driver = webdriver.Chrome()
    driver.get(link3)
    time.sleep(3)
    driver.save_screenshot(f'{link}03_test_download_button_to_url.png')
    driver.close()

def test_up_button():
    print('')
    print('"playbooks":Кнопка "Наверх"')
    browser.perform(scroll(0, 10000))
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/playbooks.html#'))
    browser.element('[class="primary-btn cta-btn"]').click()
    browser.should(have.url_containing('/theveil/playbooks.html#'))