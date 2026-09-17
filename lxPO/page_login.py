from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tools import Tools

class PageLogin():
    def __init__(self):#self当前对象，当前类
        #设置页面实例属性
        self.driver = Tools.get_driver()
        self.username = (By.ID,"keywords")
        self.password = (By.ID,"password")
        self.login_button = (By.ID,"login-btn")

    def open_url(self):
        self.driver.get("http://121.43.169.97:8081/common/member/login")

    def login(self):
        #输入账号
        #加*是为了解包。因为上面属性有两个元素，需要解包
        #只在当前函数用，不加 self；需要让对象的多个方法共同使用，就加 self。
        ele=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username))
        ele.send_keys("13800001001")
        #输入密码
        (WebDriverWait(self.driver, 10)
         .until(EC.visibility_of_element_located(self.password)).send_keys("Aa123456"))

        #点击登录
        ele=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.login_button))
        ele.click()


if __name__ == '__main__':
     lg=PageLogin()
     #打开页面
     lg.open_url()
     #操作登录
     lg.login()