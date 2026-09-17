#数据驱动最适合在“功能流程已经跑通，并且需要用很多组数据重复验证”的时候使用。
#1.构造数据（json） 先写[],再写{} eg如下
[
  {
    "title": "登录成功",
    "username": "测试账号1",
    "password": "正确密码",
    "expected": "测试账号1",
    "success": True#在json文件里面要小写
  },
  {
    "title": "密码错误",
    "username": "专用测试账号",
    "password": "错误密码",
    "expected": "密码错误",
    "success": False#在json文件里面要小写
  }
]
#2.读取数据（在tools里面写）
import json
import os

from config import PATH


def read_json(file_name):
    file_path = os.path.join(PATH, "data", file_name)

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
#3.参数化调用（在测试类里面写）
import pytest

from tools import read_json


class TestLogin:

    @pytest.mark.parametrize(
        "case",
        read_json("login_data.json"),
        ids=lambda case: case["title"]
    )
    def test_login(self, case):
        self.page_login.login(
            case["username"],
            case["password"]
        )

        if case["success"]:
            actual = self.page_login.get_success_result()
        else:
            actual = self.page_login.get_fail_result()

        assert case["expected"] in actual