from playwright.sync_api import Locator, ElementHandle

from src.core.interfaces.ui_element_interface import IUiElement


class PlaywrightElement(IUiElement):
    def __init__(self, element: Locator):
        self.__element = element

    def click(self):
        self.__element.click()

    def type(self, text: str):
        self.__element.type(text)

    def get_text(self) -> str:
        return self.__element.text_content()

    def is_visible(self) -> bool:
        return self.__element.is_visible()

    def get_value(self) -> str:
        return self.__element.input_value()
