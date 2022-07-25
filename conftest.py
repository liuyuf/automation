# -*- coding:utf-8 -*-
"""
    Describe: 组装request
    Author: liuyufeng
    Date: 2022-06-24 15:06
    demonstration:

        class TestClass(object):
            Basedata = readCaseJson.ReadCaseJson("modelName", "jsonCaseName").getItem()
            ids = [i["name"] for i in Basedata]

            @pytest.mark.parametrize("AssemblyRequest", Basedata, ids=ids, indirect=True)
        def test_one(self, AssemblyRequest):
            rel = AssemblyRequest
            assert rel.json()["StatusCode"] == 200
"""
import pytest
import requests
import json
from ConfigurationsCollection.readConfigFile import ReadConfig
from ConfigurationsCollection.configLogging import LogBookClass
from BaseFunctions.reName import reName


@pytest.fixture
def SessionLogin(request):
    """
    1、前置后置方法
    2、负责提供session
    :param request:
    :return:
    """
    host = ReadConfig().get_sectionKey_value("HTTP", 'base_host')
    timeout = ReadConfig().get_sectionKey_value("HTTP", 'timeout')

    session = requests.session()
    login_url = host + "/api/v1/index/login"

    headers = {
        "Content-Type": "application/json"
    }

    login_data = {
        "mobileZone": "86",
        "mobile": "1888888888",
        "verifyCode": "1528"
    }
    rel = session.post(url=login_url, headers=headers, data=json.dumps(login_data), timeout=float(timeout))

    session.headers.update({'x-token': rel.json()["data"]["token"]})

    def logout():
        logout_url = host + "/api/v1/user/logout"
        session.post(url=logout_url)

    request.addfinalizer(logout)

    return session


@pytest.fixture
def AssemblyRequest(request, SessionLogin):
    host = ReadConfig().get_sectionKey_value("HTTP", 'base_host')
    timeout = ReadConfig().get_sectionKey_value("HTTP", 'timeout')

    Basedata = request.param

    url = Basedata["url"]
    method = Basedata["method"]
    headers = Basedata["headers"]

    logger = LogBookClass(reName(url), Basedata["name"])

    testUrl = host + url

    if headers["Content-Type"].__contains__("application/json"):
        data = json.dumps(Basedata["param"])
    else:
        data = Basedata["param"]

    # 默认文件为FALSE
    files = None
    if Basedata.get("files") is not None:
        files = Basedata["files"]

    # 1、先将有效token保存到变量中
    # 2、如果case里有'x-token', 则使用它；没有则继续使用有效的token
    effectiveToken = SessionLogin.headers["x-token"]

    if Basedata.get("x-token") is None:
        SessionLogin.headers.update({'x-token': effectiveToken})
    else:
        customToken = Basedata["x-token"]
        SessionLogin.headers.update({'x-token': customToken})

    if method == "POST":
        try:
            re = SessionLogin.post(url=testUrl, data=data, headers=headers, files=files, timeout=float(timeout))
            logger.logRecider("INFO", "POST {0} 成功".format(testUrl))
            return re
        except Exception as e:
            logger.logRecider("ERROR", e)

    elif method == "GET":
        try:
            re = SessionLogin.post(url=testUrl, params=data, headers=headers, files=files, timeout=float(timeout))
            logger.logRecider("INFO", "POST {0} 成功".format(testUrl))
            return re
        except Exception as e:
            logger.logRecider("ERROR", e)
    else:
        logger.logRecider("ERROR", "请求方式错误")
        raise Exception("请求方式错误")
