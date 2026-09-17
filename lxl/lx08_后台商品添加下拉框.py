from selenium.webdriver.support import expected_conditions as EC, select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
#浏览器配置
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

# 1启动Edge
driver = webdriver.Edge(options=options)
driver.maximize_window()
#2.登录
driver.get("https://hmshop-test.itheima.net/Admin/Admin/login")#链接地址可能后期会改
driver.find_element(By.NAME, value="username").send_keys("test1")
driver.find_element(By.NAME, value="password").send_keys("123456")
driver.find_element(By.ID, value="vertify").send_keys("8888")
driver.find_element(By.XPATH, "/html/body/div[1]/form/div/div[1]/div[2]/div[5]/span/input").click()

#显示等待
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "商城")))
#点击商城
driver.find_element(By.LINK_TEXT, "商城").click()
#3需要进入进入Frame
fr=driver.find_element(By.I, value="workspace")
driver.switch_to.frame("fr")

driver.find_element(By.XPATH,"//*[text()='添加商品'" ).click()
#eg:<a>添加商品</a>才用文本

#4返回原来的内容
driver.switch_to.default_content()

#5填写商品信息（下拉框）
#商品名称
driver.find_element(By.NAME, value="goods_name").send_keys("测试商品")
#选择种类
select1=Select(driver.find_element(By.NAME, value="cat_id"))
select1.select_by_visible_text("手机")
#或者select.select_by_index(1)
#或者select.select_by_value("1")
#选择运营商
select2=Select(driver.find_element(By.NAME, value="cat_id_2"))
select2.select_by_visible_text("运营商")
#商品分类
select3=Select(driver.find_element(By.NAME, value="cat_id_3"))
select3.select_by_visible_text("办套餐")

#6.填写商品价格
driver.find_element(By.NAME, "shop_price").send_keys("100")
driver.find_element(By.NAME, "market_price").send_keys("200")
#是否包邮
driver.find_element(By.ID, value="is_free_shipping_label_1").click()
#确认提交
driver.find_element(By.ID, value="submit").click()

driver.quit()#退出浏览器



