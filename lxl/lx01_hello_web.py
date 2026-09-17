from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# 方式1：原始字符串 r"" 解决路径转义问题
path = r'C:\py\python\chromedriver.exe'

# selenium4 必须用Service传入驱动路径
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

# 测试打开网页
driver.get("https://www.baidu.com")
time.sleep(10)
print(driver.title)

# 关闭
driver.quit()



