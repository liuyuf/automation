# -*- coding:utf-8 -*-
"""
    Describe: 从URL中组装一个名称
    Author: liuyufeng
    Date: 2022-07-25 11:51
"""


def reName(strPath):
    strList = strPath.split("/")
    if len(strList) > 2:
        combinationName = ''.join([i.title() for i in strList[-2:]])
    elif len(strList) <= 2 and len(strList) != 0:
        combinationName = ''.join(strList)
    else:
        combinationName = "NameIsError"
    return combinationName
