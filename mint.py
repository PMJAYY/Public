'''
Created on Jun 26, 2014

@author: Phumudzo Muvhango
'''
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class login(QWidget):
    def __init__(self,parent= None):
        QWidget.__init__(self,parent)
        
        self.setWindowTitle("Login")
        self.resize(500,500)
             
        username = QLineEdit()
        username.setPlaceholderText("Username")
        password = QLineEdit()
        password.setPlaceholderText("Password")
        password.setEchoMode(2)
        
        login = QPushButton("Login")
        cancel = QPushButton("Cancel")
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(login)
        hbox.addWidget(cancel)
        
        grid = QGridLayout()
        grid.setColumnStretch(0,1)
        grid.setColumnStretch(3,1)
        grid.setRowStretch(0,1)
        grid.setRowStretch(4,1)
        
        grid.addWidget(username,1,2)
        grid.addWidget(password,2,2)
        grid.addLayout(hbox,3,2)
    
        
        self.setLayout(grid)  
        self.connect(cancel, SIGNAL("clicked()"),qApp,SLOT("quit()"))
        
        
    def closeEvent(self,event):
        print("\a")
        reply = QMessageBox.question(self,"Message","Are you sure you want to quit?",QMessageBox.Yes,QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept()
        
        else:
            event.ignore()

    
app = QApplication(sys.argv)
block = login()
block.show()
sys.exit(app.exec_())
        
