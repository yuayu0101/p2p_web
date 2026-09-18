import os
import shutil
import tempfile

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    """为每条测试用例创建并关闭一个 Edge 浏览器。"""
    options = webdriver.EdgeOptions()
    is_ci = bool(os.getenv("JENKINS_URL") or os.getenv("CI"))
    profile_dir = None

    # Jenkins runs as a Windows service without an interactive desktop.
    if is_ci:
        profile_dir = tempfile.mkdtemp(prefix="jenkins-edge-")
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--remote-debugging-pipe")
        options.add_argument("--window-size=1920,1080")
        options.add_argument(f"--user-data-dir={profile_dir}")

    try:
        driver = webdriver.Edge(options=options)
    except Exception:
        if profile_dir:
            shutil.rmtree(profile_dir, ignore_errors=True)
        raise

    # 统一设置浏览器窗口和隐式等待时间
    if not is_ci:
        driver.maximize_window()
    driver.implicitly_wait(10)

    try:
        # yield 前是前置操作；测试执行完后继续执行 finally
        yield driver
    finally:
        driver.quit()
        if profile_dir:
            shutil.rmtree(profile_dir, ignore_errors=True)
