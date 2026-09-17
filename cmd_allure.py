import os

#生成离线报告
run_cmd="allure generate ./report -o ./new_report --clean"
os.system(run_cmd)
#通过os.system()执行命令
#allure generate :生成allure测试报告中的命令
#./report :测试报告的路径
#-o :指定生成的报告路径p
#--clean :清理报告路径
##

#批量执行测试脚本
# pytest
# 通过终端生成测试报告
# python cmd_allure.py
