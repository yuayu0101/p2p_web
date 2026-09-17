import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    """为每条测试用例创建并关闭一个 Edge 浏览器。"""
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)

    # 统一设置浏览器窗口和隐式等待时间
    driver.maximize_window()
    driver.implicitly_wait(10)

    try:
        # yield 前是前置操作；测试执行完后继续执行 finally
        yield driver
    finally:
        driver.quit()
