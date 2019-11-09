# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 13:25
# @Author  : XiaoFeng
# @Email   : xiaofengcoding@163.com
# @Desc    : 初始化服务类
# @File    : init_service.py

from constants.project_constants import DATA_DIR_NAME
from constants.project_constants import LOG_DIR_NAME
from utils.path_util import get_project_root_path
import os


def project_init():
    """
    项目初始化
    :return:
    """
    project_dirs_init()


def project_dirs_init():
    """
    初始化项目目录结构【数据目录、日志目录】
    :return:
    """
    project_root_path = get_project_root_path()
    project_data_path = project_root_path + DATA_DIR_NAME
    project_log_path = project_root_path + LOG_DIR_NAME
    if not os.path.exists(project_data_path):
        os.mkdir(project_data_path)
    if not os.path.exists(project_log_path):
        os.mkdir(project_log_path)