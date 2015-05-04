# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FreeJournalUploaderGUI.ui'
#
# Created: Tue Apr 14 07:19:11 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os

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


class Ui_FJ_Uploader_Main_Window(object):

    def setupUi(self, FJ_Uploader_Main_Window):
        FJ_Uploader_Main_Window.setObjectName(
            _fromUtf8("FJ_Uploader_Main_Window"))
        FJ_Uploader_Main_Window.resize(673, 567)
        FJ_Uploader_Main_Window.setMinimumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon(
            os.getcwd() + '/frontend/uploader/FJ_Desktop_UI/FreeJournal_icon.jpg')
        # icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/FreeJournal_icon.jpg")),
        # QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FJ_Uploader_Main_Window.setWindowIcon(icon)
        FJ_Uploader_Main_Window.setAutoFillBackground(False)
        FJ_Uploader_Main_Window.setDocumentMode(False)
        FJ_Uploader_Main_Window.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(FJ_Uploader_Main_Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_8 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.horizontalLayoutPerform = QtGui.QHBoxLayout()
        self.horizontalLayoutPerform.setObjectName(
            _fromUtf8("horizontalLayoutPerform"))
        self.pushButtonNew = QtGui.QPushButton(self.centralwidget)
        self.pushButtonNew.setDefault(False)
        self.pushButtonNew.setObjectName(_fromUtf8("pushButtonNew"))
        self.horizontalLayoutPerform.addWidget(self.pushButtonNew)
        self.pushButtonDelete = QtGui.QPushButton(self.centralwidget)
        self.pushButtonDelete.setEnabled(False)
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButtonDelete.setFont(font)
        self.pushButtonDelete.setAccessibleDescription(_fromUtf8(""))
        self.pushButtonDelete.setAutoFillBackground(False)
        self.pushButtonDelete.setCheckable(False)
        self.pushButtonDelete.setAutoDefault(False)
        self.pushButtonDelete.setDefault(False)
        self.pushButtonDelete.setFlat(False)
        self.pushButtonDelete.setObjectName(_fromUtf8("pushButtonDelete"))
        self.horizontalLayoutPerform.addWidget(self.pushButtonDelete)
        self.pushButtonPublish = QtGui.QPushButton(self.centralwidget)
        self.pushButtonPublish.setEnabled(False)
        self.pushButtonPublish.setObjectName(_fromUtf8("pushButtonPublish"))
        self.horizontalLayoutPerform.addWidget(self.pushButtonPublish)
        self.gridLayout_8.addLayout(self.horizontalLayoutPerform, 1, 2, 1, 1)
        self.gridLayoutModify = QtGui.QGridLayout()
        self.gridLayoutModify.setObjectName(_fromUtf8("gridLayoutModify"))
        self.pushButtonRemove = QtGui.QPushButton(self.centralwidget)
        self.pushButtonRemove.setEnabled(False)
        self.pushButtonRemove.setObjectName(_fromUtf8("pushButtonRemove"))
        self.gridLayoutModify.addWidget(self.pushButtonRemove, 1, 0, 1, 1)
        self.pushButtonAdd = QtGui.QPushButton(self.centralwidget)
        self.pushButtonAdd.setEnabled(False)
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))
        self.gridLayoutModify.addWidget(self.pushButtonAdd, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayoutModify, 0, 1, 1, 1)
        self.gridLayoutCollections = QtGui.QGridLayout()
        self.gridLayoutCollections.setObjectName(
            _fromUtf8("gridLayoutCollections"))
        self.treeWidgetCollections = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidgetCollections.setObjectName(
            _fromUtf8("treeWidgetCollections"))
        self.gridLayoutCollections.addWidget(
            self.treeWidgetCollections, 1, 0, 1, 1)
        self.labelCollections = QtGui.QLabel(self.centralwidget)
        self.labelCollections.setObjectName(_fromUtf8("labelCollections"))
        self.gridLayoutCollections.addWidget(self.labelCollections, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayoutCollections, 0, 2, 1, 1)
        self.gridLayoutLocal = QtGui.QGridLayout()
        self.gridLayoutLocal.setObjectName(_fromUtf8("gridLayoutLocal"))
        self.treeViewLocal = QtGui.QTreeView(self.centralwidget)
        self.treeViewLocal.setObjectName(_fromUtf8("treeViewLocal"))
        self.gridLayoutLocal.addWidget(self.treeViewLocal, 1, 0, 1, 1)
        self.labelLocal = QtGui.QLabel(self.centralwidget)
        self.labelLocal.setObjectName(_fromUtf8("labelLocal"))
        self.gridLayoutLocal.addWidget(self.labelLocal, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayoutLocal, 0, 0, 1, 1)
        self.horizontalLayoutOut = QtGui.QHBoxLayout()
        self.horizontalLayoutOut.setObjectName(
            _fromUtf8("horizontalLayoutOut"))
        self.labelOut = QtGui.QLabel(self.centralwidget)
        self.labelOut.setObjectName(_fromUtf8("labelOut"))
        self.horizontalLayoutOut.addWidget(self.labelOut)
        self.lineEditOut = QtGui.QLineEdit(self.centralwidget)
        self.lineEditOut.setReadOnly(True)
        self.lineEditOut.setObjectName(_fromUtf8("lineEditOut"))
        self.horizontalLayoutOut.addWidget(self.lineEditOut)
        self.gridLayout_8.addLayout(self.horizontalLayoutOut, 1, 0, 1, 1)
        FJ_Uploader_Main_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FJ_Uploader_Main_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 673, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        FJ_Uploader_Main_Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(FJ_Uploader_Main_Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        FJ_Uploader_Main_Window.setStatusBar(self.statusbar)
        self.actionView_Documentation = QtGui.QAction(FJ_Uploader_Main_Window)
        self.actionView_Documentation.setObjectName(
            _fromUtf8("actionView_Documentation"))
        self.actionAbout_Free_Journal = QtGui.QAction(FJ_Uploader_Main_Window)
        self.actionAbout_Free_Journal.setObjectName(
            _fromUtf8("actionAbout_Free_Journal"))
        self.actionNew_Collection = QtGui.QAction(FJ_Uploader_Main_Window)
        self.actionNew_Collection.setObjectName(
            _fromUtf8("actionNew_Collection"))
        self.actionQuit_FJ = QtGui.QAction(FJ_Uploader_Main_Window)
        self.actionQuit_FJ.setCheckable(False)
        self.actionQuit_FJ.setObjectName(_fromUtf8("actionQuit_FJ"))
        self.actionFree_Journal_Website = QtGui.QAction(
            FJ_Uploader_Main_Window)
        self.actionFree_Journal_Website.setObjectName(
            _fromUtf8("actionFree_Journal_Website"))
        self.actionGitHub_Source = QtGui.QAction(FJ_Uploader_Main_Window)
        self.actionGitHub_Source.setObjectName(_fromUtf8("actionGitHub_Source"))
        self.menuFile.addAction(self.actionNew_Collection)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit_FJ)
        self.menuHelp.addAction(self.actionFree_Journal_Website)
        self.menuHelp.addAction(self.actionGitHub_Source)
        self.menuHelp.addAction(self.actionView_Documentation)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Free_Journal)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(FJ_Uploader_Main_Window)
        QtCore.QObject.connect(self.actionQuit_FJ, QtCore.SIGNAL(
            _fromUtf8("triggered()")), FJ_Uploader_Main_Window.close)
        QtCore.QMetaObject.connectSlotsByName(FJ_Uploader_Main_Window)

    def retranslateUi(self, FJ_Uploader_Main_Window):
        FJ_Uploader_Main_Window.setWindowTitle(_translate("FJ_Uploader_Main_Window", "Free Journal Uploader", None))
        self.pushButtonNew.setText(_translate("FJ_Uploader_Main_Window", "New", None))
        self.pushButtonDelete.setText(_translate("FJ_Uploader_Main_Window", "Delete", None))
        self.pushButtonPublish.setText(_translate("FJ_Uploader_Main_Window", "Publish", None))
        self.pushButtonRemove.setText(_translate("FJ_Uploader_Main_Window", "<<<", None))
        self.pushButtonAdd.setText(_translate("FJ_Uploader_Main_Window", ">>>", None))
        self.treeWidgetCollections.headerItem().setText(0, _translate("FJ_Uploader_Main_Window", "Name", None))
        self.treeWidgetCollections.headerItem().setText(1, _translate("FJ_Uploader_Main_Window", "Address", None))
        self.treeWidgetCollections.headerItem().setText(2, _translate("FJ_Uploader_Main_Window", "URI", None))
        self.treeWidgetCollections.headerItem().setText(3, _translate("FJ_Uploader_Main_Window", "Title", None))
        self.treeWidgetCollections.headerItem().setText(4, _translate("FJ_Uploader_Main_Window", "Description", None))
        self.treeWidgetCollections.headerItem().setText(5, _translate("FJ_Uploader_Main_Window", "Date Created", None))
        self.labelCollections.setText(_translate("FJ_Uploader_Main_Window", "Collections", None))
        self.labelLocal.setText(_translate("FJ_Uploader_Main_Window", "Local Directory", None))
        self.labelOut.setText(_translate("FJ_Uploader_Main_Window", "Output:", None))
        self.menuFile.setTitle(_translate("FJ_Uploader_Main_Window", "File", None))
        self.menuHelp.setTitle(_translate("FJ_Uploader_Main_Window", "Help", None))
        self.actionView_Documentation.setText(_translate("FJ_Uploader_Main_Window", "View Documentation", None))
        self.actionView_Documentation.setShortcut(_translate("FJ_Uploader_Main_Window", "F1", None))
        self.actionAbout_Free_Journal.setText(_translate("FJ_Uploader_Main_Window", "About Free Journal", None))
        self.actionNew_Collection.setText(_translate("FJ_Uploader_Main_Window", "New Collection...", None))
        self.actionQuit_FJ.setText(_translate("FJ_Uploader_Main_Window", "Quit", None))
        self.actionFree_Journal_Website.setText(_translate("FJ_Uploader_Main_Window", "Free Journal Website", None))
        self.actionGitHub_Source.setText(_translate("FJ_Uploader_Main_Window", "View Source Code", None))
