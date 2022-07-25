# # -*- coding:utf-8 -*-
# """
#     Describe:
#     Author: liuyufeng
#     Date: 2022-07-11 18:19
# """
import pytest
from BaseFunctions import readCaseJson


class TestAccount(object):

    Basedata = readCaseJson.ReadCaseJson("userRelated", "newJsonype_2").getItem()
    ids = [i["name"] for i in Basedata]

    @pytest.mark.parametrize("AssemblyRequest", Basedata, ids=ids, indirect=True)
    def test_11(self, AssemblyRequest):
        rel = AssemblyRequest
        print(rel.json())
        assert 1 == 1
