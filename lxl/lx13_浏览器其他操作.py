from lark.parsers.earley_forest import handles_ambiguity
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.select import Select
import time
# 关键配置：脚本结束浏览器不关闭
# Edge浏览器配置
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

# 启动Edge
driver = webdriver.Edge(options=options)
driver.maximize_window()

driver.get("http://121.43.169.97:8848/pageA.html")
baidu = driver.find_element(By.ID, "fw")


driver.execute_script(
    "document.documentElement.scrollTop = arguments[0].offsetTop;",
    baidu
)
baidu.click()
handles=driver.window_handles
driver.switch_to.window(handles[1])

driver.refresh()  # 刷新
driver.back()     # 后退
driver.forward()  # 前进