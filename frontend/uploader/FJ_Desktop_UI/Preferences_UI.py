# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Preferences_UI.ui'
#
# Created: Sun Mar 15 19:21:40 2015
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


class Ui_DialogPreferences(object):

    def setupUi(self, DialogPreferences):
        DialogPreferences.setObjectName(_fromUtf8("DialogPreferences"))
        DialogPreferences.resize(550, 450)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            DialogPreferences.sizePolicy().hasHeightForWidth())
        DialogPreferences.setSizePolicy(sizePolicy)
        DialogPreferences.setMinimumSize(QtCore.QSize(550, 450))
        DialogPreferences.setMaximumSize(QtCore.QSize(550, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(_fromUtf8(":/Images/FreeJournal_icon.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogPreferences.setWindowIcon(icon)
        DialogPreferences.setAutoFillBackground(False)
        self.gridLayout_2 = QtGui.QGridLayout(DialogPreferences)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.buttonBoxPreferences = QtGui.QDialogButtonBox(DialogPreferences)
        self.buttonBoxPreferences.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxPreferences.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.buttonBoxPreferences.setObjectName(
            _fromUtf8("buttonBoxPreferences"))
        self.gridLayout_2.addWidget(self.buttonBoxPreferences, 3, 1, 1, 2)
        self.listWidgetPreferences = QtGui.QListWidget(DialogPreferences)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.listWidgetPreferences.sizePolicy().hasHeightForWidth())
        self.listWidgetPreferences.setSizePolicy(sizePolicy)
        self.listWidgetPreferences.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidgetPreferences.setMaximumSize(QtCore.QSize(100, 16777215))
        self.listWidgetPreferences.setObjectName(
            _fromUtf8("listWidgetPreferences"))
        item = QtGui.QListWidgetItem()
        self.listWidgetPreferences.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidgetPreferences.addItem(item)
        self.gridLayout_2.addWidget(self.listWidgetPreferences, 0, 0, 2, 1)
        self.pushButtonPreferences = QtGui.QPushButton(DialogPreferences)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButtonPreferences.sizePolicy().hasHeightForWidth())
        self.pushButtonPreferences.setSizePolicy(sizePolicy)
        self.pushButtonPreferences.setObjectName(
            _fromUtf8("pushButtonPreferences"))
        self.gridLayout_2.addWidget(self.pushButtonPreferences, 3, 3, 1, 1)
        self.framePreferences = QtGui.QFrame(DialogPreferences)
        self.framePreferences.setFrameShape(QtGui.QFrame.StyledPanel)
        self.framePreferences.setFrameShadow(QtGui.QFrame.Raised)
        self.framePreferences.setObjectName(_fromUtf8("framePreferences"))
        self.gridLayout_2.addWidget(self.framePreferences, 0, 1, 2, 3)
        self.linePreferences = QtGui.QFrame(DialogPreferences)
        self.linePreferences.setFrameShape(QtGui.QFrame.HLine)
        self.linePreferences.setFrameShadow(QtGui.QFrame.Sunken)
        self.linePreferences.setObjectName(_fromUtf8("linePreferences"))
        self.gridLayout_2.addWidget(self.linePreferences, 2, 0, 1, 4)

        self.retranslateUi(DialogPreferences)
        QtCore.QObject.connect(self.buttonBoxPreferences, QtCore.SIGNAL(
            _fromUtf8("accepted()")), DialogPreferences.accept)
        QtCore.QObject.connect(self.buttonBoxPreferences, QtCore.SIGNAL(
            _fromUtf8("rejected()")), DialogPreferences.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogPreferences)

    def retranslateUi(self, DialogPreferences):
        DialogPreferences.setWindowTitle(
            _translate("DialogPreferences", "Preferences", None))
        __sortingEnabled = self.listWidgetPreferences.isSortingEnabled()
        self.listWidgetPreferences.setSortingEnabled(False)
        item = self.listWidgetPreferences.item(0)
        item.setText(_translate("DialogPreferences", "General", None))
        item = self.listWidgetPreferences.item(1)
        item.setText(_translate("DialogPreferences", "Connection", None))
        self.listWidgetPreferences.setSortingEnabled(__sortingEnabled)
        self.pushButtonPreferences.setText(
            _translate("DialogPreferences", "Apply", None))

from .frontend.uploader import resources_rc
