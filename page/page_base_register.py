from base.page_base import BasePage
from selenium.webdriver.common.by import By

from config import BASE_URL
import time

class PageRegister(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.phone = (By.ID, "phone")
        self.pwd = (By.ID, "password")
        self.img_code = (By.ID, "verifycode")
        self.phone_click = (By.ID, "get_phone_code")
        self.phone_code = (By.ID, "phone_code")
        self.reg=(By.CLASS_NAME,"lg-btn")
        self.success_result=(By.CSS_SELECTOR,"div.reg-step-last > h1")
        self.fail_result=(By.XPATH,"//*[contains(text(),'手机已存在')]")

    def open_url(self):
        self.driver.get(BASE_URL+"/common/member/reg")

    def register(self,phone,pwd,img_code,phone_code):
        self.base_input(self.phone,phone)
        self.base_input(self.pwd,pwd)
        self.base_input(self.img_code,img_code)
        self.base_click(self.phone_click)
        time.sleep(2)
        self.base_input(self.phone_code,phone_code)
        self.base_click(self.reg)

    def get_success_result(self):
        # 成功区域受页面样式影响，.text 可能为空，读取 textContent 更稳定
        return self.fd_element(self.success_result).get_attribute("textContent").strip()

    def get_fail_result(self):
        return self.fd_element(self.fail_result).text.strip()
