from abc import ABCMeta, abstractmethod

from selenium.webdriver.common.by import By

from src.core.interfaces.ui_element_interface import IUiElement


class IUiDriver(metaclass=ABCMeta):
    @abstractmethod
    def visit(self, url: str): ...

    @abstractmethod
    def find_element(self, selector: str, by: By) -> IUiElement: ...

    @abstractmethod
    def close(self): ...

    @abstractmethod
    def get_url(self): ...
