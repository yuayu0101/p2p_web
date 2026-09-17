#在setting部署好就不用写其他的。直接输入ui就行
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 关键配置：脚本结束浏览器不关闭
# Edge浏览器配置
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

# 启动Edge
driver = webdriver.Edge(options=options)
driver.maximize_window()

driver.get("https://hmshop-test.itheima.net/")
# driver.find_element(by=By.LINK_TEXT, value="登录").click()
driver.find_element(by=By.PARTIAL_LINK_TEXT, value="登").click()

print("页面标题：", driver.title)