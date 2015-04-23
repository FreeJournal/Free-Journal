# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_Comment_UI.ui'
#
# Created: Sun Mar 15 19:19:20 2015
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


class Ui_DialogAddComment(object):

    def setupUi(self, DialogAddComment):
        DialogAddComment.setObjectName(_fromUtf8("DialogAddComment"))
        DialogAddComment.resize(275, 200)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            DialogAddComment.sizePolicy().hasHeightForWidth())
        DialogAddComment.setSizePolicy(sizePolicy)
        DialogAddComment.setMinimumSize(QtCore.QSize(275, 200))
        DialogAddComment.setMaximumSize(QtCore.QSize(275, 286))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(_fromUtf8(":/Images/FreeJournal_icon.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogAddComment.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(DialogAddComment)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelAddComment = QtGui.QLabel(DialogAddComment)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelAddComment.setFont(font)
        self.labelAddComment.setObjectName(_fromUtf8("labelAddComment"))
        self.verticalLayout.addWidget(self.labelAddComment)
        self.plainTextEditAddComment = QtGui.QPlainTextEdit(DialogAddComment)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.plainTextEditAddComment.sizePolicy().hasHeightForWidth())
        self.plainTextEditAddComment.setSizePolicy(sizePolicy)
        self.plainTextEditAddComment.setObjectName(
            _fromUtf8("plainTextEditAddComment"))
        self.verticalLayout.addWidget(self.plainTextEditAddComment)
        self.labelWordCount = QtGui.QLabel(DialogAddComment)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        font.setKerning(True)
        self.labelWordCount.setFont(font)
        self.labelWordCount.setObjectName(_fromUtf8("labelWordCount"))
        self.verticalLayout.addWidget(self.labelWordCount)
        self.lineAddComment = QtGui.QFrame(DialogAddComment)
        self.lineAddComment.setFrameShape(QtGui.QFrame.HLine)
        self.lineAddComment.setFrameShadow(QtGui.QFrame.Sunken)
        self.lineAddComment.setObjectName(_fromUtf8("lineAddComment"))
        self.verticalLayout.addWidget(self.lineAddComment)
        self.buttonBoxAddComment = QtGui.QDialogButtonBox(DialogAddComment)
        self.buttonBoxAddComment.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxAddComment.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.buttonBoxAddComment.setObjectName(
            _fromUtf8("buttonBoxAddComment"))
        self.verticalLayout.addWidget(self.buttonBoxAddComment)

        self.retranslateUi(DialogAddComment)
        QtCore.QObject.connect(self.buttonBoxAddComment, QtCore.SIGNAL(
            _fromUtf8("accepted()")), DialogAddComment.accept)
        QtCore.QObject.connect(self.buttonBoxAddComment, QtCore.SIGNAL(
            _fromUtf8("rejected()")), DialogAddComment.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogAddComment)

    def retranslateUi(self, DialogAddComment):
        DialogAddComment.setWindowTitle(
            _translate("DialogAddComment", "Add Comment", None))
        self.labelAddComment.setText(
            _translate("DialogAddComment", "Add Comment to :", None))
        self.labelWordCount.setText(
            _translate("DialogAddComment", "Max Word Count: 100", None))

from .frontend.uploader import resources_rc
