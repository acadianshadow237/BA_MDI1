import sys
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QComboBox, QDialog)
from PySide6.QtCore import Qt

from Models.login_model import url_builder
from Models.login_model import login_stuff
from Controllers.controller import check_db_exists 

class LoginForm(QDialog):
	def __init__(self,my_stuff):
		super().__init__()
		self.setWindowTitle('Login Form')
		self.resize(500, 120)
		self.my_url = ''
		self.my_login = login_stuff()
		self.my_login.user_name = my_stuff.my_login.user_name
		self.my_login.user_password = my_stuff.my_login.user_password
		self.my_login.server_name =  my_stuff.my_login.server_name
		self.my_login.database_name = my_stuff.my_login.database_name
		self.my_login.schema = my_stuff.my_login.schema
		self.my_login.database_type = my_stuff.my_login.database_type	
		self.login_flag = False	
		
		#self.setWindowModality(Qt.ApplicationModal)

		layout = QGridLayout()
		#layout.setVerticalSpacing(1)
		#1
		label_name = QLabel('<font size="4">User Name:</font>')
		self.lineEdit_username = QLineEdit()
		self.lineEdit_username.setPlaceholderText('Please enter your User Name')
		layout.addWidget(label_name, 0, 0)
		layout.addWidget(self.lineEdit_username, 0, 1)
		#2
		label_password = QLabel('<font size="4">Password:</font>')
		self.lineEdit_password = QLineEdit()
		self.lineEdit_password.setEchoMode(QLineEdit.Password)
		self.lineEdit_password.setPlaceholderText('Please enter your password')
		layout.addWidget(label_password, 1, 0)
		layout.addWidget(self.lineEdit_password, 1, 1)
		#3
		label_servername = QLabel('<font size="4">Server Name:</font>')
		self.combo_servername = QComboBox()
		self.combo_servername.setPlaceholderText('Please enter your Server Name')
		self.combo_servername.setEditable(True)
		layout.addWidget(label_servername, 2, 0)
		layout.addWidget(self.combo_servername, 2, 1)
		#4
		label_databasename = QLabel('<font size="4">Database Name:</font>')
		self.combo_databasename = QComboBox()
		self.combo_databasename.setPlaceholderText('Please enter your Database Name')
		self.combo_databasename.setEditable(True)
		layout.addWidget(label_databasename, 3, 0)
		layout.addWidget(self.combo_databasename, 3, 1)

		label_schema = QLabel('<font size="4"> Schema: </font>')
		self.lineedit_schema = QLineEdit()
		self.lineedit_schema.setPlaceholderText('Please enter your Database Name')
		layout.addWidget(label_schema, 4, 0)
		layout.addWidget(self.lineedit_schema, 4, 1)

		label_databasetype = QLabel('<font size="4"> Database Type: </font>')
		self.combo_databasetype = QComboBox()
		self.combo_databasetype.addItem("Oracle")
		self.combo_databasetype.addItem("MS SQL Server")
		layout.addWidget(label_databasetype, 5, 0)
		layout.addWidget(self.combo_databasetype, 5, 1)

		
		button_login = QPushButton('Login')
		button_login.clicked.connect(self.check_password)
		layout.addWidget(button_login, 6, 0,1,2)
		button_cancel = QPushButton('Cancel')
		button_cancel.clicked.connect(self.cancel_pressed)
		layout.addWidget(button_cancel, 7,0,1,2)

	
		layout.setRowMinimumHeight(1, 75)
		layout.setRowMinimumHeight(2, 75)
		layout.setRowMinimumHeight(3, 75)
		layout.setRowMinimumHeight(4, 75)
		layout.setRowMinimumHeight(5, 75)
		layout.setRowMinimumHeight(6, 75)

		self.setLayout(layout)
		self.clear_fields()		

		if self.my_login.user_name.strip():
			self.fill_dialog()
	
	def cancel_pressed(self):
		self.login_flag = False
		self.close()

	def clear_fields(self):
		self.lineEdit_username.clear()
		self.lineEdit_password.clear()
		self.combo_servername.clear()
		self.combo_databasename.clear()
		self.lineedit_schema.clear()
		
	def fill_dialog(self):

		self.lineEdit_username.insert(self.my_login.user_name)
		self.self.lineEdit_password.insert(self.my_login.password)
		self.combo_servername.addItem(self.my_login.server_name)
		self.combo_databasename.addItem(self.my_login.database_name)
		self.lineedit_schema.insert(self.my_login.schema)
		self.combo_databasetype.setCurrentIndex(self.my_login.database_type)


	def check_password(self):
		msg = QMessageBox()
		
		s1 = self.lineEdit_username.text()
		s2 = self.lineEdit_password.text()
		s3 = self.combo_servername.currentText()
		s4 = self.combo_databasename.currentText()
		s5 = self.lineedit_schema.text()
		s6 = self.combo_databasetype.currentIndex()

		if not s1.strip() :
			msg.setWindowTitle('User Name Error!')
			msg.setText('Please Enter a User Name')
			msg.exec()
		elif not s2.strip():
			msg.setWindowTitle('Password Error!')
			msg.setText('Please Enter a password')
			msg.exec()
		elif not s3.strip():
			msg.setWindowTitle('Server Name Error!')
			msg.setText('Please Enter a Server Name')
			msg.exec()
		elif not s4.strip():
			msg.setWindowTitle('Database Name Error!')
			msg.setText('Please Enter a Database Name')
			msg.exec()
		elif not s5.strip():
			msg.setWindowTitle('Schema Name Error!')
			msg.setText('Please Enter a Schema Name')
			msg.exec()
	
		else:

			self.my_login.user_name = s1.strip()
			self.my_login.user_password = s2.strip()
			self.my_login.server_name = s3.strip()
			self.my_login.database_name = s4.strip()
			self.my_login.schema = s5.strip()
			self.my_login.database_type = s6
			
			self.my_url = url_builder(self.my_login)
			if check_db_exists(self) == -1:
				msg.setWindowTitle('Problem with login data')
				msg.setText('Please check all Login Data!')
				msg.exec()
				
			else:			
				self.login_flag = True
				self.close()
			
		


if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = LoginForm()
	form.show()

	sys.exit(app.exec())
