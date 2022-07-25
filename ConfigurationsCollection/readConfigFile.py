# -*- coding:utf-8 -*-
"""
    Describe: 
    Author: liuyufeng
    Date: 2022-05-30 16:17
"""
import configparser
from BaseFunctions.getRootPath import GetRootPath


class ReadConfig(object):

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_Path = "{0}/{1}".format(GetRootPath.getRootPath(), "ConfigurationsCollection/config.ini")
        self.config.read(self.config_Path, encoding="utf-8")

    def get_ini_sections(self):
        """
        获取所有的节点名称
        :return:
        """
        return self.config.sections()

    def get_section_keys(self, section):
        """
        返回节点下所有的key
        :param section:
        :return:
        """
        return self.config.options(section)

    def get_section_items(self, section):
        """
        返回节点下的键值对
        :param section:
        :return:
        """
        return self.config.items(section)

    def get_sectionKey_value(self, section, key):
        """
        返回指定节点下的key的值
        :return:
        """
        try:
            return self.config.get(section, key)
        except Exception as e:
            print(section)
            print(key)
            print("输入的key不存在，请检查")


if __name__ == '__main__':
    t = ReadConfig()
    c = t.get_ini_sections()
    print(c)
