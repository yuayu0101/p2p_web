from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

# 启动Edge
driver = webdriver.Edge(options=options)
driver.maximize_window()

driver.get("https://hmshop-test.itheima.net/Admin/Admin/login")#链接地址可能后期会改
driver.find_element(By.NAME, value="username").send_keys("test1")
driver.find_element(By.NAME, value="password").send_keys("123456")
driver.find_element(By.ID, value="vertify").send_keys("8888")
driver.find_element(By.XPATH, "/html/body/div[1]/form/div/div[1]/div[2]/div[5]/span/input").click()
#点击添加商品
# 添加商品
time.sleep(1)#让程序停留
#需要进入进入Frame
fr=driver.find_element(By.I, value="workspace")
driver.switch_to.frame("fr")

driver.find_element(By.XPATH,"//*[text()='添加商品'" ).click()
#eg:<a>添加商品</a>才用文本

