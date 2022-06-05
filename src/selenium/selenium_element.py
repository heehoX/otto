from selenium.webdriver.remote.webelement import WebElement

from src.core.interfaces.ui_element_interface import IUiElement


class SeleniumElement(IUiElement):
    def __init__(self, element: WebElement):
        self.__element = element

    def click(self):
        self.__element.click()

    def type(self, text: str):
        self.__element.send_keys(text)

    def get_text(self) -> str:
        return self.__element.text

    def is_visible(self) -> bool:
        return self.__element.is_displayed()

    def get_value(self) -> str:
        return self.__element.get_attribute('value')
