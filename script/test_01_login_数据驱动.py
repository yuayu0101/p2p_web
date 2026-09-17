import pytest

from page.page_base_login import PageLogin
from tools import GetLog, read_json


log = GetLog.get_log()


class TestLogin:
    @pytest.fixture(autouse=True)
    def setup_pages(self, browser):
        """使用统一浏览器 fixture 初始化登录页面。"""
        self.page_login = PageLogin(browser)
        self.page_login.open_url()

    # 定义测试方法
    @pytest.mark.parametrize(
        "phone,password,expected,success",
        read_json("login_data.json"),
    )
    def test_01_login(self, phone, password, expected, success):
        # 准备数据
        # self.driver = DriverTools.get_driver()
        # self.page_login = PageLogin(self.driver)
        # 调用方法

        self.page_login.login(phone, password)
        # 成功用例读取用户名，失败用例读取页面错误提示
        if success:
            result = self.page_login.get_success_result()
        else:
            result = self.page_login.get_fail_result()
        # 打印日志

        log.info("登录结果：{}".format(result))
        # 断言
        assert expected in result


