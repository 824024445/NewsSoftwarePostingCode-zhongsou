# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from foo import commu_econo
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import begin
from matplotlib_examples.spiders.examples import assi_value


class Ui_Post(object):
    onesingal = pyqtSignal(str)

    def setupUi(self, Post):
        Post.setObjectName("Post")
        Post.resize(611, 462)
        self.label = QtWidgets.QLabel(Post)
        self.label.setGeometry(QtCore.QRect(30, 20, 51, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Post)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 51, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Post)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 51, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Post)
        self.label_4.setGeometry(QtCore.QRect(90, 50, 501, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Post)
        self.label_5.setGeometry(QtCore.QRect(90, 62, 441, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Post)
        self.label_6.setGeometry(QtCore.QRect(90, 30, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Post)
        self.label_7.setGeometry(QtCore.QRect(90, 95, 54, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Post)
        self.label_8.setGeometry(QtCore.QRect(90, 170, 54, 21))
        self.label_8.setObjectName("label_8")
        self.urled = QtWidgets.QLineEdit(Post)
        self.urled.setGeometry(QtCore.QRect(170, 30, 371, 21))
        self.urled.setObjectName("urled")
        # self.urled.editingFinished.connect(self.SendUr())
        self.keyword = QtWidgets.QComboBox(Post)
        self.keyword.setGeometry(QtCore.QRect(140, 95, 81, 20))
        self.keyword.setObjectName("keyword")
        self.keyword.addItem("")
        self.keyword.addItem("")
        self.keyword.addItem("")
        self.keyword.addItem("")
        self.keyword.addItem("")
        self.pagenumber = QtWidgets.QLineEdit(Post)
        self.pagenumber.setGeometry(QtCore.QRect(150, 170, 61, 20))
        self.pagenumber.setObjectName("pagenumber")
        self.delete_record = QtWidgets.QPushButton(Post)
        self.delete_record.setGeometry(QtCore.QRect(90, 130, 75, 21))
        self.delete_record.setObjectName("delete_record")
        self.delete_record.clicked.connect(lambda :self.Delete_record(self.keyword.currentText()))
        self.label_9 = QtWidgets.QLabel(Post)
        self.label_9.setGeometry(QtCore.QRect(170, 130, 251, 21))
        self.label_9.setObjectName("label_9")
        self.obtain_url = QtWidgets.QPushButton(Post)
        self.obtain_url.setGeometry(QtCore.QRect(230, 170, 91, 23))
        self.obtain_url.setObjectName("obtain_url")
        self.obtain_url.clicked.connect(lambda : self.Obtain_one(self.keyword.currentText(), self.pagenumber.text(), self.urled.text()))
        self.send_url = QtWidgets.QPushButton(Post)
        self.send_url.setGeometry(QtCore.QRect(90, 200, 91, 23))
        self.send_url.setObjectName("send_url")
        self.sengblog = QtWidgets.QTextEdit(Post)
        self.sengblog.setGeometry(QtCore.QRect(80, 250, 451, 192))
        self.sengblog.setObjectName("sengblog")
        self.sengblog.setReadOnly(True)
        self.send_url.clicked.connect(lambda :self.slotStart(self.keyword.currentText()))
        self.thread = Worker()
        self.thread.sinOut.connect(self.slotAdd)
        self.label_13 = QtWidgets.QLabel(Post)
        self.label_13.setGeometry(QtCore.QRect(30, 220, 51, 41))
        self.label_13.setObjectName("label_13")
        self.retranslateUi(Post)
        # self.username.editingFinished.connect(self.send_url.click)
        QtCore.QMetaObject.connectSlotsByName(Post)

    def Delete_record(self,arg):
        if arg == "经济圈":
            f = open("files/example.json", "w")
        # 打开通过爬虫爬取得帖子url
        elif arg == "男人圈":
            f = open("files/example_man.json", "w")
        elif arg == "摄影圈":
            f = open("files/example_pic.json", "w")
        elif arg == "内涵段子":
            f = open("files/example_duanzi.json", "w")
        elif arg == "社会百科":
            f = open("files/example_sec.json", "w")
        else:
            print("project_ui的delet_recod出错")
        f.truncate()
        f.close()

    def Obtain_one(self, k1, k2, k3):
        assi_value(k1, k2, k3)
        begin.Term_send(k1)

    def slotStart(self, rec):
        global record
        record = rec
        self.send_url.setEnabled(False)
        self.thread.start()

    def slotAdd(self, file_inf):
        self.sengblog.insertPlainText(file_inf)

    def retranslateUi(self, Post):
        _translate = QtCore.QCoreApplication.translate
        Post.setWindowTitle(_translate("Post", "中搜发帖"))
        Post.setWindowIcon(QIcon("files/ico.ico"))
        self.label.setText(_translate("Post", "第一步："))
        self.urled.setText('http://symobi.zhongsou.com/?interest_id=16595&rand=2056216641')
        self.label_2.setText(_translate("Post", "第二步："))
        self.label_3.setText(_translate("Post", "第三步："))
        self.label_4.setText(_translate("Post", "参考：在登陆之后，第二个界面点击圈子，跳转的时候短暂出现的网址，类似下面这种"))
        self.label_5.setText(_translate("Post", "http://symobi.zhongsou.com/?interest_id=16595&rand=2056216641"))
        self.label_6.setText(_translate("Post", "登录过的网址："))
        self.label_7.setText(_translate("Post", "圈子："))
        self.keyword.setItemText(0, _translate("Post", "经济圈"))
        self.keyword.setItemText(1, _translate("Post", "摄影圈"))
        self.keyword.setItemText(2, _translate("Post", "男人圈"))
        self.keyword.setItemText(3, _translate("Post", "社会百科"))
        self.keyword.setItemText(4, _translate("Post", "内涵段子"))
        self.label_8.setText(_translate("Post", "发帖页数："))
        self.delete_record.setText(_translate("Post", "删除记录"))
        self.label_9.setText(_translate("Post", "删除上次的记录之后再进行发送新帖"))
        self.obtain_url.setText(_translate("Post", "获取帖子链接"))
        self.send_url.setText(_translate("Post", "发送帖子"))
        self.label_13.setText(_translate("Post", "日志："))


class Worker(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.working = True
        self.num = 0

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        commu_econo.econo(self.sinOut, record)









