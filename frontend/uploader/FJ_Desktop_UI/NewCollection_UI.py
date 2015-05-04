# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FINALNewCollection_UI.ui'
#
# Created: Thu Apr 23 00:13:28 2015
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


class Ui_DialogNewCollection(object):

    def setupUi(self, DialogNewCollection):
        DialogNewCollection.setObjectName(_fromUtf8("DialogNewCollection"))
        DialogNewCollection.resize(475, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            DialogNewCollection.sizePolicy().hasHeightForWidth())
        DialogNewCollection.setSizePolicy(sizePolicy)
        DialogNewCollection.setMinimumSize(QtCore.QSize(475, 500))
        icon = QtGui.QIcon(os.getcwd() + '/frontend/uploader/FJ_Desktop_UI/FreeJournal_icon.jpg')
        DialogNewCollection.setWindowIcon(icon)
        self.verticalLayout_4 = QtGui.QVBoxLayout(DialogNewCollection)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(DialogNewCollection)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelCollectionName = QtGui.QLabel(DialogNewCollection)
        self.labelCollectionName.setObjectName(
            _fromUtf8("labelCollectionName"))
        self.verticalLayout.addWidget(self.labelCollectionName)
        self.lineEditCollectionName = QtGui.QLineEdit(DialogNewCollection)
        self.lineEditCollectionName.setObjectName(
            _fromUtf8("lineEditCollectionName"))
        self.verticalLayout.addWidget(self.lineEditCollectionName)
        self.line_3 = QtGui.QFrame(DialogNewCollection)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.label_3 = QtGui.QLabel(DialogNewCollection)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.lineEditPassword = QtGui.QLineEdit(DialogNewCollection)
        self.lineEditPassword.setObjectName(_fromUtf8("lineEditPassword"))
        self.verticalLayout_4.addWidget(self.lineEditPassword)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.line_2 = QtGui.QFrame(DialogNewCollection)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_2.addWidget(self.line_2)
        self.label_2 = QtGui.QLabel(DialogNewCollection)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.plainTextEditDescription = QtGui.QPlainTextEdit(
            DialogNewCollection)
        self.plainTextEditDescription.setObjectName(
            _fromUtf8("plainTextEditDescription"))
        self.verticalLayout_2.addWidget(self.plainTextEditDescription)
        self.line_4 = QtGui.QFrame(DialogNewCollection)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_2.addWidget(self.line_4)
        self.labelAddKeywords = QtGui.QLabel(DialogNewCollection)
        self.labelAddKeywords.setObjectName(_fromUtf8("labelAddKeywords"))
        self.verticalLayout_2.addWidget(self.labelAddKeywords)
        self.plainTextEditAddKeywords = QtGui.QPlainTextEdit(
            DialogNewCollection)
        self.plainTextEditAddKeywords.setObjectName(
            _fromUtf8("plainTextEditAddKeywords"))
        self.verticalLayout_2.addWidget(self.plainTextEditAddKeywords)
        self.line = QtGui.QFrame(DialogNewCollection)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.buttonBoxConfirm = QtGui.QDialogButtonBox(DialogNewCollection)
        self.buttonBoxConfirm.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxConfirm.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.buttonBoxConfirm.setObjectName(_fromUtf8("buttonBoxConfirm"))
        self.verticalLayout_4.addWidget(self.buttonBoxConfirm)

        self.retranslateUi(DialogNewCollection)
        QtCore.QObject.connect(self.buttonBoxConfirm, QtCore.SIGNAL(
            _fromUtf8("accepted()")), DialogNewCollection.accept)
        QtCore.QObject.connect(self.buttonBoxConfirm, QtCore.SIGNAL(
            _fromUtf8("rejected()")), DialogNewCollection.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogNewCollection)

    def retranslateUi(self, DialogNewCollection):
        DialogNewCollection.setWindowTitle(_translate("DialogNewCollection", "New Collection", None))
        self.label.setText(_translate("DialogNewCollection", "Create a new Collection by filling out the information below:", None))
        self.labelCollectionName.setText(_translate("DialogNewCollection", "Collection Title:", None))
        self.label_3.setText(_translate("DialogNewCollection", "Password:", None))
        self.label_2.setText(_translate("DialogNewCollection", "Description:", None))
        self.labelAddKeywords.setText(_translate("DialogNewCollection", "Add Keywords:", None))
