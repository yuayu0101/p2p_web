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

#4页面操作
#4.1注册
driver.find_element(By.ID,value="userA").send_keys("lyh")
driver.find_element(By.ID,value="passwordA").send_keys("123456")
driver.find_element(By.CSS_SELECTOR,value=".telA").send_keys("12345678901")
driver.find_element(By.CSS_SELECTOR,value=".emailA.dzyxA").send_keys("12346@qq.com")
driver.find_element(By.CSS_SELECTOR, "form button").click()
#下拉框
select = Select(driver.find_element(By.NAME, value="selecta"))
select.select_by_visible_text("深圳")
#弹出框

#找到alert按钮并且滚动到alert按钮上加点击
alert1=driver.find_element(By.ID,value="alerta")
driver.execute_script(
    "arguments[0].scrollIntoView();",
    alert1
)
alert1.click()

#处理框信息
alert = driver.switch_to.alert
time.sleep(2)
alert.accept()


print("页面标题：", driver.title)