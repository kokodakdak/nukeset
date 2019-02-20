#coding:utf8
import os
#import nuke
from PySide2.QtWidgets import *



"""
뉴크 의존성도 제거할수 있다. 
"""
class CheckEnv(QWidget):
	def __init__(self):
		super(CheckEnv, self).__init__()
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)
		self.setEnv()

	def setEnv(self):
		envs = ["USER", "OCIO", "NUKE_PATH","NUKE_FONT_PATH"]
		for e in envs:
			self.layout.addWidget(QLabel("$%s : %s" % (e,os.environ[e])))

def main():
	global customApp
	try:
		customApp.close()
	except:
		pass
	customApp = CheckEnv()
	try:
		customApp.show()
	except:
		pass








"""
큐티위젯으로 짜기 전
def main():

	results = []
	envs = ["USER","OCIO","NUKE_PATH","NUKE_FONT_PATH"]

	for e in envs:
		results.append("$%s : %s" % (e, os.environ[e]))
	nuke.message("\n".join(results))
"""
