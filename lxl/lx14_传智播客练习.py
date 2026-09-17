import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# Edge浏览器配置
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

# 启动Edge
driver = webdriver.Edge(options=options)
driver.maximize_window()

#输入网址
driver.get("http://121.43.169.97:8081/")
#页面操作
#①点击注册按钮
driver.find_element(By.LINK_TEXT, '有奖注册').click()

#②点击注册信息
driver.find_element(By.ID, 'phone').send_keys('13800001001')
driver.find_element(By.ID,'password').send_keys('Aa123456')
driver.find_element(By.ID, 'verifycode').send_keys('8888')
driver.find_element(By.ID,'get_phone_code').click()
driver.find_element(By.ID,'phone_code').send_keys('666666')
driver.find_element(By.CLASS_NAME,'lg-btn').click()

#断言
results=driver.find_element(By.CSS_SELECTOR,'div.reg-step-last > h1').text
print(results)
time.sleep(5)
driver.quit()



