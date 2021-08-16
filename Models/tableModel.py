

from datetime import datetime,date
from PySide6 import QtCore
from PySide6 import QtWidgets
                
class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header

    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        return len(self.mylist[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]
        return None

    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))

        try:
            self.mylist = sorted(self.mylist, key=operator.itemgetter(col))
        except:
            pass
        if order == QtCore.Qt.DescendingOrder:
            self.mylist.reverse()
        self.emit(QtCore.SIGNAL("layoutChanged()"))


class TableCreate(QtWidgets.QTableWidget):
    def __init__(self,header,data, *args):
        QtWidgets.QTableWidget.__init__(self,*args)
        self.header = header
        self.data = data
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setData()
        self.my_type = None

    def setData(self):
        horHeaders = []
        hidehorheaders = ['ElementID','ID','NetworkID','Lane','Historic','Order','Length','FromMeasure','ToMeasure','FromElement','FromOffset','ToElement','ToOffset' \
        ,'SRI','SRI_From','SRI_To','create_date','create_user','pvmt_proj_nmbr_detail','update_date','update_user','Map']
       
        for n, key in enumerate(self.header):
            horHeaders.append(key)
        
        for m,item in enumerate(self.data):
            for i, key in enumerate(item): 
              
                if isinstance(key, datetime) == True :
                    key = datetime.strftime(key,"%d-%b-%Y (%H:%M:%S)")
                newitem = QtWidgets.QTableWidgetItem(key)
                self.setItem(m,i, newitem)

        self.setHorizontalHeaderLabels(horHeaders)
        
class LOGDATA(object):
    def _init_(self):
        self.PVMT_TXT_ID = ''
        self.PVMT_TXT_ACTION_CODE = ''
        self.COUNTY_NMBR = 0
        self.NEW_COUNTY_NMBR = 0
        self.ROUTE_ID =  ''
        self.NEW_ROUTE_ID = ''
        self.SRI = ''
        self.NEW_SRI = ''
        self.FST_MP_START = 9999.999999
        self.FST_NEW_MP_START = 9999.999999
        self.FST_MP_END = 9999.999999
        self.FST_NEW_MP_END = 9999.999999
        self.FST_PASID = -10000
        self.SND_PASID = -10000
        self.CREATE_DATE = date.today()
        self.CREATE_USER = ''
        self.UPDATE_DATE = date.today()
        self.UPDATE_USER = ''
        self.SND_MP_START = 9999.999999
        self.SND_NEW_MP_START = 9999.999999
        self.SND_MP_END = 9999.999999
        self.SND_NEW_MP_END = 9999.999999
        self.FIELDNAME = ''
        self.FIELDVALUE = ''
        self.FIELDNEWVALUE = ''
        
    pass


def tableCreate2(my_table,my_header,my_data):
    horHeaders = []
    hideheader = ['ElementID','ID','id','NetworkID','Lane','Historic','Order','Length','FromMeasure','ToMeasure','FromElement','FromOffset','ToElement','ToOffset' \
    ,'sri','SRI_From','SRI_To','pvmt_proj_nmbr_detail','update_date','update_user','Map','RFrom','RTo','Offset','End','ValidOn','ValidTo','EndOn','ChunkId','DeleteRole' \
    ,'DTIMSGEO','SelectRole','UpdateRole','zz_Deighton_Fix','CreateOn','skid_test_id','skid_test_section_ind','pvmt_proj_mix_design_nmbr'] 

    hideheaders2 = []

    for item in hideheader:
        hideheaders2.append(item.strip())  
    

    my_table.setRowCount(len(my_data))
   
    
    for n, key in enumerate(my_header):
        key = key.strip('\n')
        horHeaders.append(key)
     
    my_table.setColumnCount(len(horHeaders))
    my_table.setHorizontalHeaderLabels(horHeaders)

    #my_table.HorizontalHeaderLabels.font().setPointSize(12)
   

    for m,item in enumerate(my_data):
        for i, key in enumerate(item): 
            if isinstance(key, datetime) == True :
                key = datetime.strftime(key,"%d-%b-%Y (%H:%M:%S)")
            else:
                if key is None:
                    key = ''
                key = str(key)
                          
            
            newitem = QtWidgets.QTableWidgetItem(key)
            newitem.setFlags(QtCore.Qt.ItemIsEditable)
            my_table.setItem(m,i, newitem)

    columnCount = my_table.columnCount()
    for i in range(columnCount):
        my_header = my_table.horizontalHeaderItem(i).text();

        if my_header.strip() in  hideheaders2:
            my_table.setColumnHidden(0,True)  

    header = my_table.horizontalHeader()
    header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
    
    

def tableCreate3(my_table,my_header,my_fields,my_data):
    horHeaders = []
    hideheader = ['ElementID','ID','id','Name','RoadName','From','To','pvmt_analysis_section_id','NetworkID','Lane','Historic','Order','Length','FromMeasure','ToMeasure','FromElement','FromOffset','ToElement','ToOffset' \
    'create_date','create_user','update_date','update_user','Map','RFrom','RTo','Offset','End','ValidOn','ValidTo','EndOn','ChunkId','DeleteRole' \
    ,'DTIMSGEO','SelectRole','UpdateRole','zz_Deighton_Fix','CreateOn',] 

    hideheaders2 = []

    hideheader3 = ['ID','id','Name','RoadName','From','To','pvmt_analysis_section_id','FilterColumn']


    for item in hideheader:
        hideheaders2.append(item.strip())  
  
    my_table.setRowCount(len(my_data))
    my_table.setColumnCount(len(my_header))
   
    
    for n, key in enumerate(my_header):
        key = key.strip('\n')
        horHeaders.append(key)
     
    my_table.setColumnCount(len(horHeaders))
    my_table.setHorizontalHeaderLabels(horHeaders)

    for m,key in enumerate(my_data):
        if isinstance(key, datetime) == True :
            key = datetime.strftime(key,"%d-%b-%Y (%H:%M:%S)")
        else:
            if key is None:
                key = ''
            key = str(key)
                          
            
        newitem = QtWidgets.QTableWidgetItem(key)
        newitem.setFlags(QtCore.Qt.ItemIsEditable)
        my_table.setItem(m,1, newitem)

    for i, item in enumerate(my_fields):
        newitem2 = QtWidgets.QTableWidgetItem(item.strip())
        newitem2.setFlags(QtCore.Qt.ItemIsEditable)
       
        my_table.setItem(i,0, newitem2)
        ##my_table.item(i,0).setBackgroundColor(QtGui.QColor(211,211,211))
        
    columnCount = my_table.columnCount()
   
    for i in range(columnCount):
        my_header = my_table.horizontalHeaderItem(i).text();

        if my_header.strip() in  hideheaders2:
            my_table.setColumnHidden(0,True)  

    header = my_table.horizontalHeader()
    header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
   
    
        