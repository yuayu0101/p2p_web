from base.page_base import BasePage
from selenium.webdriver.common.by import By
from config import BASE_URL


class PageOpenAccount(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.name = (
            By.NAME,
            "realname"
        )

        self.card = (
            By.NAME,
            "card_id"
        )

        self.submit_btn = (
            By.CSS_SELECTOR,
            '#safeName input[type="submit"][value="确认提交"]'
        )

        self.im_btn = (
            By.CSS_SELECTOR,
            '#successForm input[type="button"][value="立即开通"]'
        )

        self.success_result = (
            By.CSS_SELECTOR,
            "body"
        )

    def open_url(self):
        self.driver.get(BASE_URL + "/trust/public/reg")

    def open_account(self, name, card):
        self.open_url()
        self.base_input(self.name, name)
        self.base_input(self.card, card)
        self.base_click(self.submit_btn)
        self.base_click(self.im_btn)

    def get_success_result(self):
        return self.base_switch_handle(self.success_result).text.strip()
