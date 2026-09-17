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
#4页面操作#获取元素对象
driver.find_element(by=By.ID, value="username").send_keys("admin")
driver.find_element(by=By.CLASS_NAME, value="J-login-submit").click()




# 打印页面标题，看有没有成功打开网页
print("页面标题：", driver.title)

# 调试阶段：不要写 driver.quit()


