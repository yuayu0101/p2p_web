from base.page_base import BasePage
from selenium.webdriver.common.by import By


class PageCreditApplication(BasePage):
    # 额度申请
    def __init__(self, driver):
        super().__init__(driver)
        # 元素定位（属性和方法名不可以一样）
        self.role = (By.XPATH, '//*[@id="mlayout"]/div[2]/div[2]/div[1]/a/em')
        self.credit_app = (By.LINK_TEXT, "申请额度")
        self.money = (By.ID, "amount_account")
        self.detail = (By.NAME, "remark")
        self.code = (By.ID, "verifycode")
        self.submit = (By.CSS_SELECTOR, ".btn-submit.btn-md")
        self.success_result = (By.XPATH, "//*[normalize-space(.)='提交申请成功']")

    def switch_role(self):  # 点击切换到借款账户
        self.base_click(self.role)

    def click_credit_application(self):  # 点击额度申请
        self.base_click(self.credit_app)

    def credit_application(self, money, detail, code):
        self.base_input(self.money, money)
        self.base_input(self.detail, detail)
        self.base_input(self.code, code)
        self.base_click(self.submit)

    def get_success_result(self):
        return self.base_get_text(self.success_result)
