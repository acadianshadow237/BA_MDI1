
import sys
import operator

from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QComboBox, QDialog, QTableWidget)
from PySide6 import QtCore
from PySide6 import QtGui
from PySide6.QtCore import (Signal, Slot)

from helpers.helpers1 import clearColorRow, setColorRow, extractData , extractHeaders
from Views.split_sections_ui import Ui_DialogSplitSections
from Views.tweak_sections_ui import Ui_DialogTweakSections
from Views.move_sections_ui import Ui_DialogMoveSections
from Views.copy_sections_ui import Ui_DialogCopySections
from Views.simple_edit_ui import Ui_DialogSimpleEdit

from Controllers.orm_select import county_select, route_select, direction_select, VAS_select
from Controllers.controller import simpleUpdate
from Models.login_model import login_stuff
from Models.tableModel import MyTableModel , tableCreate2, tableCreate3
from Models.my_tables_model import get_table_link
import sqlalchemy as sa



class splitSections(Ui_DialogSplitSections):
    def __init__(self,my_self):
        super(splitSections, self).__init__()
           
       
        self.mdiArea = my_self.mdiArea

        self.index = 0
        self.my_login = login_stuff()
        self.my_db_tables = my_self.my_db_tables
        self.my_url = my_self.my_url
        self.database_type = my_self.my_login.database_type
        self.my_session = my_self.my_session
        self.my_login = my_self.my_login
        self.setWindowFlag
        self.fileName = None

        self.my_VAS_Sql = None
        self.my_id = None
        self.my_name = None
        self.my_county = None
        self.my_route = None
        self.my_sri = None
        self.my_from = None
        self.my_to = None
        self.my_split = None
        self.my_pasid = None

        self.my_row = None
        self.my_column = None
       
        self.setupUi(self)
        
        self.textEditFrom.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.textEditTo.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.setup_county()        
       
        self.comboBoxCounty.currentIndexChanged.connect(self.county_change)
        self.comboBoxRoute.currentIndexChanged.connect(self.route_change)
        self.comboBoxDirection.currentIndexChanged.connect(self.direction_change)

        self.tableWidget.cellClicked.connect(self.selectRow)                    
        self.pushButtonReset.clicked.connect(self.reset_all)
        self.pushButtonSplit.clicked.connect(self.onSplit)
       

    def county_change(self):
        if self.comboBoxCounty.currentIndex == 0:
            self.comboBoxRoute.setCurrentIndex(0)
            self.comboBoxDirection.setCurrentIndex(0)
            self.FilterColumncheckBox.setChecked(False)
        else:
            self.FilterColumncheckBox.setChecked(True)
            self.comboBoxRoute.clear()
            self.comboBoxDirection.clear()
            self.setup_route()
            
        pass

    def route_change(self):
        if self.comboBoxRoute.currentIndex == 0:
            
            self.comboBoxDirection.clear()
            pass
        else:
            self.setup_direction()

    def direction_change(self):
        if self.comboBoxDirection.currentIndex == 0  :
           
            pass
        else:
            my_direction = self.comboBoxDirection.currentText()
            if my_direction.strip() == '':
                pass
            else:
                self.my_sri = my_direction[:my_direction.find(' ')]
                self.my_from = my_direction[my_direction.find(': ')+1 : my_direction.find('T') ]
                self.my_from = float(self.my_from.strip())
                self.my_to = my_direction[my_direction.find('To: ')+3:]
                self.my_to = float(self.my_to.strip())
               
                self.fill_tables()
     

        pass
    
    def reset_all(self):
        self.comboBoxCounty.setCurrentIndex(0)
        self.comboBoxRoute.setCurrentIndex(0)
        self.comboBoxDirection.setCurrentIndex(0)
        self.tableWidget.clearContents()
        self.textEditFrom.clear()
        self.textEditSplit.clear()
        self.textEditTo.clear()
       
        self.FilterColumncheckBox.setChecked(False)
       

    def setup_county(self):
        c1 = county_select(self)
        self.comboBoxCounty.addItems(c1.get_county())

    def setup_route(self):
        if self.comboBoxCounty.currentIndex == 0:
            
            self.comboBoxDirection.clear()
            pass
        else:
            rt1 = route_select(self)
            my_temp_list = rt1.get_route()
     
            for item in my_temp_list:
                self.comboBoxRoute.addItem(str(item))     
            self.setup_direction()
            pass       

    def setup_direction(self):
        my_list = []
        if self.comboBoxDirection.currentIndex == 0 :
            
            pass
        else:
            if self.comboBoxRoute.currentIndex != 0:
                db = self.my_db_tables.VBase
                tm_county = self.comboBoxCounty.currentText()
                tm_county = tm_county[tm_county.find('[')+1:tm_county.find(']')]
                tm_route = self.comboBoxRoute.currentText()
                stmt = sa.select(db.c.Name,db.c.From,db.c.To).filter(db.c.County == tm_county).filter(db.c.Route_ID == tm_route).order_by(db.c.Name,db.c.From)
                results = self.my_session.execute(stmt)
            
                my_list.clear()
                my_list.insert(0,'')
                for item in results:
                    if item is None:
                        pass
                    else:
                        my_str = item[0] + ' From: ' + str(item[1]) + ' To: ' + str(item[2])
                        my_list.append(my_str)

            self.comboBoxDirection.clear()        
            self.comboBoxDirection.addItems(my_list) 


    def fill_tables(self):

        if  self.my_VAS_Sql == None:
            my_item = ''  
            my_keys = [] 
            my_data = []
            my_temp = []
            my_vas = []
         
            db = self.my_db_tables.VAnalysis_Sections
                    
            stmt = sa.select(db.c.id,db.c.Name,db.c.RoadName,db.c.From,db.c.To,db.c.pvmt_analysis_section_id,db.c.Pavement_A,
db.c.FilterColumn).filter(db.c.RoadName == self.my_sri) 

            if self.FilterColumncheckBox.isChecked() == True:
                stmt = stmt.filter(db.c.FilterColumn == 1)
          
            results1 = self.my_session.execute(stmt)
            my_vas_keys = []
            
            for item in results1.keys():
                my_vas_keys.append(item)

            for item1 in results1:
                my_vas.append(item1)
 
            self.tableWidget.clearContents()
           
            
            tableCreate2(self.tableWidget,my_vas_keys, my_vas)
            
            
            self.tableWidget.viewport().update()
     
            
        else:
            pass
        

    def selectRow(self,row,column):
        self.my_row = row
        self.my_column = column
        clearColorRow(self.tableWidget,QtGui.QColor(255,255,255))
        setColorRow(self.tableWidget,row,QtGui.QColor(211,211,211))
        self.my_id = self.tableWidget.item(self.my_row,0).text()
        self.my_name = self.tableWidget.item(self.my_row,1).text()
        self.my_route = self.tableWidget.item(self.my_row,2).text()
        self.my_from = self.tableWidget.item(self.my_row,3).text()
        self.my_to = self.tableWidget.item(self.my_row,4).text()
        self.my_pasid = self.tableWidget.item(self.my_row,5).text()
        self.textEditFrom.setPlainText(self.tableWidget.item(self.my_row,3).text())
        self.textEditTo.setPlainText(self.tableWidget.item(self.my_row,4).text())

    def onSplit(self):
        print('Split Here')


class tweakSections(Ui_DialogTweakSections):
    def __init__(self,my_self):
        super(tweakSections, self).__init__()
           
       
        self.mdiArea = my_self.mdiArea

        self.index = 0
        self.my_login = login_stuff()
        self.my_db_tables = my_self.my_db_tables
        self.my_url = my_self.my_url
        self.database_type = my_self.my_login.database_type
        self.my_session = my_self.my_session
        self.my_login = my_self.my_login
        self.setWindowFlag
        self.fileName = None

        self.my_VAS_Sql = None
        self.my_id = None
        self.my_name = None
        self.my_county = None
        self.my_route = None
        self.my_sri = None
        self.my_from = None
        self.my_to = None
        self.my_split = None
        self.my_pasid = None

        self.my_row = None
        self.my_column = None
       
        self.setupUi(self)
        
        self.textEditFrom.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.textEditTo.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.setup_county()        
       
        self.comboBoxCounty.currentIndexChanged.connect(self.county_change)
        self.comboBoxRoute.currentIndexChanged.connect(self.route_change)
        self.comboBoxDirection.currentIndexChanged.connect(self.direction_change)

        self.tableWidget.cellClicked.connect(self.selectRow)                    
        self.pushButtonReset.clicked.connect(self.reset_all)
       
       

    def county_change(self):
        if self.comboBoxCounty.currentIndex == 0:
            self.comboBoxRoute.setCurrentIndex(0)
            self.comboBoxDirection.setCurrentIndex(0)
            self.FilterColumncheckBox.setChecked(False)
        else:
            self.FilterColumncheckBox.setChecked(True)
            self.comboBoxRoute.clear()
            self.comboBoxDirection.clear()
            self.setup_route()
            
        pass

    def route_change(self):
        if self.comboBoxRoute.currentIndex == 0:
            
            self.comboBoxDirection.clear()
            pass
        else:
            self.setup_direction()

    def direction_change(self):
        if self.comboBoxDirection.currentIndex == 0  :
           
            pass
        else:
            my_direction = self.comboBoxDirection.currentText()
            if my_direction.strip() == '':
                pass
            else:
                self.my_sri = my_direction[:my_direction.find(' ')]
                self.my_from = my_direction[my_direction.find(': ')+1 : my_direction.find('T') ]
                self.my_from = float(self.my_from.strip())
                self.my_to = my_direction[my_direction.find('To: ')+3:]
                self.my_to = float(self.my_to.strip())
               
                self.fill_tables()
     

        pass
    
    def reset_all(self):
        self.comboBoxCounty.setCurrentIndex(0)
        self.comboBoxRoute.setCurrentIndex(0)
        self.comboBoxDirection.setCurrentIndex(0)
        self.tableWidget.clearContents()
        self.textEditFrom.clear()
        self.textEditSplit.clear()
        self.textEditTo.clear()
       
        self.FilterColumncheckBox.setChecked(False)
       

    def setup_county(self):
        c1 = county_select(self)
        self.comboBoxCounty.addItems(c1.get_county())

    def setup_route(self):
        if self.comboBoxCounty.currentIndex == 0:
            
            self.comboBoxDirection.clear()
            pass
        else:
            rt1 = route_select(self)
            my_temp_list = rt1.get_route()
     
            for item in my_temp_list:
                self.comboBoxRoute.addItem(str(item))     
            self.setup_direction()
            pass       

    def setup_direction(self):
        my_list = []
        if self.comboBoxDirection.currentIndex == 0 :
            
            pass
        else:
            if self.comboBoxRoute.currentIndex != 0:
                db = self.my_db_tables.VBase
                tm_county = self.comboBoxCounty.currentText()
                tm_county = tm_county[tm_county.find('[')+1:tm_county.find(']')]
                tm_route = self.comboBoxRoute.currentText()
                stmt = sa.select(db.c.Name,db.c.From,db.c.To).filter(db.c.County == tm_county).filter(db.c.Route_ID == tm_route).order_by(db.c.Name,db.c.From)
                results = self.my_session.execute(stmt)
            
                my_list.clear()
                my_list.insert(0,'')
                for item in results:
                    if item is None:
                        pass
                    else:
                        my_str = item[0] + ' From: ' + str(item[1]) + ' To: ' + str(item[2])
                        my_list.append(my_str)

            self.comboBoxDirection.clear()        
            self.comboBoxDirection.addItems(my_list) 


    def fill_tables(self):

        if  self.my_VAS_Sql == None:
            my_item = ''  
            my_keys = [] 
            my_data = []
            my_temp = []
            my_vas = []
         
            db = self.my_db_tables.VAnalysis_Sections
                    
            stmt = sa.select(db.c.id,db.c.Name,db.c.RoadName,db.c.From,db.c.To,db.c.pvmt_analysis_section_id,db.c.Pavement_A,
db.c.FilterColumn).filter(db.c.RoadName == self.my_sri) 

            if self.FilterColumncheckBox.isChecked() == True:
                stmt = stmt.filter(db.c.FilterColumn == 1)
          
            results1 = self.my_session.execute(stmt)
            my_vas_keys = []
            
            for item in results1.keys():
                my_vas_keys.append(item)

            for item1 in results1:
                my_vas.append(item1)
 
            self.tableWidget.clearContents()
           
            
            tableCreate2(self.tableWidget,my_vas_keys, my_vas)
            
            
            self.tableWidget.viewport().update()
     
            
        else:
            pass
        

    def selectRow(self,row,column):
        self.my_row = row
        self.my_column = column
        clearColorRow(self.tableWidget,QtGui.QColor(255,255,255))
        setColorRow(self.tableWidget,row,QtGui.QColor(211,211,211))
        self.my_id = self.tableWidget.item(self.my_row,0).text()
        self.my_name = self.tableWidget.item(self.my_row,1).text()
        self.my_route = self.tableWidget.item(self.my_row,2).text()
        self.my_from = self.tableWidget.item(self.my_row,3).text()
        self.my_to = self.tableWidget.item(self.my_row,4).text()
        self.my_pasid = self.tableWidget.item(self.my_row,5).text()
        self.textEditFrom.setPlainText(self.tableWidget.item(self.my_row,3).text())
        self.textEditTo.setPlainText(self.tableWidget.item(self.my_row,4).text())


class moveSections(Ui_DialogMoveSections):
    def __init__(self,my_self):
        super(moveSections, self).__init__()
           
       
        self.mdiArea = my_self.mdiArea

        self.index = 0
        self.my_login = login_stuff()
        self.my_db_tables = my_self.my_db_tables
        self.my_url = my_self.my_url
        self.database_type = my_self.my_login.database_type
        self.my_session = my_self.my_session
        self.my_login = my_self.my_login
        self.setWindowFlag
        self.fileName = None

        self.my_VAS_Sql = None
        self.my_id = None
        self.my_name = None
        self.my_county = None
        self.my_route = None
        self.my_sri = None
        self.my_from = None
        self.my_to = None
        self.my_split = None
        self.my_pasid = None

        self.my_row = None
        self.my_column = None
       
        self.setupUi(self)
        
        self.textEditFrom.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.textEditTo.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.setup_county()        
       
        self.comboBoxCounty.currentIndexChanged.connect(self.county_change)
        self.comboBoxRoute.currentIndexChanged.connect(self.route_change)
        self.comboBoxDirection.currentIndexChanged.connect(self.direction_change)

        self.tableWidget.cellClicked.connect(self.selectRow)                    
        self.pushButtonReset.clicked.connect(self.reset_all)
       
       

    def county_change(self):
        if self.comboBoxCounty.currentIndex == 0:
            self.comboBoxRoute.setCurrentIndex(0)
            self.comboBoxDirection.setCurrentIndex(0)
            self.FilterColumncheckBox.setChecked(False)
        else:
            self.FilterColumncheckBox.setChecked(True)
            self.comboBoxRoute.clear()
            self.comboBoxDirection.clear()
            self.setup_route()
            
        pass

    def route_change(self):
        if self.comboBoxRoute.currentIndex == 0:
            
            self.comboBoxDirection.clear()
            pass
        else:
            self.setup_direction()

    def direction_change(self):
        if self.comboBoxDirection.currentIndex == 0  :
           
            pass
        else:
            my_direction = self.comboBoxDirection.currentText()
            if my_direction.strip() == '':
                pass
            else:
                self.my_sri = my_direction[:my_direction.find(' ')]
                self.my_from = my_direction[my_direction.find(': ')+1 : my_direction.find('T') ]
                self.my_from = float(self.my_from.strip())
                self.my_to = my_direction[my_direction.find('To: ')+3:]
                self.my_to = float(self.my_to.strip())
               
                self.fill_tables()
     

        pass
    
    def reset_all(self):
        self.comboBoxCounty.setCurrentIndex(0)
        self.comboBoxRoute.setCurrentIndex(0)
        self.comboBoxDirection.setCurrentIndex(0)
        self.tableWidget.clearContents()
        self.textEditFrom.clear()
        self.textEditSplit.clear()
        self.textEditTo.clear()
       
        self.FilterColumncheckBox.setChecked(False)
       

    def setup_county(self):
        c1 = county_select(self)
        self.comboBoxCounty.addItems(c1.get_county())

    def setup_route(self):
        if self.comboBoxCounty.currentIndex == 0:
            
            self.comboBoxDirection.clear()
            pass
        else:
            rt1 = route_select(self)
            my_temp_list = rt1.get_route()
     
            for item in my_temp_list:
                self.comboBoxRoute.addItem(str(item))     
            self.setup_direction()
            pass       

    def setup_direction(self):
        my_list = []
        if self.comboBoxDirection.currentIndex == 0 :
            
            pass
        else:
            if self.comboBoxRoute.currentIndex != 0:
                db = self.my_db_tables.VBase
                tm_county = self.comboBoxCounty.currentText()
                tm_county = tm_county[tm_county.find('[')+1:tm_county.find(']')]
                tm_route = self.comboBoxRoute.currentText()
                stmt = sa.select(db.c.Name,db.c.From,db.c.To).filter(db.c.County == tm_county).filter(db.c.Route_ID == tm_route).order_by(db.c.Name,db.c.From)
                results = self.my_session.execute(stmt)
            
                my_list.clear()
                my_list.insert(0,'')
                for item in results:
                    if item is None:
                        pass
                    else:
                        my_str = item[0] + ' From: ' + str(item[1]) + ' To: ' + str(item[2])
                        my_list.append(my_str)

            self.comboBoxDirection.clear()        
            self.comboBoxDirection.addItems(my_list) 


    def fill_tables(self):

        if  self.my_VAS_Sql == None:
            my_item = ''  
            my_keys = [] 
            my_data = []
            my_temp = []
            my_vas = []
         
            db = self.my_db_tables.VAnalysis_Sections
                    
            stmt = sa.select(db.c.id,db.c.Name,db.c.RoadName,db.c.From,db.c.To,db.c.pvmt_analysis_section_id,db.c.Pavement_A,
db.c.FilterColumn).filter(db.c.RoadName == self.my_sri) 

            if self.FilterColumncheckBox.isChecked() == True:
                stmt = stmt.filter(db.c.FilterColumn == 1)
          
            results1 = self.my_session.execute(stmt)
            my_vas_keys = []
            
            for item in results1.keys():
                my_vas_keys.append(item)

            for item1 in results1:
                my_vas.append(item1)
 
            self.tableWidget.clearContents()
           
            
            tableCreate2(self.tableWidget,my_vas_keys, my_vas)
            
            
            self.tableWidget.viewport().update()
     
            
        else:
            pass
        

    def selectRow(self,row,column):
        self.my_row = row
        self.my_column = column
        clearColorRow(self.tableWidget,QtGui.QColor(255,255,255))
        setColorRow(self.tableWidget,row,QtGui.QColor(211,211,211))
        self.my_id = self.tableWidget.item(self.my_row,0).text()
        self.my_name = self.tableWidget.item(self.my_row,1).text()
        self.my_route = self.tableWidget.item(self.my_row,2).text()
        self.my_from = self.tableWidget.item(self.my_row,3).text()
        self.my_to = self.tableWidget.item(self.my_row,4).text()
        self.my_pasid = self.tableWidget.item(self.my_row,5).text()
        self.textEditFrom.setPlainText(self.tableWidget.item(self.my_row,3).text())
        self.textEditTo.setPlainText(self.tableWidget.item(self.my_row,4).text())


class copySections(Ui_DialogCopySections):
    def __init__(self,my_self):
        super(copySections, self).__init__()
           
       
        self.mdiArea = my_self.mdiArea

        self.index = 0
        self.my_login = login_stuff()
        self.my_db_tables = my_self.my_db_tables
        self.my_url = my_self.my_url
        self.database_type = my_self.my_login.database_type
        self.my_session = my_self.my_session
        self.my_login = my_self.my_login
        self.setWindowFlag
        self.fileName = None

        self.my_VAS_Sql = None
        self.my_id = None
        self.my_name = None
        self.my_county = None
        self.my_route = None
        self.my_sri = None
        self.my_from = None
        self.my_to = None
        self.my_split = None
        self.my_pasid = None

        self.my_row = None
        self.my_column = None
       
        self.setupUi(self)
        
        self.textEditFrom.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.textEditTo.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.setup_county()        
       
        self.comboBoxCounty.currentIndexChanged.connect(self.county_change)
        self.comboBoxRoute.currentIndexChanged.connect(self.route_change)
        self.comboBoxDirection.currentIndexChanged.connect(self.direction_change)

        self.tableWidget.cellClicked.connect(self.selectRow)                    
        self.pushButtonReset.clicked.connect(self.reset_all)
       
       

    def county_change(self):
        if self.comboBoxCounty.currentIndex == 0:
            self.comboBoxRoute.setCurrentIndex(0)
            self.comboBoxDirection.setCurrentIndex(0)
            self.FilterColumncheckBox.setChecked(False)
        else:
            self.FilterColumncheckBox.setChecked(True)
            self.comboBoxRoute.clear()
            self.comboBoxDirection.clear()
            self.setup_route()
            
        pass

    def route_change(self):
        if self.comboBoxRoute.currentIndex == 0:
            
            self.comboBoxDirection.clear()
            pass
        else:
            self.setup_direction()

    def direction_change(self):
        if self.comboBoxDirection.currentIndex == 0  :
           
            pass
        else:
            my_direction = self.comboBoxDirection.currentText()
            if my_direction.strip() == '':
                pass
            else:
                self.my_sri = my_direction[:my_direction.find(' ')]
                self.my_from = my_direction[my_direction.find(': ')+1 : my_direction.find('T') ]
                self.my_from = float(self.my_from.strip())
                self.my_to = my_direction[my_direction.find('To: ')+3:]
                self.my_to = float(self.my_to.strip())
               
                self.fill_tables()
     

        pass
    
    def reset_all(self):
        self.comboBoxCounty.setCurrentIndex(0)
        self.comboBoxRoute.setCurrentIndex(0)
        self.comboBoxDirection.setCurrentIndex(0)
        self.tableWidget.clearContents()
        self.textEditFrom.clear()
        self.textEditSplit.clear()
        self.textEditTo.clear()
       
        self.FilterColumncheckBox.setChecked(False)
       

    def setup_county(self):
        c1 = county_select(self)
        self.comboBoxCounty.addItems(c1.get_county())

    def setup_route(self):
        if self.comboBoxCounty.currentIndex == 0:
            
            self.comboBoxDirection.clear()
            pass
        else:
            rt1 = route_select(self)
            my_temp_list = rt1.get_route()
     
            for item in my_temp_list:
                self.comboBoxRoute.addItem(str(item))     
            self.setup_direction()
            pass       

    def setup_direction(self):
        my_list = []
        if self.comboBoxDirection.currentIndex == 0 :
            
            pass
        else:
            if self.comboBoxRoute.currentIndex != 0:
                db = self.my_db_tables.VBase
                tm_county = self.comboBoxCounty.currentText()
                tm_county = tm_county[tm_county.find('[')+1:tm_county.find(']')]
                tm_route = self.comboBoxRoute.currentText()
                stmt = sa.select(db.c.Name,db.c.From,db.c.To).filter(db.c.County == tm_county).filter(db.c.Route_ID == tm_route).order_by(db.c.Name,db.c.From)
                results = self.my_session.execute(stmt)
            
                my_list.clear()
                my_list.insert(0,'')
                for item in results:
                    if item is None:
                        pass
                    else:
                        my_str = item[0] + ' From: ' + str(item[1]) + ' To: ' + str(item[2])
                        my_list.append(my_str)

            self.comboBoxDirection.clear()        
            self.comboBoxDirection.addItems(my_list) 


    def fill_tables(self):

        if  self.my_VAS_Sql == None:
            my_item = ''  
            my_keys = [] 
            my_data = []
            my_temp = []
            my_vas = []
         
            db = self.my_db_tables.VAnalysis_Sections
                    
            stmt = sa.select(db.c.id,db.c.Name,db.c.RoadName,db.c.From,db.c.To,db.c.pvmt_analysis_section_id,db.c.Pavement_A,
db.c.FilterColumn).filter(db.c.RoadName == self.my_sri) 

            if self.FilterColumncheckBox.isChecked() == True:
                stmt = stmt.filter(db.c.FilterColumn == 1)
          
            results1 = self.my_session.execute(stmt)
            my_vas_keys = []
            
            for item in results1.keys():
                my_vas_keys.append(item)

            for item1 in results1:
                my_vas.append(item1)
 
            self.tableWidget.clearContents()
           
            
            tableCreate2(self.tableWidget,my_vas_keys, my_vas)
            
            
            self.tableWidget.viewport().update()
     
            
        else:
            pass
        

    def selectRow(self,row,column):
        self.my_row = row
        self.my_column = column
        clearColorRow(self.tableWidget,QtGui.QColor(255,255,255))
        setColorRow(self.tableWidget,row,QtGui.QColor(211,211,211))
        self.my_id = self.tableWidget.item(self.my_row,0).text()
        self.my_name = self.tableWidget.item(self.my_row,1).text()
        self.my_route = self.tableWidget.item(self.my_row,2).text()
        self.my_from = self.tableWidget.item(self.my_row,3).text()
        self.my_to = self.tableWidget.item(self.my_row,4).text()
        self.my_pasid = self.tableWidget.item(self.my_row,5).text()
        self.textEditFrom.setPlainText(self.tableWidget.item(self.my_row,3).text())
        self.textEditTo.setPlainText(self.tableWidget.item(self.my_row,4).text())

#class ItemChanged(QObject):
#    ''' Represents a punching bag; when you punch it, it
#        emits a signal that indicates that it was punched. '''
#    itemchanged = Signal()
 
#    def __init__(self):
#        # Initialize the PunchingBag as a QObject
#        QObject.__init__(self)
 
#    def itemChange(self):
#        ''' Punch the bag '''
#        self.itemchanged.emit()

class simpleEdits(Ui_DialogSimpleEdit):
    
    def __init__(self,ID,fieldName,fieldCurrentValue,tableName,url):
        super(simpleEdits, self).__init__()
        self.setupUi(self)

        self.url = url
        self.ID = ID
        self.fieldName = fieldName
        self.fieldCurrentValue = fieldCurrentValue
        self.tableName = tableName
        self.pushButtonSave.clicked.connect(self.onSave)
        self.lineEditFieldName.setText(self.fieldName)
        self.lineEditFieldCurrentValue.setText(self.fieldCurrentValue)

        self.load_table()

    def onSave(self):
        newValue = self.lineEditFieldNewValue.text()
        if newValue == None:
            return
        else:    
            simpleUpdate(self.ID,self.fieldName,newValue,self.tableName)
        pass

    def load_table(self):
        
        lutype,luval = get_table_link(self.url,self.tableName,self.fieldName)

        pass

    



    
        
            

