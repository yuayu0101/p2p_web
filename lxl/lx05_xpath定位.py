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

driver.get("https://hmshop-test.itheima.net/Home/user/login.html")

driver.find_element(By.XPATH, "//*[@id='username']").send_keys("13800000001")
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("123456")
driver.find_element(By.XPATH, "//*[@id='verify_code']").send_keys("8888")

driver.find_element(By.CLASS_NAME, "J-login-submit").click()

print("页面标题：", driver.title)
#断言
assert "会员中心" in driver.title
