from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.core.interfaces.ui_driver_interface import IUiDriver
from src.core.interfaces.ui_element_interface import IUiElement
from src.selenium.selenium_element import SeleniumElement


class SeleniumUiDriver(IUiDriver):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, selector: str, by: By) -> IUiElement:
        return SeleniumElement(self.driver.find_element(by, selector))

    def visit(self, url: str):
        self.driver.get(url)

    def close(self):
        self.driver.close()

    def get_url(self) -> str:
        return self.driver.current_url
