from selenium.webdriver.common.by import By

from src.core.interfaces.ui_driver_interface import IUiDriver
from src.core.interfaces.ui_element_interface import IUiElement


class DuckDuckGoHomePage:
    def __init__(self, driver: IUiDriver):
        self.driver = driver

    def __search_box(self) -> IUiElement:
        return self.driver.find_element(selector='q', by=By.NAME)

    def __search_result(self) -> IUiElement:
        return self.driver.find_element(selector='a[data-testid="result-title-a"]', by=By.CSS_SELECTOR)

    def perform_search(self, search_term: str):
        self.__search_box().type(search_term)

    def click_search_result(self) -> None:
        self.__search_result().click()

    def is_loaded(self) -> bool:
        return self.__search_box().is_visible()

    def get_search_box_content(self) -> str:
        return self.__search_box().get_value()
