import pytest

from page.page_base_login import PageLogin
from tools import GetLog


log = GetLog.get_log()


class TestLogin:
    @pytest.fixture(autouse=True)
    def setup_pages(self, browser):
        """使用 conftest.py 提供的浏览器初始化登录页面。"""
        self.page_login = PageLogin(browser)
        self.page_login.open_url()

    # 定义测试方法
    def test_01_login_success(self):
        # 准备数据
        # self.driver = DriverTools.get_driver()
        # self.page_login = PageLogin(self.driver)
        # 调用方法

        self.page_login.login("13800001001", "Aa123456")
        # 打印日志
        result = self.page_login.get_success_result()
        log.info("登录结果：{}".format(result))
        # 断言
        assert "13800001001" == result

    def test_02_login_fail_pwd_error(self):
        self.page_login.login("13800001001", "1234567")

        result = self.page_login.get_fail_result()
        log.info("登录结果：{}".format(result))
        assert "密码错误" in result
