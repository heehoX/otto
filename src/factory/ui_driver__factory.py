from playwright.sync_api import sync_playwright
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.core.interfaces.ui_driver_interface import IUiDriver
from src.playwright.playwright_driver import PlaywrightUiDriver
from src.selenium.selenium_driver import SeleniumUiDriver


def create_ui_driver(driver_type: str) -> IUiDriver:
    match driver_type:
        case "selenium":
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            selenium_driver = SeleniumUiDriver(driver)
            return selenium_driver
        case "playwright":
            playwright = sync_playwright().start()
            playwright_driver = PlaywrightUiDriver(playwright)
            return playwright_driver
        case _:
            print(f"{driver_type} is not supported")
