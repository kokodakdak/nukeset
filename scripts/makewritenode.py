#coding:utf8
import nuke
import nukescripts
from PySide2.QtWidgets import *


class MakeWrite(QWidget):
	formats = ["2048x1152","1920x1080","2048x872"]
	exts = [".exr",".dpx",".jpg",".mov"]

	def __init__(self):
		super(MakeWrite, self).__init__()
		self.ok = QPushButton("OK")
		self.cancel = QPushButton("Cancel")
		self.ext = QComboBox()
		self.ext.addItems(self.exts)
		self.fm = QComboBox()
		self.fm.addItems(self.formats)
		self.reformat = QCheckBox("&reformat",self)
		self.reformat.setChecked(True)
		self.slate = QCheckBox("&slate",self)
		self.slate.setChecked(True)
		self.addtimecode = QCheckBox("&AddTimecode",self)
		self.addtimecode.setChecked(False)
		self.startframe = QLineEdit(str(int(nuke.Root()["first_frame"].value())))
		self.starttimecode = QLineEdit("00:00:00:00")

		#event
		self.ok.clicked.connect(self.bt_ok)
		self.fm.currentIndexChanged.connect(self.indexChanged)
		self.cancel.clicked.connect(self.close)

		#set layout
		layout = QGridLayout()
		layout.addWidget(self.reformat, 0, 0)
		layout.addWidget(self.fm, 0,1)
		layout.addWidget(self.addtimecode,1, 0)
		layout.addWidget(self.startframe, 1, 1)
		layout.addWidget(self.starttimecode, 1, 2)
		layout.addWidget(self.slate, 2, 0)
		layout.addWidget(QLabel("Ext"), 3, 0)
		layout.addWidget(self.ext, 3, 1)
		layout.addWidget(self.cancel, 4, 0)
		layout.addWidget(self.ok, 4, 1)

		self.linkOrder = []	
		
		self.setLayout(layout)


	def indexChanged(self):
		self.reformatSize = self.fm.currentText()



	def genReformat(self):
		reformat = nuke.nodes.Reformat()
		reformat["type"].setValue("to box")
		reformat["box_fixed"].setValue(True)
		width, height = self.fm.currentText().split("x")
		reformat["box_width"].setValue(int(width))
		reformat["box_height"].setValue(int(height))
		self.linkOrder.append(reformat)

	def genAddTimeCode(self):
		timecode = nuke.nodes.AddTimeCode()
		timecode["startcode"].setValue(str(self.starttimecode.text())
		timecode["useFrame"].setValue(True)
		timecode["frame"].setValue(int(self.startframe.text())
		self.linkOrder.append(timecode)

	def genSlate(self):	
		slate = nuke.nodes.slate()
		self.linkOrder.append(slate)


	def genWrite(self):		
		write = nuke.nodes.Write()
		dirname, basename = os.path.split(nuke.root().name())
		filename, notuse = os.path.splittext(basename)
		ext = str(self.ext.currentText())
		write["file_type"].setValue("to box")
		write["file"].setValue("/test/test.####%s" % (self.ext.currentText()))
		write["create_directories"].setValue(True)
		self.linkOrder.append(write)





# 이걸 어케 수정할까
	def bt_ok(self):
		if self.reformat.isChecked():
			self.genReformat()
		if self.addtimecode.isChecked():					
			self.genAddTimeCode()
		if self.slate.isChecked():
			self.genSlate()
		self.genWrite()


		tail = nuke.selectedNode()
		for n in self.linkOrder:
			n.setInput(0,tail)
			tail = n
		self.close()


def main():
	if len(nuke.selectedNodes()) == 0:
		nuke.message("노드를 선택하세요.")
		return
	global customApp
	try:
		customApp.close()
	except:
		pass
	customApp = MakeWrite()
	try:
		customApp.show()
	except:
		pass

