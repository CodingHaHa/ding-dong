# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 17:34
# @Author  : XiaoFeng
# @Email   : xiaofengcoding@163.com
# @Desc    : 任务清单实体
# @File    : checklist_entity.py

class ChecklistItem:
    """
    任务清单条目类
    """

    def __init__(self, itemName, itemType, itemTime):
        self.itemTime = itemTime
        self.itemType = itemType
        self.itemName = itemName


