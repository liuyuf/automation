# -*- coding:utf-8 -*-
"""
    Describe: 命令行执行项目命令
    Author: liuyufeng
    Date: 2022-05-30 15:54
"""
import subprocess
from BaseFunctions.getRootPath import GetRootPath
import time

casePath = "{0}/{1}".format(GetRootPath.getRootPath(), "TestCases")
allureName = "allure" + str(int(time.time()))
reportPath = "{0}/{1}/{2}".format(GetRootPath.getRootPath(), "ReportsCollection", allureName)

commandRunTest = 'pytest -s {0} --alluredir={1}'.format(casePath, reportPath)
commandReport = 'allure serve {0}'.format(reportPath)
sub = subprocess.Popen(commandRunTest, shell=True)

# 等待脚本结束，启动报告服务
while 1:
    if sub.poll() is not None:
        subprocess.Popen(commandReport, shell=True)
        break
