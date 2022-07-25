# -*- coding:utf-8 -*-
"""
    Describe: 
    Author: liuyufeng
    Date: 2022-06-21 12:36
"""
import os
import sys
from logbook import Logger, StreamHandler, TimedRotatingFileHandler
from BaseFunctions.getRootPath import GetRootPath


class LogBookClass(object):

    def __init__(self, modelName, caseName=""):
        """
        初始化日志文件路径
        :param modelName: 模块名称
        :param caseName: 用例名称
        """
        self.modelName = modelName
        self.caseName = caseName

        # 获取报告地址
        # self.filePathList = os.path.split(os.getcwd())
        self.reportPath = ''.join([GetRootPath.getRootPath(), "/Logs"])

        # 构建日志文件路径
        self.modelReportFile = "{0}/{1}".format(self.reportPath, self.modelName)

        # 创建日志文件夹
        if os.path.exists(self.modelReportFile) is not True:
            os.mkdir(self.modelReportFile)
        self.logFIlePath = "{0}/{1}".format(self.modelReportFile, "log.txt")

    def logRecider(self, level, logText):
        """
        实例化log句柄
        :param level:
        :param logText:
        :return:
        """
        level = level.upper()

        format_string = u'[{record.time:%Y-%m-%d %H:%M:%S.%f%z}] {record.level_name}:' \
                        u' {record.channel}: {record.message}'

        # 输出到console
        with StreamHandler(sys.stdout, format_string=format_string, encoding='utf-8', level=level) as header:
            self.chooseLevel(header.level_name, logText)

        # 输出到文件
        with TimedRotatingFileHandler(self.logFIlePath, encoding='utf-8', level=level,
                                      format_string=format_string, date_format='%Y-%m-%d %H:%M') as header:
            self.chooseLevel(header.level_name, logText)

    def chooseLevel(self, level, logText):
        """
        根据日志等级返回对应日志操作
        :param level:
        :param logText:
        :return:
        """
        logText = self.caseName + ": " + logText

        if level == 'INFO':
            return Logger(self.modelName).info(logText)
        elif level == 'DEBUG':
            return Logger(self.modelName).debug(logText)
        elif level == 'ERROR':
            return Logger(self.modelName).error(logText)


if __name__ == '__main__':
    l = LogBookClass("systest_2")
    l.logRecider("info", "this is test")
