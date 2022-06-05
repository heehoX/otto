from abc import ABCMeta, abstractmethod

from selenium.webdriver.common.by import By


class IUiElement(metaclass=ABCMeta):
    @abstractmethod
    def click(self): ...

    @abstractmethod
    def type(self, text: str): ...

    @abstractmethod
    def get_text(self) -> str: ...

    @abstractmethod
    def is_visible(self) -> bool: ...

    @abstractmethod
    def get_value(self) -> str: ...
