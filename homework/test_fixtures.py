import pytest
from selenium import webdriver
from selene import browser
"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


@pytest.fixture(params=[(2560, 1440), (1920, 1080)])
def test_github_desktop(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]
    yield browser
    browser.quit()


@pytest.fixture(params=[(400, 560), (375, 667)])
def test_github_mobile(request):
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_height = request.param[0]
    browser.config.window_width = request.param[1]
    yield browser
    browser.quit()


def test_desktop(test_github_desktop):
    browser.open('https://github.com/')
    browser.element('a.HeaderMenu-link--sign-in').click()


def test_mobile(test_github_mobile):
    browser.open('https://github.com/')
    browser.element('.flex-column [aria-label="Toggle navigation"]').click()
    browser.element('a.HeaderMenu-link--sign-in').click()