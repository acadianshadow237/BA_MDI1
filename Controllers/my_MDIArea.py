
from argparse import ArgumentParser, RawTextHelpFormatter
from functools import partial
import sys

from PySide6.QtCore import (QByteArray, QFile, QFileInfo, QPoint, QSettings,
        QSaveFile, QSize, QTextStream, Qt)
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow,
        QMdiArea, QMessageBox, QTextEdit, QWidget,QMdiSubWindow)


class MdiArea(QWidget):

    def __init__(self, my_parrent):
        super(self).__init__()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self._is_untitled = True

        self.count = 0

    def addDocument(self, document):
        document.fileChanged.connect(self.onFileChanged)
        document.fileLoaded.connect(self.onFileLoaded)
        sub = QMdiSubWindow()
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

