
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 关键配置：脚本结束浏览器不关闭
#浏览器配置
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

# 1启动Edge
driver = webdriver.Edge(options=options)
driver.maximize_window()

driver.get("https://hmshop-test.itheima.net/Admin/Admin/login")
#4页面操作
#4.1登录成功
driver.find_element(By.NAME, value="username").send_keys("test1")
driver.find_element(By.NAME, value="password").send_keys("123456")
driver.find_element(By.ID, value="vertify").send_keys("8888")
#显示等待+登录成功
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/form/div/div[1]/div[2]/div[5]/span/input"))).click()#点击登录并且显示等待了
#4.2进入账户设置
ele=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='账户设置']")))
#4.3鼠标悬停
ActionChains(driver).move_to_element(ele).perform()
#
#4.4再去点击收获地址
driver.find_element(By.XPATH, "//a[2][text()='收获地址']").click()
#4.5点击新增收获地址
driver.find_element(By.CLASS_NAME,value="co_blue").click()
#4.6添加收货人
driver.find_element(By.NAME, value="consignee").send_keys("张三")
#4.7添加手机号
driver.find_element(By.NAME, value="mobile").send_keys("12345678901")
#4.8添加收获地址代码(下拉框)
Select(driver.find_element(By.ID, "province")).select_by_value("1")
Select(driver.find_element(By.ID, "city")).select_by_value("2")
Select(driver.find_element(By.ID, "district")).select_by_value("0")
#4.9添加详细地址
driver.find_element(By.CSS_SELECTOR, "input[placeholder='详细地址']").send_keys("上海")
driver.find_element(By.NAME, value="zipcode").send_keys("200000")

print("页面标题：", driver.title)

#如果单独没有问题。全部加起来运行有问题。可能是时间太快了。加time.sleep就行