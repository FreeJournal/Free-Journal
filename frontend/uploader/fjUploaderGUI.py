import sys
from PyQt4 import QtCore, QtGui
import frontend.uploader.FJ_Desktop_UI.fjUploaderUI as UploaderUI
import frontend.uploader.FJ_Desktop_UI.NewCollection_UI as NewCollection_UI
import frontend.uploader.FJ_Desktop_UI.About_UI as About_UI
import webbrowser
from frontend.cli import commands as CLI
from os.path import isfile
import os.path


class StartQT4(QtGui.QMainWindow):

    model = QtGui.QDirModel()
    index = QtCore.QModelIndex()
    indexCollec = 0

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = UploaderUI.Ui_FJ_Uploader_Main_Window()
        self.ui.setupUi(self)

        # Tree Defintions
        self.model = QtGui.QDirModel()
        self.model.setReadOnly(True)
        self.ui.treeViewLocal.setModel(self.model)
        self.model.setSorting(
            QtCore.QDir.DirsFirst | QtCore.QDir.IgnoreCase | QtCore.QDir.Name)
        self.index = QtCore.QModelIndex()
        self.index = self.model.index(os.path.expanduser('~/Documents'))
        self.ui.treeViewLocal.expand(self.index)
        self.ui.treeViewLocal.scrollTo(self.index)
        self.ui.treeViewLocal.setCurrentIndex(self.index)
        self.ui.treeViewLocal.resizeColumnToContents(0)
        self.indexCollec = self.ui.treeWidgetCollections.currentIndex()
        self.UpdateTreeFromCache()

        # button definitions
        self.ui.pushButtonNew.clicked.connect(self.NewCollecWindowOpen)
        self.ui.actionNew_Collection.triggered.connect(self.NewCollecWindowOpen)
        self.ui.actionAbout_Free_Journal.triggered.connect(self.NewAboutWindowOpen)
        self.ui.actionFree_Journal_Website.triggered.connect(self.FJWeb)
        self.ui.actionGitHub_Source.triggered.connect(self.FJSource)
        self.ui.actionView_Documentation.triggered.connect(self.FJDocs)
        self.ui.pushButtonDelete.clicked.connect(self.DeleteCollection)
        self.ui.pushButtonPublish.clicked.connect(self.Publish)
        self.ui.treeWidgetCollections.itemClicked.connect(self.EnableFunctions)
        self.ui.pushButtonAdd.clicked.connect(self.AddDoc)
        self.ui.pushButtonRemove.clicked.connect(self.RemoveDoc)

        self.ui.lineEditOut.setText("Click 'New' to create a new Colleciton.")

    def AddDoc(self):
        self.index = self.ui.treeViewLocal.currentIndex()
        filepath = str(self.model.filePath(self.index))
        selectedItem = self.ui.treeWidgetCollections.currentItem()
        collection_address = str(selectedItem.text(1))
        title = "None"
        description = "None"
        (titleGet, truth) = QtGui.QInputDialog.getText(
            self, "Doc Title", "Title:", QtGui.QLineEdit.Normal, "None")
        if truth == True:
            title = str(titleGet)
        (Desc, truthD) = QtGui.QInputDialog.getText(
            self, "Doc Description", "Description:", QtGui.QLineEdit.Normal, "None")
        if truthD == True:
            description = str(Desc)
        if truth == True & truthD == True:
            if isfile(filepath):
                if not title == '':
                    CLI.put_document(
                        filepath, collection_address, title, description)
                    self.UpdateTreeFromCache()
                    self.ui.lineEditOut.setText(
                        "Inserted Document successfully!")
                else:
                    message = QtGui.QMessageBox(self)
                    message.setText("Please enter a title.")
                    message.setWindowTitle("Error")
                    message.setIcon(QtGui.QMessageBox.Warning)
                    message.addButton("OK", QtGui.QMessageBox.AcceptRole)
                    message.exec_()
            else:
                 message = QtGui.QMessageBox(self)
                 message.setText("Please select a valid file.")
                 message.setWindowTitle("Error")
                 message.setIcon(QtGui.QMessageBox.Warning)
                 message.addButton("OK", QtGui.QMessageBox.AcceptRole)
                 message.exec_() 
           
    def RemoveDoc(self):
        if self.ui.treeWidgetCollections.currentItem() is None: return
        selectedItem = self.ui.treeWidgetCollections.currentItem()
        document_hash = str(selectedItem.text(2))
        if document_hash != '':
            document = CLI.cache.get_document_by_hash(document_hash)
            CLI.cache.remove_document(document)
            self.UpdateTreeFromCache()
        
    def EnableFunctions(self):
        self.ui.pushButtonPublish.setEnabled(True)
        self.ui.pushButtonDelete.setEnabled(True)
        self.ui.pushButtonAdd.setEnabled(True)
        self.ui.pushButtonRemove.setEnabled(True)
    
    def DisableFunctions(self):
        self.ui.pushButtonPublish.setEnabled(False)
        self.ui.pushButtonDelete.setEnabled(False)
        self.ui.pushButtonAdd.setEnabled(False)
        self.ui.pushButtonRemove.setEnabled(False)
        
    def UpdateTreeFromCache(self):
        self.ui.treeWidgetCollections.clear()
        for collection in CLI.cache.get_all_collections():
            initialItem = QtGui.QTreeWidgetItem(self.ui.treeWidgetCollections)
            initialItem.setText(0, collection.title)
            initialItem.setText(1, collection.address)
            initialItem.setText(
                5, collection.creation_date.strftime("%A, %d. %B %Y %I:%M%p"))
            documents = CLI.cache.get_documents_from_collection(
                collection.address)
            count = 0
            for doc in documents:
                newDoc = QtGui.QTreeWidgetItem()
                initialItem.addChild(newDoc)
                initialItem.child(count).setText(2, doc.hash)
                initialItem.child(count).setText(3, doc.title)
                initialItem.child(count).setText(4, doc.description)
                count += 1
        self.ui.treeWidgetCollections.setSortingEnabled(True)

    def FJSource(self):
        webbrowser.open(
            'https://www.github.com/FreeJournal/freejournal', new=0, autoraise=True)

    def FJDocs(self):
        webbrowser.open(
            'https://www.github.com/FreeJournal/freejournal/wiki', new=0, autoraise=True)

    def FJWeb(self):
        webbrowser.open('http://www.freejournal.org', new=0, autoraise=True)

    def Publish(self, checked=None):
        if checked==None: return
        if self.ui.treeWidgetCollections.currentItem() is None: return
        selectedItem = self.ui.treeWidgetCollections.currentItem()
        collection_address = str(selectedItem.text(1))
        (password, pressed) = QtGui.QInputDialog.getText(self, "Collection Password",
                                                         "Enter the collection password:", QtGui.QLineEdit.Normal, "")
        if pressed == True:
            if not password == '':
                address_password = password
                CLI.publish_collection(address_password, collection_address)
                self.ui.lineEditOut.setText(
                    "Collection published successfully!")
                self.UpdateTreeFromCache()
            else:
                message = QtGui.QMessageBox(self)
                message.setText("Please enter a password.")
                message.setWindowTitle("Error")
                message.setIcon(QtGui.QMessageBox.Warning)
                message.addButton("OK", QtGui.QMessageBox.AcceptRole)
                message.exec_()
                
    def DeleteCollection(self, checked=None):
        if checked==None: return
        if self.ui.treeWidgetCollections.currentItem() is None: return
        message = QtGui.QMessageBox(self)
        message.setText("Are you sure you want to delete this Collection?")
        message.setWindowTitle("Delete Collection")
        message.setIcon(QtGui.QMessageBox.Warning)
        message.addButton("Yes", QtGui.QMessageBox.AcceptRole)
        message.addButton("No", QtGui.QMessageBox.RejectRole)
        message.setDetailedText(
            "This will not remove any local files in this collection.")
        message.exec_()
        decision = message.clickedButton().text()
        if decision == "Yes":
            selectedItem = self.ui.treeWidgetCollections.currentItem()
            collection_address = str(selectedItem.text(1))
            itemIndex = self.ui.treeWidgetCollections.indexOfTopLevelItem(
                selectedItem)
            garbage = self.ui.treeWidgetCollections.takeTopLevelItem(itemIndex)
            collection = CLI.cache.get_collection_with_address(
                collection_address)
            CLI.cache.remove_collection(collection)
            self.ui.lineEditOut.setText("Collection deleted successfully!")
            if self.ui.treeWidgetCollections.currentItem() is None:
                self.DisableFunctions()
                
    
    def NewAboutWindowOpen(self, checked=None):
        if checked == None:
            return
        NewAbout = QtGui.QDialog()
        NewAbout.ui = About_UI.Ui_Form()
        NewAbout.ui.setupUi(NewAbout)
        NewAbout.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        NewAbout.exec_() 

    def NewCollecWindowOpen(self, checked=None):
        if checked == None:
            return
        dialogObject = NewCollecWindow(self)
        dialogObject.show()

class NewCollecWindow(QtGui.QDialog):

    def __init__(self, parent):
        global main_UI
        main_UI = parent
        QtGui.QDialog.__init__(self, parent)
        self.ui = NewCollection_UI.Ui_DialogNewCollection()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.title = ''
        self.description = ''
        self.keywords = ''
        self.btc = ''
        self.address_password = ''
        self.collection_address = ''
        self.ui.buttonBoxConfirm.accepted.connect(self.PutCollection)
        
      def PutCollection(self):
          self.address_password = str(self.ui.lineEditPassword.text())
          self.title = str(self.ui.lineEditCollectionName.text())
          self.description = str(self.ui.plainTextEditDescription.toPlainText())
          self.keywords = str(self.ui.plainTextEditAddKeywords.toPlainText())
          self.btc = "btc123"         
          if self.address_password == '': 
              message = QtGui.QMessageBox(self)
              message.setText("A Collection password is required.")
              message.setWindowTitle("Error")
              message.setIcon(QtGui.QMessageBox.Warning)
              message.addButton("OK", QtGui.QMessageBox.AcceptRole)
              message.exec_()   
          elif self.title == '':
              message = QtGui.QMessageBox(self)
              message.setText("Please enter a Collection title.")
              message.setWindowTitle("Error")
              message.setIcon(QtGui.QMessageBox.Warning)
              message.addButton("OK", QtGui.QMessageBox.AcceptRole)
              message.exec_() 
          else:
              CLI.put_collection(self.address_password, self.title, self.description, self.keywords, self.btc)
              main_UI.ui.lineEditOut.setText("Collection created successfully!")
              main_UI.UpdateTreeFromCache()
      

def run():
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
