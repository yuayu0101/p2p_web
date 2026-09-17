from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.page_base import BasePage


class PageCreditAudit(BasePage):
    """后台额度申请审核页面对象。"""

    def __init__(self, driver):
        super().__init__(driver)

        # 后台左侧菜单及主内容 iframe
        self.credit_manage_menu = (
            By.XPATH,
            "//span[normalize-space(.)='额度管理']/parent::a",
        )
        self.credit_audit_menu = (
            By.CSS_SELECTOR,
            "a[rel='loan/amountapply/list']",
        )
        self.content_iframe = (By.ID, "iframe_box")

        # 额度申请列表页
        self.search_username = (By.NAME, "member_name")
        self.search_button = (By.CSS_SELECTOR, "input.srcbtn")
        self.audit_button = (By.LINK_TEXT, "审核")

        # 点击“审核”后，表单会显示在列表页内部的新 iframe 中
        self.audit_iframe = (By.CSS_SELECTOR, "iframe.xubox_iframe")
        self.pass_amount = (By.NAME, "income_amount")
        self.pass_status = (
            By.XPATH,
            "//input[@name='status' and @value='1']/following-sibling::span",
        )
        self.audit_remark = (By.CSS_SELECTOR, "textarea")
        self.verify_code = (By.NAME, "valicode")
        self.save_button = (By.CSS_SELECTOR, ".dybtn-save")

    @staticmethod
    def _application_row(username, remark=None):
        """根据用户名和可选备注生成额度申请行定位器。"""
        xpath = (
            "//tr[@ng-repeat='list in tableB']"
            f"[td[contains(@class,'member_name') and normalize-space()='{username}']]"
        )
        if remark:
            xpath += (
                f"[td[contains(@class,'remark') and normalize-space()='{remark}']]"
            )
        return (
            By.XPATH,
            xpath,
        )

    def open_credit_audit_page(self):
        """进入额度申请审核列表，并切换到主内容 iframe。"""
        self.base_switch_default()
        self.base_click(self.credit_manage_menu)
        self.base_click(self.credit_audit_menu)

        # 等 iframe 真正跳到额度申请列表后再切换，避免进入旧页面
        WebDriverWait(self.driver, self.default_timeout).until(
            lambda driver: "loan/amountapply/list"
            in driver.find_element(*self.content_iframe).get_attribute("src")
        )
        self.base_switch_iframe(self.content_iframe)

    def search_and_select_application(self, username, remark=None):
        """按用户名查询，并选中符合备注的待审核申请。"""
        self.base_input(self.search_username, username)
        old_rows = self.driver.find_elements(
            By.CSS_SELECTOR,
            "tr[ng-repeat='list in tableB']",
        )
        self.base_click(self.search_button)

        row = self._application_row(username, remark)
        try:
            # 查询会重新渲染表格，先等待旧行失效
            if old_rows:
                WebDriverWait(self.driver, self.default_timeout).until(
                    EC.staleness_of(old_rows[0])
                )

            # 每次重试都重新定位元素，避免点击已经失效的旧行对象
            def click_fresh_row(driver):
                try:
                    element = driver.find_element(*row)
                    if element.is_displayed() and element.is_enabled():
                        element.click()
                        return True
                except StaleElementReferenceException:
                    return False
                return False

            WebDriverWait(
                self.driver,
                self.default_timeout,
                ignored_exceptions=(StaleElementReferenceException,),
            ).until(click_fresh_row)
        except TimeoutException as error:
            raise AssertionError(
                f"没有找到 {username} 的指定待审核额度申请，请确认前置申请提交成功"
            ) from error

    def open_audit_dialog(self):
        """打开审核弹窗，并切换到审核表单 iframe。"""
        self.base_click(self.audit_button)
        self.base_switch_iframe(self.audit_iframe)

    def pass_application(self, amount, remark, verify_code):
        """填写审核信息并提交“通过”操作。"""
        self.base_input(self.pass_amount, amount)
        self.base_click(self.pass_status)
        self.base_input(self.audit_remark, remark)
        self.base_input(self.verify_code, verify_code)
        self.base_click(self.save_button)

    def is_application_pending(self, username, remark=None):
        """审核后重新查询指定申请是否仍在待审核列表。"""
        self.base_switch_default()
        wait = WebDriverWait(self.driver, self.default_timeout)

        # 保存成功后审核 iframe 会关闭；等待它关闭可避免过早查询
        wait.until(EC.frame_to_be_available_and_switch_to_it(self.content_iframe))
        wait.until(EC.invisibility_of_element_located(self.audit_iframe))

        self.base_input(self.search_username, username)
        old_rows = self.driver.find_elements(By.CSS_SELECTOR, "tr[ng-repeat='list in tableB']")
        self.base_click(self.search_button)

        # 查询会重新渲染表格，等待旧行失效后再判断最终结果
        if old_rows:
            wait.until(EC.staleness_of(old_rows[0]))

        # 等待 Angular 完成异步刷新，避免在新数据渲染前过早断言
        wait.until(
            lambda driver: driver.execute_script(
                """
                const node = document.querySelector('[ng-controller="tableCtrl"]');
                if (!node || !window.angular) return true;
                const scope = angular.element(node).scope();
                return !scope || scope.pageHide === true;
                """
            )
        )

        row = self._application_row(username, remark)
        return bool(self.driver.find_elements(*row))
