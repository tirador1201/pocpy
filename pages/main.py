from playwright.sync_api import Page

from framework.base_page import BasePage
from framework.elements.textbox import Textbox
import allure


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.test_textbox = Textbox(page.get_by_role("link", name="Get started"), "123")

    def click_link(self):
        with allure.step('Click link to make sure something happens'):
            self.test_textbox.click()
