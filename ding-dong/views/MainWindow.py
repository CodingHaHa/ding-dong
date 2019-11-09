# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 16:51
# @Author  : XiaoFeng
# @Email   : xiaofengcoding@163.com
# @Desc    : 主窗体
# @File    : MainWindow.py

from PyQt5.Qt import *
import sys
from utils.path_util import get_resources_dir_path

# 创建一个GUI应用
# 注意：需要传递参数sys.argv
app = QApplication(sys.argv)

# 创建一个窗体
window = QWidget()
# 设置窗体的标题
window.setWindowTitle("滴答")
window.setObjectName("MainWindow")
window.setStyleSheet("#MainWindow{background-color: #CDC5BF}")

window.setWindowIcon(QIcon(get_resources_dir_path()+"/images/checklist.png"))

# 设置窗体的大小
window.resize(550, 700)
# 移动窗体的位置
window.move(400, 200)

# 在窗体上创建一个标签
label = QLabel(window)
# 设置标签的内容
label.setText("滴答，欢迎您!")
# 移动标签的位置
label.move(200, 200)

# 主窗体需要进行显示
window.show()

# 程序退出:进入程序的主循环，并通过exit()函数确保主循环安全的结束
sys.exit(app.exec_())
