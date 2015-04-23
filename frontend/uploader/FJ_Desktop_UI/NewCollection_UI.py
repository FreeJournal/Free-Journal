# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewCollection_UI.ui'
#
# Created: Tue Mar 17 14:10:57 2015
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


class Ui_DialogNewCollection(object):

    def setupUi(self, DialogNewCollection):
        DialogNewCollection.setObjectName(_fromUtf8("DialogNewCollection"))
        DialogNewCollection.resize(450, 500)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            DialogNewCollection.sizePolicy().hasHeightForWidth())
        DialogNewCollection.setSizePolicy(sizePolicy)
        DialogNewCollection.setMinimumSize(QtCore.QSize(450, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(_fromUtf8(":/Images/FreeJournal_icon.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.labelUploadDocument = QtGui.QLabel(DialogNewCollection)
        self.labelUploadDocument.setObjectName(
            _fromUtf8("labelUploadDocument"))
        self.verticalLayout.addWidget(self.labelUploadDocument)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEditAddDirectory = QtGui.QLineEdit(DialogNewCollection)
        self.lineEditAddDirectory.setObjectName(
            _fromUtf8("lineEditAddDirectory"))
        self.horizontalLayout.addWidget(self.lineEditAddDirectory)
        self.toolButtonAddDirectory = QtGui.QToolButton(DialogNewCollection)
        self.toolButtonAddDirectory.setObjectName(
            _fromUtf8("toolButtonAddDirectory"))
        self.horizontalLayout.addWidget(self.toolButtonAddDirectory)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.line_5 = QtGui.QFrame(DialogNewCollection)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout_4.addWidget(self.line_5)
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
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelPrivacy = QtGui.QLabel(DialogNewCollection)
        self.labelPrivacy.setObjectName(_fromUtf8("labelPrivacy"))
        self.horizontalLayout_2.addWidget(self.labelPrivacy)
        spacerItem = QtGui.QSpacerItem(
            40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.radioButtonPublic = QtGui.QRadioButton(DialogNewCollection)
        self.radioButtonPublic.setObjectName(_fromUtf8("radioButtonPublic"))
        self.horizontalLayout_2.addWidget(self.radioButtonPublic)
        self.radioButtonPrivate = QtGui.QRadioButton(DialogNewCollection)
        self.radioButtonPrivate.setObjectName(_fromUtf8("radioButtonPrivate"))
        self.horizontalLayout_2.addWidget(self.radioButtonPrivate)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
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
        DialogNewCollection.setWindowTitle(
            _translate("DialogNewCollection", "New Collection", None))
        self.label.setText(
            _translate("DialogNewCollection", "Create a new Collection by filling out the information below:", None))
        self.labelCollectionName.setText(
            _translate("DialogNewCollection", "Collection Name:", None))
        self.labelUploadDocument.setText(
            _translate("DialogNewCollection", "Upload Document:", None))
        self.toolButtonAddDirectory.setText(
            _translate("DialogNewCollection", "...", None))
        self.label_3.setText(
            _translate("DialogNewCollection", "Password:", None))
        self.label_2.setText(
            _translate("DialogNewCollection", "Description:", None))
        self.labelAddKeywords.setText(
            _translate("DialogNewCollection", "Add Keywords:", None))
        self.labelPrivacy.setText(
            _translate("DialogNewCollection", "Collection Privacy Setting:", None))
        self.radioButtonPublic.setText(
            _translate("DialogNewCollection", "Public", None))
        self.radioButtonPrivate.setText(
            _translate("DialogNewCollection", "Private", None))

from .frontend.uploader import resources_rc
