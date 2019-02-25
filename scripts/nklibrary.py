#coding:utf8

import nuke
import os
from PySide2.QtWidgets import *


class NkLibrary(QWidget):
	def __init__(self):
		super(NkLibrary,self).__init__()
		self.libpath = os.getenv("NUKE_PATH") + "/nk/"
		self.appname = "Nuke Library"
		self.appversion = "v0.1"
		#widget
		self.nklist = QListWidget()
		self.addNkList()
		nkpath = os.getenv("NUKE_PATH")+"/nk/"
		self.ok = QPushButton("OK")
		self.cancel = QPushButton("Cancel")

		#layout
		self.setWindowTitle(self.appname + self.appversion)
		layout = QVBoxLayout()
		layout.addWidget(self.nklist)
		layout.addWidget(self.ok)
		layout.addWidget(self.cancel)
		self.setLayout(layout)

		#event
		self.ok.clicked.connect(self.pushOK)
		self.cancel.clicked.connect(self.close)
		self.nklist.itemClicked.connect(self.itemClick)

	def pushOK(self):
		nuke.nodePaste(self.libpath + self.currentItem)
		self.close()


	def itemClick(self, item):
		self.currentItem = item.text()
		

	def addNkList(self):
		if not os.path.exists(self.libpath):
			nuke.message(self.libpath + "경로가 존재하지않습니다.")
		for i in os.listdir(self.libpath):
			base, ext = os.path.splitext(i)
			if ext != ".nk":
				continue
			self.nklist.addItem(QListWidgetItem(i))




def main():
	global customApp
	try:
		customApp.close()
	except:
		pass

	customApp = NkLibrary()
	try:
		customApp.show()
	except:
		pass
