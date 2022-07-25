# -*- coding:utf-8 -*-
"""
    Describe: 
    Author: liuyufeng
    Date: 2022-06-23 16:58
"""
import os


class GetRootPath(object):

    @staticmethod
    def getRootPath():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
