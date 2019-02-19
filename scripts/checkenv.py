#coding:utf8
import os
import nuke
#from PySide2.QtWidgets import *

def main():

	results = []
	envs = ["USER","OCIO","NUKE_PATH","NUKE_FONT_PATH"]

	for e in envs:
		results.append("$%s : %s" % (e, os.environ[e]))
	nuke.message("\n".join(results))

