from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 关键配置：脚本结束浏览器不关闭
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://hmshop-test.itheima.net/Home/user/login.html")

# 4页面操作#获取元素对象
driver.find_element(by=By.CSS_SELECTOR, value="#username").send_keys("admin")
driver.find_element(by=By.CSS_SELECTOR, value="input[name='password']").send_keys("123456")
driver.find_element(by=By.CSS_SELECTOR, value="input[name='verify_code']").send_keys("8888")
#点击
driver.find_element(by=By.CSS_SELECTOR, value=".J-login-submit").click()

print("页面标题：", driver.title)
