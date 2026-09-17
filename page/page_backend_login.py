from selenium.webdriver.common.by import By

from base.page_base import BasePage
from config import BACK_URL


class PageBackendLogin(BasePage):
    """后台登录页面对象。"""

    def __init__(self, driver):
        super().__init__(driver)

        # 后台登录页的元素定位器
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.verify_code = (By.ID, "valicode")
        self.login_button = (By.CSS_SELECTOR, ".login-button")

        # 登录成功后，页面右上角会显示当前管理员信息
        self.admin_info = (By.CSS_SELECTOR, ".user-info")
        # 登录失败时，错误信息显示在这个元素中
        self.error_message = (By.ID, "errorMessage")

    def open_url(self):
        """打开后台登录页。"""
        self.driver.get(BACK_URL)

    def login(self, username, password, verify_code):
        """输入后台账号、密码、验证码并登录。"""
        self.base_input(self.username, username)
        self.base_input(self.password, password)
        self.base_input(self.verify_code, verify_code)
        self.base_click(self.login_button)

    def login_success(self, username, password, verify_code):
        """封装后台成功登录的完整步骤，供其他后台用例复用。"""
        self.open_url()
        self.login(username, password, verify_code)

    def get_success_result(self):
        """获取登录成功后的管理员信息。"""
        return self.base_get_text(self.admin_info)

    def get_fail_result(self):
        """获取登录失败提示。"""
        return self.base_get_text(self.error_message)
