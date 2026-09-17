import time

import pytest

from page.page_base_login import PageLogin
from page.page_backend_login import PageBackendLogin
from page.page_credit_application import PageCreditApplication
from page.page_credit_audit import PageCreditAudit
from tools import GetLog


log = GetLog.get_log()


class TestCreditAudit:
    @pytest.fixture(autouse=True)
    def setup_pages(self, browser):
        """初始化前台申请和后台审核所需的页面对象。"""
        self.front_login_page = PageLogin(browser)
        self.credit_page = PageCreditApplication(browser)
        self.backend_login_page = PageBackendLogin(browser)
        self.audit_page = PageCreditAudit(browser)

    def test_01_credit_application_pass(self):
        # 使用唯一备注标识本用例创建的申请，避免与其他待审核记录混淆
        username = "13800001009"
        remark = "自动化审核{}".format(time.time_ns())

        # 测试6自己准备前置数据，不再依赖测试4的执行结果
        self.front_login_page.login_success(username, "Aa123456")
        self.credit_page.switch_role()
        self.credit_page.click_credit_application()
        self.credit_page.credit_application("10000", remark, "8888")
        assert "提交申请成功" in self.credit_page.get_success_result()

        # 前置申请成功后，再进入后台执行审核
        self.backend_login_page.login_success("admin", "HM_2023_test", "8888")

        # 进入额度申请审核列表，查询并选中该用户的待审核记录
        self.audit_page.open_credit_audit_page()
        self.audit_page.search_and_select_application(username, remark)
        self.audit_page.open_audit_dialog()

        # 审核通过额度申请：通过额度、备注、测试验证码
        self.audit_page.pass_application("10000", "自动化测试审核通过", "8888")

        # 审核成功后，该记录应从“待审核”列表中消失
        pending = self.audit_page.is_application_pending(username, remark)
        log.info("额度审核后是否仍为待审核：{}".format(pending))
        assert pending is False
