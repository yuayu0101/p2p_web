
# 导入固定包
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#显示等待
"""#打开网页后面（NoSuchElementException异常情况）
##隐式等待（只用一次全局有效）WebDriver.implicitly_wait(秒数)

#显示等待（只对指定元素生效）主要写在写在打开网页之后、点击或输入之前。
（异常情况TimeoutException）
1.元素 = WebDriverWait(driver, 秒数).until(
    EC.条件名称((By.定位方式, "定位内容"))
)#最多等10秒，找到ID叫 login 的东西，等它能点击后，把它交给 button。

写法2：
元素 = WebDriverWait(driver, 等待秒数).until(
    lambda 浏览器: 浏览器.find_element(定位方式, "定位内容")
)最多等待秒数，不断让浏览器查找定位方式为定位内容，找到以后交给 元素。

 {###条件名称
你想等待什么	条件名称
@元素出现在HTML中	presence_of_element_located
@等元素看得见	visibility_of_element_located
@等元素看得见且能点击	element_to_be_clickable
元素消失	invisibility_of_element_located
等待页面出现‘指定文字’	text_to_be_present_in_element
网页标题包含某段文字	title_contains
进入新的iframe	frame_to_be_available_and_switch_to_it
}"""


#1 Edge浏览器配置
'''
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

# 启动Edge
driver = webdriver.Edge(options=options)
driver.maximize_window()
'''

#标签.类名 > 子标签  (页面上有很多相同标签，或者目标元素没有ID时，通过它外面的父元素来准确找到它
'''eg:
<h1>商城首页</h1>
<div class="login">
    <h1>会员登录</h1>
</div>
<div class="success">
    <h1>注册成功</h1>
</div>

#找注册成功这句话
driver.find_element(
    By.CSS_SELECTOR,
    "div.success > h1"
)
找到 class 叫 success 的 div 盒子，再找到它里面的 h1 大标题
'''


#2.打开网页
'''driver.get("https://目标网址.com")'''

#3页面操作（定位元素）##标签太多了
'''
By.ID         →  根据 id="xxx"        例如 By.ID, value="username"
By.NAME       →  根据 name="xxx"      例如 By.NAME, value="username"
By.CLASS_NAME →  根据 class="xxx"(只是点击)     例如 By.CLASS_NAME, value="J-login-submit"（只能写一个值）
By.TAG_NAME   →  根据 标签名          例如 By.TAG_NAME, value="button"
By.LINK_TEXT  →  根据链接文本（只有<a>标签kysy）     例如 By.LINK_TEXT, value="登录"(全部文本信息<a>黑马程序员<a>)
By.PARTIAL_LINK_TEXT →  根据链接文本的一部分  例如 By.PARTIAL_LINK_TEXT, value="登"
By.CSS_SELECTOR →  根据 CSS选择器     例如 By.CSS_SELECTOR, value="input[name='username']"
By.XPATH      →  根据 XPath     例如 By.XPATH, value="//*[@id='username']"


 浏览器对象.find_element (By. 定位方式（这个要求要大写），value="属性值")
eg:<input type="text" name="username" id="username">
driver.find_element(By.ID, value="username").send_keys("admin")输入
driver.find_element(By.CLASS_NAME, value="J-login-submit").click()点击
driver.find_element(By.CSS_SELECTOR, value="CSS表达式")CSS选择器,class可以执行多个
driver.find_element(By.XPATH, value="XPath表达式")XPath

{CSS表达式
eg:class="btn primary active"
     找任意一个：.btn
     同时找多个：.btn.primary.active
    多个 class 之间不要加空格

##  ID 选择器（#）
CSS 表达式：`#username`意思就是找页面中的id='username'的元素
##  类 选择器（.）
CSS 表达式：`.username`意思就是找页面中的class='username'的元素
##  标签 选择器
CSS 表达式：`input`意思就是找页面中的所有input标签
##  属性  选择器
CSS 表达式：`[name='username']`意思就是找页面中所有name='username'的元素
##  组合  选择器
CSS 表达式：`#username[name='username']`意思就是找页面中id='username'且name='username'的元素
}


{XPath选择定位  //：表示从根节点开始查找 /：表示只找一层
driver.find_element(By.XPATH, "XPath表达式")
XPath表达式：//标签名[@属性名='属性值' and @属性名='属性值']
标签名：input，button，form等
属性名：id，name，class，type等

//标签名[text()='文本内容'](这种方法一般是为了找不到标签名写的)
driver.find_element(By.CSS_SELECTOR, "form 标签名")#不受空格和文字的影响


}
#操作这个已经拿到的元素（上面或者下面都可以）
变量名.send_keys (要输入的内容,输入内容都是用这个)
ele.send_keys("admin")
ele.click()#这个是点击操作
'''


#4.添加商品
'''
driver.switch_to.frame() 一般在这种情况下使用：
你要操作的按钮、输入框或文字，位于 <iframe> 标签内部。


进入前要找iframe fr=driver.find_element(By.ID, "iframe_id")
driver.switch_to.frame(iframe)       # 进入iframe
driver.switch_to.default_content()   # 退出iframe，返回主页

#返回原来的内容
driver.switch_to.default_content()
'''


#5.Select下拉框（这个就不要加显示等待了）
'''
 #创建对象
select=Select(driver.find_element(By.ID, "id"))`"id"` 是占位示例，写脚本时要替换成网页真实 id。
# 可以这样子写Select(driver.find_element(By.ID, "id")).select_by_visible_text("北京")
 # #根据页面显示的文字选择
select.select_by_visible_text("北京")

 # # 根据 option 的 value 选择
select.select_by_value("bj")

 # # 根据位置选择，从 0 开始
select.select_by_index(0)
'''

#6.鼠标悬停（找到菜单元素之后，点击悬停后出现的子菜单之前。）
"""
ActionChains(driver).move_to_element(网页元素).perform()
eg:
<div id="menu">商品分类</div>

menu = driver.find_element(By.ID, "menu")
ActionChains(driver).move_to_element(menu).perform()
找到ID为 menu 的商品分类，然后把鼠标移动到它上面。
"""

#7弹出框
'''
弹出框变量(自己写的) = driver.switch_to.alert
弹出框变量.操作方法()
eg:
弹出框变量.accept()#点击确定
弹出框变量.dismiss()#点击取消
弹出框变量.send_keys("文本")#输入文本
弹出框变量.text#获取文本

'''

#8.滚动条
'''
# 滚动到指定元素
driver.execute_script("arguments[0].scrollIntoView();", 元素)

eg：
element = driver.find_element(By.ID, "submitButton")
driver.execute_script(
    "arguments[0].scrollIntoView();",
    element
)

# 滚动到指定高度
driver.execute_script("window.scrollTo(水平位置, 垂直位置)")

# 滚动到页面底部
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
'''

#9多窗口
'''
窗口列表(zjqm) = driver.window_handles #获取所有窗口的列表
driver.switch_to.window(窗口列表[下标]) #切换到指定窗口
'''

#10搜索操作截图
'''
# 截整个页面
driver.save_screenshot("页面截图.png")
eg：
driver.get("https://www.baidu.com")
driver.save_screenshot("百度页面.png")

# 截取一个元素
element.screenshot("元素截图.png")

'''


#11.判断是否被选中
'''复选框、单选按钮、下拉框中的选项
ele = driver.find_element(By.ID, "id")#找到元素
元素.is_selected()#判断元素是否被选中
元素.is_enabled()   # 能不能使用
元素.is_displayed() # 看不看得见
'''

#12.浏览器其他操作
'''
driver.refresh()  # 刷新
driver.back()     # 后退
driver.forward()  # 前进
'''



# .关闭浏览器
'''driver.quit()'''


