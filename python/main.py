#!/usr/bin/env python

# NOTE: needs Python 2, for pyqt5
# https://bugs.kde.org/show_bug.cgi?id=362967

import sys
import PyQt5
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QWidget, QLineEdit, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QMenu, QWidgetAction, QApplication)

def handler(msg_type, msg_log_context, msg_string):
    print(msg_string)
PyQt5.QtCore.qInstallMessageHandler(handler)

class PopupAction(QWidgetAction):

    # From KoLineEditAction::KoLineEditAction(QObject* parent)
    def __init__(self, parent):
        super(QWidgetAction, self).__init__(parent)
        widget = QWidget(None)
        label1 = QLabel(None)
        input1 = QLineEdit(None)
        input1.setPlaceholderText("New tag")
        #print(dir(input1))
        hbox = QHBoxLayout()
        hbox.addWidget(label1)
        hbox.addWidget(input1)
        widget.setLayout(hbox)
        self.setDefaultWidget(widget)

    def test(self, e):
        print(e)

class PopupMenu(QMenu):

    def __init__(self, parent):
        super(QMenu, self).__init__(parent)
        self.initUI()

    def initUI(self):
        menu = self.addMenu("ASSIGN?")
        menu.addAction(PopupAction(self)) # bug here! even if parent is self or None
        
        #self.addAction(PopupAction(self)) # no bug here!

class Window(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel()
        label1.setText("Enter your text")

        input1 = QLineEdit()

        button1 = QPushButton("Show menu")

        popup = PopupMenu(self)
        button1.setMenu(popup)

        hbox = QHBoxLayout()
        hbox.addWidget(label1)
        hbox.addWidget(input1)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(button1)
        
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')    
        self.show()

    def addInputBox(self):
        print("OI")
        pass


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = Window()
    w.resize(530, 140)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())