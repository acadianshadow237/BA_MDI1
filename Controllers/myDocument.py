
from argparse import ArgumentParser, RawTextHelpFormatter
from functools import partial
import sys

from PySide6.QtCore import (QByteArray, QFile, QFileInfo, QPoint, QSettings,
        QSaveFile, QSize, QTextStream, Qt)
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow,
        QMdiArea, QMessageBox, QTextEdit, QWidget)


class Document(QtWidgets.QWidget):
    """Generic document widget."""

    def __init__(self, filename, parent=None):
        super(Document, self).__init__(parent)
  
        self.filename = filename
        self.warningLabel = self.createWarningLabel()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.warningLabel)
        if doc_type == 1:
            v = VAS_view()
            v.fileName = self.filename
        layout.addWidget(v)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        # Load the file.
        QtCore.QCoreApplication.instance().processEvents()
        self.reload()

    def createTextEdit(self):
        """Create text editor."""
        textEdit = QtWidgets.QTextEdit(self)
        # Disable editing.
        textEdit.setReadOnly(True)
        # Set a monospace font for content.
        textEdit.setFont(QtGui.QFont("Monospace", 10))
        return textEdit

    def createWarningLabel(self):
        label = QtWidgets.QLabel(self)
        label.setObjectName("warningLabel")
        label.setStyleSheet(
            "padding: 16px;"
            "background-color: #f9ac3a;"
            "border: none;"
        )
        label.setWordWrap(True)
        label.hide()
        return label

    def reload(self):
        """Reload from file."""
        #with open(self.filename) as f:
        #    self.timestamp = os.path.getmtime(self.filename)
        #    self.textEdit.setText(f.read())
        #    self.fileLoaded.emit(self)
        self.clearWarning()

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

