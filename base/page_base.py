from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
from config import PATH
from tools import GetLog


# 负责公共操作、例如等待并且查找元素
class BasePage(object):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.default_timeout = timeout

    # 定位元素
    def fd_element(self, loc):
        """
        查找元素，loc是元组，包含元素定位方式和定位表达式
        :param loc:     元素定位方式和定位表达式
        :return: 定位到的元素
        :except:       元素定位方式或定位表达式错误，抛出异常
        :raise 主动抛出异常
        """
        try:
            element = WebDriverWait(self.driver, self.default_timeout).until(EC.presence_of_element_located(loc))
            return element
        except Exception as e:
            GetLog.get_log().error(f"元素定位失败,{loc},{e}")
            raise

    # 输入
    def base_input(self, loc, text):
        '''
        输入文本
        :param loc: 元素定位方式和定位表达式
        :param text: 输入的文本
        :return:
        '''
        # 定位元素
        ele = self.fd_element(loc)
        # 清空输入框
        ele.clear()
        # 输入内容
        ele.send_keys(text)

    # 点击
    def base_click(self, loc):
        """
        点击元素
        :param loc: 元素定位方式和定位表达式
        :return:
        """
        WebDriverWait(self.driver, self.default_timeout).until(EC.element_to_be_clickable(loc)).click()

    # 获取文本
    def base_get_text(self, loc):
        """
        获取元素文本
        :param loc: 元素定位方式和定位表达式
        :return: 去除前后空格后的文本
        """
        return self.fd_element(loc).text.strip()

    # 截图
    def get_shot(self, file_name):
        file_path = os.path.join(PATH, "img", file_name)
        self.driver.save_screenshot_as_file(file_path)

    # 切换窗口

    def base_switch_handle(self, loc):
        """
        切换窗口
        :param loc: 元素定位方式和定位表达式
        :return:
        """
        old_handle = self.driver.current_window_handle
        try:
            WebDriverWait(self.driver, self.default_timeout).until(lambda x: len(x.window_handles) > 1)
            handles = self.driver.window_handles
            for handle in handles:
                if handle != old_handle:
                    self.driver.switch_to.window(handle)
                    break
        except TimeoutException:
            self.driver.switch_to.window(old_handle)
        # 切换到新窗口就行定位
        element = self.fd_element(loc)

        return element

    # 切换iframe
    def base_switch_iframe(self, loc):
        """
        切换iframe
        :param loc: 元素定位方式和定位表达式
        :return:
        """
        frame_ele = self.fd_element(loc)
        self.driver.switch_to.frame(frame_ele)

    # 切换到默认窗口
    def base_switch_default(self):
        """
        切换到默认窗口
        :return:
        """
        self.driver.switch_to.default_content()
