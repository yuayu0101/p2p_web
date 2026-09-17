import pytest

from page.page_base_login import PageLogin
from page.page_credit_application import PageCreditApplication
from tools import GetLog


log = GetLog.get_log()


class TestCreditApplication:
    @pytest.fixture(autouse=True)
    def setup_pages(self, browser):
        """登录前台，并初始化额度申请页面对象。"""
        self.login_page = PageLogin(browser)
        self.login_page.login_success("13800001009", "Aa123456")
        self.credit_page = PageCreditApplication(browser)

    def test_01_credit_application_success(self):
        # 切换到借款账户并进入额度申请页面
        self.credit_page.switch_role()
        self.credit_page.click_credit_application()

        # 填写并提交额度申请
        self.credit_page.credit_application("10000", "自动化测试申请额度", "8888")

        # 获取并断言成功结果
        result = self.credit_page.get_success_result()
        log.info("额度申请结果：{}".format(result))
        assert "提交申请成功" in result
