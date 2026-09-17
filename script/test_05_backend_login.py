import pytest

from page.page_backend_login import PageBackendLogin
from tools import GetLog


log = GetLog.get_log()


class TestBackendLogin:
    @pytest.fixture(autouse=True)
    def setup_pages(self, browser):
        """使用统一浏览器 fixture 初始化后台登录页面。"""
        self.login_page = PageBackendLogin(browser)
        self.login_page.open_url()

    def test_01_backend_login_success(self):
        # 使用后台测试账号登录，图片验证码在测试环境固定为 8888
        self.login_page.login("admin", "HM_2023_test", "8888")

        # 管理员信息中出现 admin，说明后台登录成功
        result = self.login_page.get_success_result()
        log.info("后台登录结果：{}".format(result))
        assert "admin" in result
