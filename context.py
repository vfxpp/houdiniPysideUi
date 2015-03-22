#!/usr/bin/env python
#-*- coding:utf-8 -*-
from PySide import QtGui,QtCore
import sys
import os

class main(QtGui.QWidget):
	def __init__(self,parent=None):
		super(main,self).__init__(parent)
		self.test = qd()
		self.testb = qdb()
		self.setWindowTitle('easy tools')
		self.setWindowIcon(QtGui.QIcon('zhangjl.jpg'))

		self.project = QtGui.QLabel('Project')
		self.project.setToolTip('enter project name')
		
		self.scence = QtGui.QLabel('Scence')
		self.scence.setToolTip('enter scence name')

		self.shot = QtGui.QLabel('Shot')
		self.shot.setToolTip('enter shot name')

		self.e1 = QtGui.QLineEdit()
		self.e1.setToolTip('enter project name')
		self.e2 = QtGui.QLineEdit()
		self.e2.setToolTip('enter scence name')
		self.e3 = QtGui.QLineEdit()
		self.e3.setToolTip('enter shot name')
		self.project.setBuddy(self.e1)
		self.scence.setBuddy(self.e2)
		self.shot.setBuddy(self.e3)
		
		prolayA = QtGui.QHBoxLayout()
		prolayA.addWidget(self.project)
		prolayA.addWidget(self.e1)


		prolayB = QtGui.QHBoxLayout()
		prolayB.addWidget(self.scence)
		prolayB.addWidget(self.e2)

		prolayC = QtGui.QHBoxLayout()
		prolayC.addWidget(self.shot)
		prolayC.addWidget(self.e3)

		pro = QtGui.QVBoxLayout()
		pro.addLayout(prolayA)
		pro.addLayout(prolayB)
		pro.addLayout(prolayC)
		pro.addStretch()



		self.la = QtGui.QLabel('Layout File List')
		self.lb = QtGui.QLabel('Animaition File List')
		lalay = QtGui.QVBoxLayout()
		lalay.addWidget(self.la)
		lalay.addWidget(self.test)

		lblay = QtGui.QVBoxLayout()
		lblay.addWidget(self.lb)
		lblay.addWidget(self.testb)

		mainLayout = QtGui.QHBoxLayout()
		mainLayout.addLayout(pro)
		mainLayout.addLayout(lalay)
		mainLayout.addLayout(lblay)

		self.setLayout(mainLayout)




class qd(QtGui.QMainWindow):
	def __init__(self):
		super(qd,self).__init__()
		
		self.list = QtGui.QListWidget()


		#for i in range(len(os.popen('ls').readlines())):
		#	lst = QtGui.QListWidgetItem(os.popen('ls').readlines()[i][:-1])


		lst = os.popen('ls').readlines()
		self.list.addItems(lst)


		


		#lst=QtGui.QListWidgetItem('ok')
		#lstb = QtGui.QListWidgetItem('No')
		#self.list.insertItem(1,lst)
		#self.list.insertItem(2,lstb)



		self.setCentralWidget(self.list)
		self.list.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
		self.list.itemClicked.connect(self.myListWidgetContext)

		self.exit = QtGui.QAction(QtGui.QIcon('zhangjl.jpg'), 'import', self)
		self.ref = QtGui.QAction(QtGui.QIcon('zhangjl.jpg'), 'refresh', self)
		self.exit.triggered.connect(self.pp)
	def myListWidgetContext(self):
		self.popMenu = QtGui.QMenu()
		self.popMenu.addAction(self.exit)
		#获得当前鼠标位置
		self.popMenu.exec_(QtGui.QCursor.pos())

	def pp(self):

		for sel in self.list.selectedItems():
			sel.setText('>imported!!<   '+sel.text())
			print sel.text()
		#print(self.list.selectedItems()[0].text())





class qdb(QtGui.QMainWindow):
	def __init__(self):
		super(qdb,self).__init__()
		self.list = QtGui.QListWidget()

		lst = os.popen('ls').readlines()
		self.list.addItems(lst)
		#lst=QtGui.QListWidgetItem('ok')
		#lstb = QtGui.QListWidgetItem('No')
		#self.list.insertItem(1,lst)
		#self.list.insertItem(2,lstb)
		self.setCentralWidget(self.list)
		self.list.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
		self.list.itemClicked.connect(self.myListWidgetContext)

		self.exit = QtGui.QAction(QtGui.QIcon('zhangjl.jpg'), 'import', self)
		self.exit.triggered.connect(self.pp)
	def myListWidgetContext(self):
		self.popMenu = QtGui.QMenu()
		self.popMenu.addAction(self.exit)
		#获得当前鼠标位置
		self.popMenu.exec_(QtGui.QCursor.pos())

	def pp(self):
		print(self.list.selectedItems()[0].text())




app = QtGui.QApplication(sys.argv)
ex = main()
ex.show()

app.exec_()