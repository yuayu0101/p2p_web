from selenium.webdriver.common.by import By

from config import BASE_URL
from tools import DriverTools
from base.page_base import BasePage
from selenium.webdriver.support.wait import WebDriverWait


# 负责登录页面的元素和登录操作


class PageLogin(BasePage):
    def __init__(self, driver):  # self当前对象，当前类
        # 设置页面实例属性
        # self.driver = Tools.get_driver()
        # 重写父类的构造方法
        super().__init__(driver)
        '''其中先调用Tools.get_driver()创建并返回浏览器，再通过super().__init__()
        立即调用BasePage.__init__()，把浏览器和默认等待时间保存到lg
        对象中。随后回到PageLogin.__init__()，保存用户名、密码和登录按钮的定位器。'''

        # 设置页面实例属性

        self.username = (By.ID, "keywords")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-btn")

        # 成功结果元素属性
        self.fail_result = (By.CSS_SELECTOR, "#err span[ng-bind='loginErr']")
        self.success_result = (By.CLASS_NAME, "a-link1")

    def open_url(self, ):
        self.driver.get(BASE_URL + "/common/member/login")

    def login(self, username, password):
        # 输入账号
        # 加*是为了解包。因为上面属性有两个元素，需要解包
        # 只在当前函数用，不加 self；需要让对象的多个方法共同使用，就加 self。
        # ele=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username))
        self.base_input(self.username, username)
        # 输入密码
        self.base_input(self.password, password)

        # 点击登录
        # ele=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.login_button))
        self.base_click(self.login_button)

    def login_success(self, username, password):
        self.open_url()
        self.login(username, password)
        return self.get_success_result()

    def get_success_result(self):
        return WebDriverWait(self.driver, self.default_timeout).until(
            lambda driver: driver.find_element(*self.success_result).text.strip()
        )

    def get_fail_result(self):
        return WebDriverWait(self.driver, self.default_timeout).until(
            lambda driver: driver.find_element(*self.fail_result).text.strip()
        )


if __name__ == '__main__':
    lg = PageLogin(DriverTools.get_driver())  # lg是fd_element中的self
    # 打开页面
    lg.open_url()
    # 操作登录
    lg.login("13800001001", "Aa123456")
