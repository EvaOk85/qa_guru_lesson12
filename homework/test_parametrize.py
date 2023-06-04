import pytest
from selenium import webdriver
from selene import browser

"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest



@pytest.fixture(params=[(2560, 1440), (1920, 1080),(400, 560), (375, 667)])
def browser_size(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]
    yield browser
    browser.quit()


@pytest.mark.parametrize("browser_size", [(2560, 1440), (1920, 1080)], indirect=True)
def test_desktop(browser_size):
    browser_size.open('https://github.com/')
    browser_size.element('a.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize("browser_size", [(400, 560), (375, 667)], indirect=True)
def test_mobile(browser_size):
    browser_size.open('https://github.com/')
    browser_size.element('.flex-column [aria-label="Toggle navigation"]').click()
    browser_size.element('a.HeaderMenu-link--sign-in').click()