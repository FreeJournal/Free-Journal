# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FreeJournal_UI.ui'
#
# Created: Sun Mar 15 19:43:13 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_FJ_Main_Window(object):

    def setupUi(self, FJ_Main_Window):
        FJ_Main_Window.setObjectName(_fromUtf8("FJ_Main_Window"))
        FJ_Main_Window.resize(758, 587)
        FJ_Main_Window.setMinimumSize(QtCore.QSize(300, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(_fromUtf8(":/Images/FreeJournal_icon.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FJ_Main_Window.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(FJ_Main_Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout_Lower_Right = QtGui.QGridLayout()
        self.gridLayout_Lower_Right.setObjectName(
            _fromUtf8("gridLayout_Lower_Right"))
        self.pushButtonDelete = QtGui.QPushButton(self.centralwidget)
        self.pushButtonDelete.setObjectName(_fromUtf8("pushButtonDelete"))
        self.gridLayout_Lower_Right.addWidget(
            self.pushButtonDelete, 1, 0, 1, 1)
        self.pushButtonDonate = QtGui.QPushButton(self.centralwidget)
        self.pushButtonDonate.setObjectName(_fromUtf8("pushButtonDonate"))
        self.gridLayout_Lower_Right.addWidget(
            self.pushButtonDonate, 2, 0, 1, 1)
        self.pushButtonNew = QtGui.QPushButton(self.centralwidget)
        self.pushButtonNew.setObjectName(_fromUtf8("pushButtonNew"))
        self.gridLayout_Lower_Right.addWidget(self.pushButtonNew, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_Lower_Right, 2, 1, 1, 1)
        self.gridLayout_Upper_Right = QtGui.QGridLayout()
        self.gridLayout_Upper_Right.setObjectName(
            _fromUtf8("gridLayout_Upper_Right"))
        self.pushButtonAdd_Comment = QtGui.QPushButton(self.centralwidget)
        self.pushButtonAdd_Comment.setObjectName(
            _fromUtf8("pushButtonAdd_Comment"))
        self.gridLayout_Upper_Right.addWidget(
            self.pushButtonAdd_Comment, 1, 0, 1, 1)
        self.pushButtonReset = QtGui.QPushButton(self.centralwidget)
        self.pushButtonReset.setObjectName(_fromUtf8("pushButtonReset"))
        self.gridLayout_Upper_Right.addWidget(self.pushButtonReset, 0, 0, 1, 1)
        self.pushButtonVote = QtGui.QPushButton(self.centralwidget)
        self.pushButtonVote.setObjectName(_fromUtf8("pushButtonVote"))
        self.gridLayout_Upper_Right.addWidget(self.pushButtonVote, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_Upper_Right, 1, 1, 1, 1)
        self.gridLayout_Lower = QtGui.QGridLayout()
        self.gridLayout_Lower.setObjectName(_fromUtf8("gridLayout_Lower"))
        self.gridLayout_Button_Rebroadcast = QtGui.QGridLayout()
        self.gridLayout_Button_Rebroadcast.setObjectName(
            _fromUtf8("gridLayout_Button_Rebroadcast"))
        self.pushButtonRebroadcast = QtGui.QPushButton(self.centralwidget)
        self.pushButtonRebroadcast.setObjectName(
            _fromUtf8("pushButtonRebroadcast"))
        self.gridLayout_Button_Rebroadcast.addWidget(
            self.pushButtonRebroadcast, 0, 0, 1, 1)
        self.gridLayout_Lower.addLayout(
            self.gridLayout_Button_Rebroadcast, 1, 0, 1, 1)
        self.gridLayout_Lower_Left = QtGui.QGridLayout()
        self.gridLayout_Lower_Left.setObjectName(
            _fromUtf8("gridLayout_Lower_Left"))
        self.tabWidgetLocal = QtGui.QTabWidget(self.centralwidget)
        self.tabWidgetLocal.setObjectName(_fromUtf8("tabWidgetLocal"))
        self.tabLocal = QtGui.QWidget()
        self.tabLocal.setObjectName(_fromUtf8("tabLocal"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tabLocal)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.treeViewLocal = QtGui.QTreeView(self.tabLocal)
        self.treeViewLocal.setObjectName(_fromUtf8("treeViewLocal"))
        self.verticalLayout_5.addWidget(self.treeViewLocal)
        self.tabWidgetLocal.addTab(self.tabLocal, _fromUtf8(""))
        self.tabPending = QtGui.QWidget()
        self.tabPending.setObjectName(_fromUtf8("tabPending"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabPending)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.treeViewPending = QtGui.QTreeView(self.tabPending)
        self.treeViewPending.setObjectName(_fromUtf8("treeViewPending"))
        self.verticalLayout_2.addWidget(self.treeViewPending)
        self.tabWidgetLocal.addTab(self.tabPending, _fromUtf8(""))
        self.tabHosting = QtGui.QWidget()
        self.tabHosting.setObjectName(_fromUtf8("tabHosting"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabHosting)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.treeViewHosting = QtGui.QTreeView(self.tabHosting)
        self.treeViewHosting.setObjectName(_fromUtf8("treeViewHosting"))
        self.verticalLayout_4.addWidget(self.treeViewHosting)
        self.tabWidgetLocal.addTab(self.tabHosting, _fromUtf8(""))
        self.gridLayout_Lower_Left.addWidget(self.tabWidgetLocal, 0, 0, 1, 1)
        self.gridLayout_Lower.addLayout(self.gridLayout_Lower_Left, 0, 0, 1, 1)
        self.pushButtonJoin_Discu = QtGui.QPushButton(self.centralwidget)
        self.pushButtonJoin_Discu.setObjectName(
            _fromUtf8("pushButtonJoin_Discu"))
        self.gridLayout_Lower.addWidget(self.pushButtonJoin_Discu, 1, 1, 1, 1)
        self.pushButtonPublish = QtGui.QPushButton(self.centralwidget)
        self.pushButtonPublish.setObjectName(_fromUtf8("pushButtonPublish"))
        self.gridLayout_Lower.addWidget(self.pushButtonPublish, 2, 0, 1, 1)
        self.tabWidgetSubs = QtGui.QTabWidget(self.centralwidget)
        self.tabWidgetSubs.setObjectName(_fromUtf8("tabWidgetSubs"))
        self.tabSubscriptions = QtGui.QWidget()
        self.tabSubscriptions.setObjectName(_fromUtf8("tabSubscriptions"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabSubscriptions)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.treeViewSubscriptions = QtGui.QTreeView(self.tabSubscriptions)
        self.treeViewSubscriptions.setObjectName(
            _fromUtf8("treeViewSubscriptions"))
        self.verticalLayout_3.addWidget(self.treeViewSubscriptions)
        self.tabWidgetSubs.addTab(self.tabSubscriptions, _fromUtf8(""))
        self.tabUpdates = QtGui.QWidget()
        self.tabUpdates.setObjectName(_fromUtf8("tabUpdates"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tabUpdates)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.treeViewUpdates = QtGui.QTreeView(self.tabUpdates)
        self.treeViewUpdates.setObjectName(_fromUtf8("treeViewUpdates"))
        self.verticalLayout_6.addWidget(self.treeViewUpdates)
        self.tabWidgetSubs.addTab(self.tabUpdates, _fromUtf8(""))
        self.gridLayout_Lower.addWidget(self.tabWidgetSubs, 0, 1, 1, 1)
        self.pushButtonDownload = QtGui.QPushButton(self.centralwidget)
        self.pushButtonDownload.setObjectName(_fromUtf8("pushButtonDownload"))
        self.gridLayout_Lower.addWidget(self.pushButtonDownload, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_Lower, 2, 0, 1, 1)
        self.lineEditSearchDatabase = QtGui.QLineEdit(self.centralwidget)
        self.lineEditSearchDatabase.setText(_fromUtf8(""))
        self.lineEditSearchDatabase.setObjectName(
            _fromUtf8("lineEditSearchDatabase"))
        self.gridLayout_2.addWidget(self.lineEditSearchDatabase, 0, 0, 1, 1)
        self.pushButtonSearch = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSearch.setObjectName(_fromUtf8("pushButtonSearch"))
        self.gridLayout_2.addWidget(self.pushButtonSearch, 0, 1, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 1)
        FJ_Main_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FJ_Main_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 758, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        FJ_Main_Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(FJ_Main_Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        FJ_Main_Window.setStatusBar(self.statusbar)
        self.actionView_Documentation = QtGui.QAction(FJ_Main_Window)
        self.actionView_Documentation.setObjectName(
            _fromUtf8("actionView_Documentation"))
        self.actionAbout_Free_Journal = QtGui.QAction(FJ_Main_Window)
        self.actionAbout_Free_Journal.setObjectName(
            _fromUtf8("actionAbout_Free_Journal"))
        self.actionNew_Collection = QtGui.QAction(FJ_Main_Window)
        self.actionNew_Collection.setObjectName(
            _fromUtf8("actionNew_Collection"))
        self.actionQuit_FJ = QtGui.QAction(FJ_Main_Window)
        self.actionQuit_FJ.setCheckable(False)
        self.actionQuit_FJ.setObjectName(_fromUtf8("actionQuit_FJ"))
        self.actionFree_Journal_Website = QtGui.QAction(FJ_Main_Window)
        self.actionFree_Journal_Website.setObjectName(
            _fromUtf8("actionFree_Journal_Website"))
        self.actionGitHub_Source = QtGui.QAction(FJ_Main_Window)
        self.actionGitHub_Source.setObjectName(
            _fromUtf8("actionGitHub_Source"))
        self.actionPrefernces = QtGui.QAction(FJ_Main_Window)
        self.actionPrefernces.setObjectName(_fromUtf8("actionPrefernces"))
        self.menuFile.addAction(self.actionNew_Collection)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit_FJ)
        self.menuHelp.addAction(self.actionFree_Journal_Website)
        self.menuHelp.addAction(self.actionGitHub_Source)
        self.menuHelp.addAction(self.actionView_Documentation)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Free_Journal)
        self.menuEdit.addAction(self.actionPrefernces)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(FJ_Main_Window)
        self.tabWidgetLocal.setCurrentIndex(0)
        self.tabWidgetSubs.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuit_FJ, QtCore.SIGNAL(
            _fromUtf8("triggered()")), FJ_Main_Window.close)
        QtCore.QMetaObject.connectSlotsByName(FJ_Main_Window)

    def retranslateUi(self, FJ_Main_Window):
        FJ_Main_Window.setWindowTitle(
            _translate("FJ_Main_Window", "Free Journal", None))
        self.pushButtonDelete.setStatusTip(
            _translate("FJ_Main_Window", "Delete", None))
        self.pushButtonDelete.setText(
            _translate("FJ_Main_Window", "Delete", None))
        self.pushButtonDonate.setStatusTip(
            _translate("FJ_Main_Window", "Support the Free Journal dream!", None))
        self.pushButtonDonate.setText(
            _translate("FJ_Main_Window", "Donate", None))
        self.pushButtonNew.setStatusTip(
            _translate("FJ_Main_Window", "Create a new Collection of Documents.", None))
        self.pushButtonNew.setText(_translate("FJ_Main_Window", "New", None))
        self.pushButtonAdd_Comment.setStatusTip(
            _translate("FJ_Main_Window", "Share your opinion.", None))
        self.pushButtonAdd_Comment.setText(
            _translate("FJ_Main_Window", "Add Comment", None))
        self.pushButtonReset.setStatusTip(
            _translate("FJ_Main_Window", "Reset search filter.", None))
        self.pushButtonReset.setText(
            _translate("FJ_Main_Window", "Reset", None))
        self.pushButtonVote.setStatusTip(
            _translate("FJ_Main_Window", "Rate a collection.", None))
        self.pushButtonVote.setText(_translate("FJ_Main_Window", "Vote", None))
        self.pushButtonRebroadcast.setStatusTip(
            _translate("FJ_Main_Window", "Rebroadcast a collection on your local machine.", None))
        self.pushButtonRebroadcast.setText(
            _translate("FJ_Main_Window", "Rebroadcast", None))
        self.tabWidgetLocal.setStatusTip(
            _translate("FJ_Main_Window", "Collections on local machine, dowloading, and hosting.", None))
        self.tabWidgetLocal.setTabText(self.tabWidgetLocal.indexOf(
            self.tabLocal), _translate("FJ_Main_Window", "Local", None))
        self.tabWidgetLocal.setTabText(self.tabWidgetLocal.indexOf(
            self.tabPending), _translate("FJ_Main_Window", "Pending...", None))
        self.tabWidgetLocal.setTabText(self.tabWidgetLocal.indexOf(
            self.tabHosting), _translate("FJ_Main_Window", "Hosting", None))
        self.pushButtonJoin_Discu.setStatusTip(
            _translate("FJ_Main_Window", "Talk about this collection.", None))
        self.pushButtonJoin_Discu.setText(
            _translate("FJ_Main_Window", "Join Discussion", None))
        self.pushButtonPublish.setStatusTip(
            _translate("FJ_Main_Window", "Publish a collection of documents.", None))
        self.pushButtonPublish.setText(
            _translate("FJ_Main_Window", "Publish", None))
        self.tabWidgetSubs.setStatusTip(
            _translate("FJ_Main_Window", "Subscriptions and Updates available.", None))
        self.tabWidgetSubs.setTabText(self.tabWidgetSubs.indexOf(
            self.tabSubscriptions), _translate("FJ_Main_Window", "Subscriptions", None))
        self.tabWidgetSubs.setTabText(self.tabWidgetSubs.indexOf(
            self.tabUpdates), _translate("FJ_Main_Window", "Updates", None))
        self.pushButtonDownload.setStatusTip(
            _translate("FJ_Main_Window", "Download the latest subsciption update.", None))
        self.pushButtonDownload.setText(
            _translate("FJ_Main_Window", "Download", None))
        self.lineEditSearchDatabase.setPlaceholderText(
            _translate("FJ_Main_Window", "Search...", None))
        self.pushButtonSearch.setStatusTip(
            _translate("FJ_Main_Window", "Search by entering keywords.", None))
        self.pushButtonSearch.setText(
            _translate("FJ_Main_Window", "Search", None))
        self.tableWidget.setStatusTip(
            _translate("FJ_Main_Window", "Available collections.", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FJ_Main_Window", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FJ_Main_Window", "Rating", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("FJ_Main_Window", "Date Added", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("FJ_Main_Window", "Health", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("FJ_Main_Window", "Label", None))
        self.menuFile.setTitle(_translate("FJ_Main_Window", "File", None))
        self.menuHelp.setTitle(_translate("FJ_Main_Window", "Help", None))
        self.menuEdit.setTitle(_translate("FJ_Main_Window", "Edit", None))
        self.actionView_Documentation.setText(
            _translate("FJ_Main_Window", "View Documentation", None))
        self.actionView_Documentation.setShortcut(
            _translate("FJ_Main_Window", "F1", None))
        self.actionAbout_Free_Journal.setText(
            _translate("FJ_Main_Window", "About Free Journal", None))
        self.actionNew_Collection.setText(
            _translate("FJ_Main_Window", "New Collection...", None))
        self.actionQuit_FJ.setText(_translate("FJ_Main_Window", "Quit", None))
        self.actionFree_Journal_Website.setText(
            _translate("FJ_Main_Window", "Free Journal Website", None))
        self.actionGitHub_Source.setText(
            _translate("FJ_Main_Window", "View Source Code", None))
        self.actionPrefernces.setText(
            _translate("FJ_Main_Window", "Preferences...", None))

from .frontend.uploader import resources_rc
