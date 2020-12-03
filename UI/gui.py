# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\gui_qt-designer-beta.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 423)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/logo.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"     border-top: 1px solid #C2C7CB;\n"
"     position: absolute;\n"
"     top: -0.5em;\n"
"     background: white;\n"
" }\n"
"\n"
" QTabWidget::tab-bar {\n"
"     alignment: center;\n"
" }\n"
"\n"
" /* Style the tab using the tab sub-control. Note that\n"
"     it reads QTabBar _not_ QTabWidget */\n"
" QTabBar::tab {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"     border: 1px solid #C4C4C3;\n"
"     border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"     min-width: 8ex;\n"
"     padding: 3px 15px;\n"
" }\n"
"\n"
" QTabBar::tab:selected, QTabBar::tab:hover {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                 stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"     border-color:#C4C4C3;\n"
"\n"
" }")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.DownloadTab = QtWidgets.QWidget()
        self.DownloadTab.setObjectName("DownloadTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.DownloadTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.DownloadTab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.videoUrlLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.videoUrlLineEdit.setFrame(True)
        self.videoUrlLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.videoUrlLineEdit.setCursorPosition(0)
        self.videoUrlLineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.videoUrlLineEdit.setObjectName("videoUrlLineEdit")
        self.gridLayout_2.addWidget(self.videoUrlLineEdit, 0, 2, 1, 1)
        self.BatchAdd = QtWidgets.QPushButton(self.groupBox)
        self.BatchAdd.setObjectName("BatchAdd")
        self.gridLayout_2.addWidget(self.BatchAdd, 0, 3, 1, 1)
        self.saveToLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.saveToLineEdit.setObjectName("saveToLineEdit")
        self.gridLayout_2.addWidget(self.saveToLineEdit, 1, 2, 1, 1)
        self.browse_btn = QtWidgets.QPushButton(self.groupBox)
        self.browse_btn.setObjectName("browse_btn")
        self.gridLayout_2.addWidget(self.browse_btn, 1, 3, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.DownloadTab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ConvertCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.ConvertCheckBox.setObjectName("ConvertCheckBox")
        self.horizontalLayout_4.addWidget(self.ConvertCheckBox)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.ConvertComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.ConvertComboBox.setMinimumSize(QtCore.QSize(120, 0))
        self.ConvertComboBox.setObjectName("ConvertComboBox")
        self.ConvertComboBox.addItem("")
        self.ConvertComboBox.addItem("")
        self.ConvertComboBox.addItem("")
        self.ConvertComboBox.addItem("")
        self.ConvertComboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.ConvertComboBox)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.DeleteFileCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.DeleteFileCheckBox.setChecked(True)
        self.DeleteFileCheckBox.setObjectName("DeleteFileCheckBox")
        self.verticalLayout_9.addWidget(self.DeleteFileCheckBox)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.download_btn = QtWidgets.QPushButton(self.DownloadTab)
        self.download_btn.setMinimumSize(QtCore.QSize(82, 28))
        self.download_btn.setStyleSheet("")
        self.download_btn.setDefault(True)
        self.download_btn.setFlat(False)
        self.download_btn.setObjectName("download_btn")
        self.verticalLayout_4.addWidget(self.download_btn)
        self.tabWidget.addTab(self.DownloadTab, "")
        self.ConvertTab = QtWidgets.QWidget()
        self.ConvertTab.setObjectName("ConvertTab")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.ConvertTab)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_11.addItem(spacerItem6)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.BrowseConvertToLineEdit = QtWidgets.QLineEdit(self.ConvertTab)
        self.BrowseConvertToLineEdit.setObjectName("BrowseConvertToLineEdit")
        self.horizontalLayout_6.addWidget(self.BrowseConvertToLineEdit)
        self.BrowseConvertToButton = QtWidgets.QPushButton(self.ConvertTab)
        self.BrowseConvertToButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.BrowseConvertToButton.setObjectName("BrowseConvertToButton")
        self.horizontalLayout_6.addWidget(self.BrowseConvertToButton)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 2, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.BrowseConvertLineEdit = QtWidgets.QLineEdit(self.ConvertTab)
        self.BrowseConvertLineEdit.setObjectName("BrowseConvertLineEdit")
        self.horizontalLayout_5.addWidget(self.BrowseConvertLineEdit)
        self.BrowseConvertButton = QtWidgets.QPushButton(self.ConvertTab)
        self.BrowseConvertButton.setObjectName("BrowseConvertButton")
        self.horizontalLayout_5.addWidget(self.BrowseConvertButton)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 2, 1, 1)
        self.ConvertMultipleToLabel = QtWidgets.QLabel(self.ConvertTab)
        self.ConvertMultipleToLabel.setObjectName("ConvertMultipleToLabel")
        self.gridLayout.addWidget(self.ConvertMultipleToLabel, 4, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 4, 1, 1, 1)
        self.ConvertMultipleFromLabel = QtWidgets.QLabel(self.ConvertTab)
        self.ConvertMultipleFromLabel.setObjectName("ConvertMultipleFromLabel")
        self.gridLayout.addWidget(self.ConvertMultipleFromLabel, 0, 0, 1, 1)
        self.DeleteConvertMultipleCheckBox = QtWidgets.QCheckBox(self.ConvertTab)
        self.DeleteConvertMultipleCheckBox.setChecked(True)
        self.DeleteConvertMultipleCheckBox.setTristate(False)
        self.DeleteConvertMultipleCheckBox.setObjectName("DeleteConvertMultipleCheckBox")
        self.gridLayout.addWidget(self.DeleteConvertMultipleCheckBox, 1, 2, 1, 1)
        self.ConvertMultipleComboBox = QtWidgets.QComboBox(self.ConvertTab)
        self.ConvertMultipleComboBox.setMinimumSize(QtCore.QSize(120, 0))
        self.ConvertMultipleComboBox.setObjectName("ConvertMultipleComboBox")
        self.ConvertMultipleComboBox.addItem("")
        self.ConvertMultipleComboBox.addItem("")
        self.ConvertMultipleComboBox.addItem("")
        self.ConvertMultipleComboBox.addItem("")
        self.ConvertMultipleComboBox.addItem("")
        self.gridLayout.addWidget(self.ConvertMultipleComboBox, 4, 2, 1, 1)
        self.ConvertMultipleDestinationLabel = QtWidgets.QLabel(self.ConvertTab)
        self.ConvertMultipleDestinationLabel.setObjectName("ConvertMultipleDestinationLabel")
        self.gridLayout.addWidget(self.ConvertMultipleDestinationLabel, 5, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem8, 2, 2, 1, 1)
        self.verticalLayout_11.addLayout(self.gridLayout)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem9)
        self.ConvertMultipleButton = QtWidgets.QPushButton(self.ConvertTab)
        self.ConvertMultipleButton.setMinimumSize(QtCore.QSize(0, 28))
        self.ConvertMultipleButton.setAutoDefault(False)
        self.ConvertMultipleButton.setObjectName("ConvertMultipleButton")
        self.verticalLayout_11.addWidget(self.ConvertMultipleButton)
        self.tabWidget.addTab(self.ConvertTab, "")
        self.ActivityTab = QtWidgets.QWidget()
        self.ActivityTab.setObjectName("ActivityTab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.ActivityTab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableWidget = QtWidgets.QTableWidget(self.ActivityTab)
        self.tableWidget.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableWidget.setStatusTip("")
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.VLine)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.ActivityTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.actionOptions = QtWidgets.QAction(MainWindow)
        self.actionOptions.setObjectName("actionOptions")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionLicense)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.videoUrlLineEdit.returnPressed.connect(self.download_btn.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "youtube-dl v0.4.1"))
        self.groupBox.setTitle(_translate("MainWindow", "Enter url and download location"))
        self.label_2.setText(_translate("MainWindow", "Video URL:"))
        self.label_3.setText(_translate("MainWindow", "Save To:"))
        self.videoUrlLineEdit.setPlaceholderText(_translate("MainWindow", "http://www.dailymotion.com/video/x2asrvp_salman-khan-teasing-katrina-kaif-at-his-sister-arpita-s-wedding_shortfilms"))
        self.BatchAdd.setText(_translate("MainWindow", "Batch Add"))
        self.browse_btn.setText(_translate("MainWindow", "Browse"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Convert"))
        self.ConvertCheckBox.setText(_translate("MainWindow", "Convert After Download"))
        self.ConvertComboBox.setItemText(0, _translate("MainWindow", "mp4"))
        self.ConvertComboBox.setItemText(1, _translate("MainWindow", "flv"))
        self.ConvertComboBox.setItemText(2, _translate("MainWindow", "ogg"))
        self.ConvertComboBox.setItemText(3, _translate("MainWindow", "webm"))
        self.ConvertComboBox.setItemText(4, _translate("MainWindow", "mkv"))
        self.DeleteFileCheckBox.setText(_translate("MainWindow", "Delete Original File"))
        self.download_btn.setText(_translate("MainWindow", "Download"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DownloadTab), _translate("MainWindow", "Download"))
        self.BrowseConvertToButton.setText(_translate("MainWindow", "Browse"))
        self.BrowseConvertButton.setText(_translate("MainWindow", "Browse"))
        self.ConvertMultipleToLabel.setText(_translate("MainWindow", "Convert file to"))
        self.ConvertMultipleFromLabel.setText(_translate("MainWindow", "Select a file or files"))
        self.DeleteConvertMultipleCheckBox.setText(_translate("MainWindow", "Delete the original file after conversion"))
        self.ConvertMultipleComboBox.setItemText(0, _translate("MainWindow", "mp4"))
        self.ConvertMultipleComboBox.setItemText(1, _translate("MainWindow", "flv"))
        self.ConvertMultipleComboBox.setItemText(2, _translate("MainWindow", "ogg"))
        self.ConvertMultipleComboBox.setItemText(3, _translate("MainWindow", "webm"))
        self.ConvertMultipleComboBox.setItemText(4, _translate("MainWindow", "mkv"))
        self.ConvertMultipleDestinationLabel.setText(_translate("MainWindow", "Save to"))
        self.ConvertMultipleButton.setText(_translate("MainWindow", "Convert"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ConvertTab), _translate("MainWindow", "Convert"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Video/Song"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Size"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ETA"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Speed"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ActivityTab), _translate("MainWindow", "Activity"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionHelp.setText(_translate("MainWindow", "About"))
        self.actionLicense.setText(_translate("MainWindow", "License"))
        self.actionOptions.setText(_translate("MainWindow", "Options"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

from UI import resource_rc
