import pytest

from page.page_base_register import PageRegister


class TestRegister:
    @pytest.fixture(autouse=True)
    def setup_pages(self, browser):
        """使用统一浏览器 fixture 初始化注册页面。"""
        self.page_register = PageRegister(browser)
        self.page_register.open_url()

    def test_01_register_phone_exists(self):
        self.page_register.register("13800002009","Aa123456","8888","8888")
        assert "手机已存在" in self.page_register.get_fail_result()

