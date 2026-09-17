import pytest

from config import CARD, NAME, PHONE
from page.page_base_login import PageLogin
from page.page_base_register import PageRegister
from page.page_open_account import PageOpenAccount
from tools import GetLog


log = GetLog.get_log()


class TestOpenAccount:
    @pytest.fixture(autouse=True)
    def setup_pages(self, browser):
        """初始化注册、登录和开户页面对象。"""
        self.register = PageRegister(browser)
        self.login = PageLogin(browser)
        self.open_acc = PageOpenAccount(browser)

    def test_01_open_account_success(self):
        # 每次使用随机手机号注册新用户，避免已有账号重复开户
        password = "Aa123456"
        self.register.open_url()
        self.register.register(PHONE, password, "8888", "666666")
        assert "注册成功" in self.register.get_success_result()

        # 新用户登录后执行开户
        self.login.login_success(PHONE, password)
        self.open_acc.open_account(NAME,CARD)
        result=self.open_acc.get_success_result()
        log.info(f"开户结果:{result}")
        #断言
        assert "OK" in result
