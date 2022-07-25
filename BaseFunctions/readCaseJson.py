# -*- coding:utf-8 -*-
"""
    Describe: 解析JSON用例
    Author: liuyufeng
    Date: 2022-06-23 10:53
"""
import json
import os
from BaseFunctions.getRootPath import GetRootPath


class ReadCaseJson(object):
    def __init__(self, modelName, jsonCaseName):
        self.paramJsonRootPath = ''.join([GetRootPath.getRootPath(), "/ParametersCollection/", modelName])

        if '.json' not in jsonCaseName:
            jsonCaseName = ''.join([jsonCaseName, '.json'])

        self.jsonPath = os.path.join(self.paramJsonRootPath, jsonCaseName)
        with open(self.jsonPath, "r", encoding="utf-8") as f:
            self.json_dict = json.load(f)

    def getItem(self):
        return self.json_dict

    def getCaseItem(self, caseName):
        return self.getItem()[caseName]


if __name__ == '__main__':
    reItem = ReadCaseJson("userRelated", "loginParam")
    print(reItem.getCaseItem("Login_success"))
