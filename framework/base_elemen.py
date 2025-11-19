import allure
from playwright.sync_api import Page, Locator, expect


class BaseElement:

    def __init__(self, locator: Locator, name: str) -> None:
        self.name = name
        self.locator = locator

    @property
    def type_of(self) -> str:
        return "Base element"

    def get_locator(self) -> Locator:
        with allure.step(f'Getting locator with for {self.name}'):
            return self.locator

    def click(self, nth: int = 0, **kwargs):
        step = f'Clicking {self.type_of} "{self.name}"'
        with allure.step(step):
            self.locator.click()

