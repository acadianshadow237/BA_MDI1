

from PySide6 import QtCore
from PySide6 import QtGui
from PySide6 import QtWidgets
import argparse
import sys, os

from Models.login_model import login_stuff, url_builder
from helpers.helpers1 import db_tables
from Views.sample_login import LoginForm

from Views.all_view import VAS_view,VCRH_view ,VCCP_view,VCRH_Edit, VProj_Edit,VCRLD_Edit,  RPE_Edit
from Views.editmenu import splitSections, tweakSections, moveSections, copySections

from helpers.mmenus import menu_cascade
from Controllers.orm_select import county_select
from Controllers.controller import connectToDatabase
from Models.my_tables_model import gather_tables

from Controllers.my_MDIArea import MdiArea

__version__ = "1.0.0"

__my_debug__ = True

# -----------------------------------------------------------------------------
#  Main window class.
# -----------------------------------------------------------------------------

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        self.mdiArea = QtWidgets.QMdiArea() 
       
        self.setCentralWidget(self.mdiArea)

        self.AppTitle = self.tr("MDI Pavement Management")
        self.AppVersion = __version__
        
        self.my_login = login_stuff()
        self.my_url = None
        self.my_session = None
        self.login_flag = False
        self.my_db_tables = db_tables
        
        
        self.index = 0
        # Setup main window.
        self.setWindowTitle(self.AppTitle)
        self.setWindowIcon(QtGui.QIcon.fromTheme('utilities-system-monitor'))
        self.resize(1200, 600)
        self.document_type=0
        self.count = 0
        menu_cascade(self)
     
        self.statusbarAct = QtGui.QAction(self.tr("&Statusbar"), self)
        self.statusbarAct.setCheckable(True)
        self.statusbarAct.setChecked(True)
        self.statusbarAct.setStatusTip(self.tr("Show or hide the statusbar in the current window"))
        self.statusbarAct.toggled.connect(self.onToggleStatusBar)
 
         
   
    def onOpen(self):
        """Select a file using a file open dialog."""
         
        if self.document_type == 1:

            my_list=[]
            #self.actionUpdate.triggered.connect(self.onEdit)
            fileName = "VAS"
            the_doc = VAS_view(self)
            self.count = self.count +1                   
            the_doc.fileName = fileName + str(self.count)
            sub = self.mdiArea.addSubWindow(the_doc)
            sub.show()
            
            #self.loadDocument(fileName)

        if self.document_type == 2:
            fileName = "VCCP"
            the_doc = VCCP_view(self)
            self.count = self.count + 1                   
            the_doc.fileName = fileName + str(self.count)   
            sub = self.mdiArea.addSubWindow(the_doc)
            sub.show()
            #self.loadDocument(fileName)

        if self.document_type == 3:
            fileName = 'VCRH'
            the_doc = VCRH_Edit(self)
            self.count = self.count + 1                   
            the_doc.fileName = fileName + str(self.count)   
            sub = self.mdiArea.addSubWindow(the_doc)
            sub.show()

        if self.document_type == 4:
            fileName = 'VCRLD'
            the_doc = VCRLD_Edit(self)
            self.count = self.count + 1                   
            the_doc.fileName = fileName + str(self.count)   
            sub = self.mdiArea.addSubWindow(the_doc)
            sub.show()

        if self.document_type == 5:
            fileName = 'VProj'
            the_doc = VProj_Edit(self)
            self.count = self.count + 1                   
            the_doc.fileName = fileName + str(self.count)   
            sub = self.mdiArea.addSubWindow(the_doc)
            sub.show()

        if self.document_type == 6:
            fileName = 'EditLayers'
            the_doc =  RPE_Edit(self)
            self.count = self.count + 1                   
            the_doc.fileName = fileName + str(self.count)   
            sub = self.mdiArea.addSubWindow(the_doc)
            sub.show()

        if self.document_type == 7:
            fileName = 'Split_Section'
            the_doc = splitSections(self)
            self.count = self.count+1
            the_doc.fileName = fileName + str(self.count) 
            sub = self.mdiArea.addSubWindow(the_doc)
            sub.show()

        if self.document_type == 8:
            fileName = 'Tweak_Section'
            the_doc = tweakSections(self)
            self.count = self.count+1
            the_doc.fileName = fileName + str(self.count) 
            sub = self.mdiArea.addSubWindow(the_doc)
            sub.show()

        if self.document_type == 9:
            fileName = 'Move_Section'
            the_doc = moveSections(self)
            self.count = self.count+1
            the_doc.fileName = fileName + str(self.count) 
            sub = self.mdiArea.addSubWindow(the_doc)
            sub.show()

        if self.document_type == 10:
            fileName = 'Copy_Section'
            the_doc = copySections(self)
            self.count = self.count+1
            the_doc.fileName = fileName + str(self.count) 
            sub = self.mdiArea.addSubWindow(the_doc)
            sub.show()

    def onToggleStatusBar(self):
        """Toggles the visibility of the status bar."""
        self.statusBar().setVisible(self.statusbarAct.isChecked())

    def onContents(self):
        QtWidgets.QMessageBox.information(self, self.tr("Contents"), self.tr("<p>Please refer to...</p>"))

    def onAbout(self):
        QtWidgets.QMessageBox.information(self, self.tr("About"),
             self.tr("<p><strong>{}</strong></p>"
            "<p>Version {}</p>"
            "<p>Authors: ...</p>").format(self.AppTitle, self.AppVersion)
        )

   


    def onLogin(self):
        if __my_debug__ == True:
            self.login_flag = True
            self.my_db_tables = db_tables
            #self.my_url = f'oracle+cx_oracle://USER_MISS:password@ORACLEDEV01:1521/GISDEV'
            self.my_login = login_stuff()
            self.my_login.user_name = 'USER_MISS'
            self.my_login.user_password = 'password'
            self.my_login.database_name = 'GISDEV'
            self.my_login.database_type = 0
            self.my_login.schema ='USER_MISS'
            self.my_login.server_name = 'ORACLEDEV01'
            self.my_url = url_builder(self.my_login)
            self.my_session = connectToDatabase(self.my_url)
            self.document_type = 1
            gather_tables(self)
            menu_cascade(self)
               

        else:
            self.my_login = login_stuff()
            self.my_url = None
            self.login_flag = False
            self.document_type = 0
            myresults = LoginForm(self)
            myresults.exec()

            if myresults.login_flag == True:
                self.my_db_table = myresults.db
                self.my_url = myresults.my_url
                self.my_login = myresults.my_login                
                self.login_flag = True
                self.my_session = connectToDatabase(self.my_url)
                menu_cascade(self)
            else:
                print('Failed')
            
        pass
    
    def onLogout(self):
        self.my_url = None
        self.db = None
        self.my_login = None
        self.login_flag = False
        self.document_type = 0
        self.my_session.close()
        for item in self.mdiArea.subWindowList():
            item.close()
        menu_cascade(self)

    def onExit(self):
        for item in self.mdiArea.subWindowList():
            item.my_session.close()
            item.close()
        self.close()
        pass

    # View Menu Area
    def onVAS(self):
        self.document_type = 1
        #menu_cascade(self)
        ##my_doc = Ui_VAS_Form()
        self.onOpen()
    
    def onVCRHVCRLDVPROJ(self):
        self.document_type = 2
        #menu_cascade(self)
        self.onOpen()

    def onVCRH(self):
        self.document_type = 3
        #menu_cascade(self)
        self.onOpen()

    def onVCRLD(self):
        self.document_type = 4
        #menu_cascade(self)
        self.onOpen()

    def onVPRJ(self):
        self.document_type = 5
        #menu_cascade(self)
        self.onOpen()

    def onLog(self):
        print('Made it to Log')

    ## project menu area
    def onNewProject(self):
        print('Made it to New Project')

    def onRenameProject(self):
        print('made it to rename project')

    def onCopyProject(self):
        print('made it to Copy Project')

    def onEditLayers(self):
        self.document_type = 6
        #menu_cascade(self)
        self.onOpen()
    
    # edit Menu Layers

    def onSplitSection(self):
        self.document_type = 7
        self.onOpen()


    def onTweakSection(self):
        self.document_type = 8
        self.onOpen()
     
    def onMoveSection(self):
        self.document_type = 9
        self.onOpen()

    def onCopySection(self):        
        self.document_type = 10
        self.onOpen()


    def loadDocument(self, filename):
        """Load document from filename."""
       
        #for index in range(self.mdiArea.count()):
            
        #    document = self.mdiArea.widget(index)
        #    if document:
        #        if filename == document.filename:
        #            self.mdiArea.setCurrentIndex(index)
        #            document.reload()
        #            return
        # Else load from file and create new document tab.

        self.statusBar.showMessage(self.tr("Loading..."), 2500)

        document = Document(filename, self)
        index = self.mdiArea.addDocument(document)
        #self.mdiArea.setCurrentIndex(index)
        index.show()

        # After loading a conenction file, it is possible to refresh the current module.
        self.refreshAct.setEnabled(True)
        self.statusBar.showMessage(self.tr("Successfully loaded file"), 2500)

        # Enable close action
        #self.closeAct.setEnabled(self.mdiArea.count())

class MdiArea(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(MdiArea, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self._is_untitled = True
        self.index = 0
       
       
    def addDocument(self, document):
        document.fileChanged.connect(self.onFileChanged)
        document.fileLoaded.connect(self.onFileLoaded)
        sub = QtWidgets.QMdiSubWindow()
        sub.setWidget(document)
      
        return sub


    def currentDocument(self):
        """Return current active document."""
        return self.widget(self.currentIndex())

    def documents(self):
        """Returns iterator of all documents."""
        for index in range(self.count()):
            yield self.widget(index)

    def closeDocument(self):
        """Close current active document. Provided for convenience.
        """
        index = self.currentIndex()
        # Finally remove tab by index.
        self.removeTab(index)

    def setDocumentChanged(self, document, changed):
        index = self.indexOf(document)
        label = document.filename
        self.setTabText(index, "{}{}".format('*' if changed else '', label))

    def checkTimestamps(self):
        for document in self.documents():
            document.checkTimestamp()

    def onFileLoaded(self, document):
        self.setDocumentChanged(document, False)

    def onFileChanged(self, document):
        self.setDocumentChanged(document, True)



class Document(QtWidgets.QWidget):
    """Generic document widget."""

    fileLoaded = QtCore.Signal(QtWidgets.QWidget)
    fileChanged = QtCore.Signal(QtWidgets.QWidget)

    def __init__(self, filename, my_parent, parent=None):
        super(Document, self).__init__(parent)
        
        self.document_type = my_parent.document_type
        self.my_db_tables = my_parent.my_db_tables
        self.my_url = my_parent.my_url
        self.my_login = my_parent.my_login
        self.my_session = my_parent.my_session
        self.filename =filename
        self.documentEdit = self.createDocumentEdit()
        self.my_parent = my_parent
        #self.warningLabel = self.createWarningLabel()
        #layout = QtWidgets.QVBoxLayout()
        #layout.addWidget(self.warningLabel)
        #layout.addWidget(self.textEdit)
        #layout.setSpacing(0)
        #layout.setContentsMargins(0, 0, 0, 0)
        #self.setLayout(layout)
        ## Load the file.
        QtCore.QCoreApplication.instance().processEvents()
        self.reload()

    def createDocumentEdit(self):

        if self.document_type == 1:
       
             my_document =  VAS_view(self)

        if self.document_type == 2:
            my_document =  VCCP_view(self)
        # Disable editing.
        #textEdit.setReadOnly(True)
        ## Set a monospace font for content.
        #textEdit.setFont(QtGui.QFont("Monospace", 10))
        return my_document

    #def createWarningLabel(self):
    #    label = QtWidgets.QLabel(self)
    #    label.setObjectName("warningLabel")
    #    label.setStyleSheet(
    #        "padding: 16px;"
    #        "background-color: #f9ac3a;"
    #        "border: none;"
    #    )
    #    label.setWordWrap(True)
    #    label.hide()
    #    return label

    def reload(self):
        #"""Reload from file."""
        #with open(self.filename) as f:
        #    self.timestamp = os.path.getmtime(self.filename)
        #    self.textEdit.setText(f.read())
        #    self.fileLoaded.emit(self)
        #self.clearWarning()
        pass

    def clearWarning(self):
        """Clear the warning badge located at the top of the document."""
        self.warningLabel.clear()
        self.warningLabel.hide()

    def showWarning(self, message):
        """Show a warning badge displaying a message located at the top of the document."""
        self.warningLabel.setText(message)
        self.warningLabel.show()

    def checkTimestamp(self):
        timestamp = os.path.getmtime(self.filename)
        if timestamp > self.timestamp:
            self.showWarning(self.tr("<strong>The file {} changed on disk.</strong> Reload (hit Ctrl+R) to see the changes.").format(self.filename))
            self.fileChanged.emit(self)
        else:
            self.clearWarning()



# -----------------------------------------------------------------------------
#  Parsing command line arguments
# -----------------------------------------------------------------------------
def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(prog=os.path.basename(__file__), description="")
    parser.add_argument('filename', nargs="*", metavar='<file>', help="file")
    parser.add_argument('-V, --version', action='version', version='%(prog)s {}'.format(__version__))
    return parser.parse_args()

# -----------------------------------------------------------------------------
#  Main routine
# -----------------------------------------------------------------------------

def main():
    """Main routine."""
    args = parse_args()

    # Create application and main window.
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # Open connections file using command line argument.
    for filename in args.filename:
        window.loadDocument(filename)

    # Run execution loop.
    return app.exec()

if __name__ == '__main__':

   exit(main())
