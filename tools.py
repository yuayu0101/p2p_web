import logging
import json
import logging.handlers
from selenium import webdriver

from config import PATH


class DriverTools:
    '''浏览器驱动类'''
    # 类属性
    driver = None

    @classmethod
    def get_driver(cls):  # 因为有@classmethod，所以cls相当于类本身Tools
        if cls.driver is None:
            options = webdriver.EdgeOptions()
            options.add_experimental_option("detach", True)
            # 启动Edge
            # (需要整个类共同保存和使用的变量加 cls.)
            cls.driver = webdriver.Edge(options=options)
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver

    '''关闭浏览器'''

    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None


def read_json(file_name):
    """
        读取json文件并且转换格式为[((),()),((),())]
    :param file_name: json文件名
    :return: 列表
    """
    data = []
    file_path = PATH + "\\data\\" + file_name#json文件路径
    with open(file_path, 'r', encoding='utf-8') as f:
        tmp = json.load(f)
        for i in tmp:
            a = tuple(i.values())
            data.append(a)
        return data


class GetLog:
    __log = None

    @classmethod
    def get_log(cls):
        if cls.__log is None:
            # 创建日志记录器
            cls.__log = logging.getLogger()
            # 设置入口级别
            cls.__log.setLevel(logging.INFO)
            filename = PATH + "/log/" + "web.log"
            tf = logging.handlers.TimedRotatingFileHandler(filename=filename,  # 日志文件名
                                                           when='midnight',  # 日志归档时间
                                                           interval=1,  # 每天归档一次
                                                           backupCount=3,  # 保留三天日志
                                                           encoding='utf-8')  # 日志文件编码
            # 获取格式器
            fmt = "%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s"
            formatter = logging.Formatter(fmt)
            # 将格式器添加到文件处理器
            tf.setFormatter(formatter)
            # 将文件处理器添加到日志记录器
            cls.__log.addHandler(tf)
        return cls.__log


if __name__ == "__main__":
    print(read_json("login_data.json"))

