import os

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    """为每条测试用例创建并关闭一个 Edge 浏览器。"""
    options = webdriver.EdgeOptions()

    # Jenkins runs as a Windows service without an interactive desktop.
    if os.getenv("JENKINS_URL") or os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Edge(options=options)

    # 统一设置浏览器窗口和隐式等待时间
    if not (os.getenv("JENKINS_URL") or os.getenv("CI")):
        driver.maximize_window()
    driver.implicitly_wait(10)

    try:
        # yield 前是前置操作；测试执行完后继续执行 finally
        yield driver
    finally:
        driver.quit()
