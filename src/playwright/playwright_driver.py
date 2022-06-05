from playwright.sync_api import Page, Browser, Playwright
from selenium.webdriver.common.by import By

from src.core.interfaces.ui_driver_interface import IUiDriver
from src.core.interfaces.ui_element_interface import IUiElement
from src.playwright.playwright_element import PlaywrightElement


class PlaywrightUiDriver(IUiDriver):
    def __init__(self, playwright: Playwright):
        self.playwright = playwright
        self.browser = self.playwright.chromium.launch(headless=True)
        self.driver = self.browser.new_page()
        self.driver.set_viewport_size({"width": 1920, "height": 1080})

    def find_element(self, selector: str, by: By) -> IUiElement:
        final_selector = ""
        match by:
            case By.NAME:
                final_selector = f"[name='{selector}']"
            case By.ID:
                final_selector = f"#{selector}"
            case By.NAME:
                final_selector = f".{selector}"
            case _:
                final_selector = selector

        return PlaywrightElement(self.driver.locator(final_selector).first)

    def visit(self, url: str):
        self.driver.goto(url)

    def close(self):
        self.playwright.stop()

    def get_url(self) -> str:
        return self.driver.url
