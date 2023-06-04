import pytest
from selenium import webdriver
from selene import browser

"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest


@pytest.fixture(params=[(2560, 1440), (400, 560), (1920, 1080), (375, 667)],
                ids=['desktop', 'mobile', 'desktop', 'mobile'])
def browser_size(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]
    id = request.node.callspec.id
    yield browser, id
    browser.quit()


def test_github_desktop(browser_size):
    window, id = browser_size
    if 'mobile' in id:
        pytest.skip('Применяется мобильное соотношение сторон')
    window.open('https://github.com/')
    window.element('a.HeaderMenu-link--sign-in').click()


def test_github_mobile(browser_size):
    window, id = browser_size
    if 'desktop' in id:
        pytest.skip('Применяется десктопное соотношение сторон')
    window.open('https://github.com/')
    window.element('.flex-column [aria-label="Toggle navigation"]').click()
    window.element('a.HeaderMenu-link--sign-in').click()