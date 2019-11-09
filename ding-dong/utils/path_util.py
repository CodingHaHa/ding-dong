# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 14:01
# @Author  : XiaoFeng
# @Email   : xiaofengcoding@163.com
# @Desc    : 文件路径工具类
# @File    : path_util.py

from constants.project_constants import PROJECT_NAME
from constants.project_constants import RESOURCES_DIR_NAME
from constants.project_constants import DATA_DIR_NAME
import os


def get_project_root_path():
    """
    获取项目根目录
    说明：兼容Windows系统，统一将路径分隔符处理为"/"
    :return:
    """
    cur_path = os.path.abspath(os.path.dirname(__file__))
    if cur_path.find("\\"):
        cur_path = str(cur_path).replace("\\", "/")
    # 截取到项目名称前/的路径
    root_path = cur_path[:cur_path.find(PROJECT_NAME + "/") + len(PROJECT_NAME + "/")]
    return root_path


def get_resources_dir_path():
    """
    获取项目资源文件目录
    :return:
    """
    return get_project_root_path() + "/" + PROJECT_NAME + "/" + RESOURCES_DIR_NAME


def get_data_dir_path():
    """
    获取数据文件目录路径
    :return:
    """
    return get_project_root_path() + "/" + PROJECT_NAME + "/" + DATA_DIR_NAME


if __name__ == "__main__":
    print(get_project_root_path())
