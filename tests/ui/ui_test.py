import pytest
from playwright.sync_api import sync_playwright
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.enums.driver_type import DriverType
from src.factory.ui_driver__factory import create_ui_driver
from src.playwright.playwright_driver import PlaywrightUiDriver
from src.selenium.selenium_driver import SeleniumUiDriver
from tests.pages.duckduckgo_home_page import DuckDuckGoHomePage


@pytest.fixture(params=["selenium", "playwright"])
def driver(request):
    driver = create_ui_driver(request.param)
    yield driver
    driver.close()


def test_can_load_web_page_using_selenium(driver):
    home_page = DuckDuckGoHomePage(driver)
    driver.visit("https://duckduckgo.com")
    assert home_page.is_loaded()


def test_can_type_text_using_selenium(request, driver):
    home_page = DuckDuckGoHomePage(driver)
    driver.visit("https://duckduckgo.com")
    home_page.perform_search(f"{request.node.callspec.id} is great")
    assert home_page.get_search_box_content() == f"{request.node.callspec.id} is great"


def test_can_click_on_search_results(request, driver):
    home_page = DuckDuckGoHomePage(driver)
    driver.visit("https://duckduckgo.com")
    home_page.perform_search(f"{request.node.callspec.id}.dev\n")
    home_page.click_search_result()
    assert f"{request.node.callspec.id}.dev/" in driver.get_url()
