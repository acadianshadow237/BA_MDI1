


from Models.my_tables_model import get_table_county, get_table_route, get_table_direction, get_table_VAS,get_table_analysis_sections
from Controllers.controller import connectToDatabase
from sqlalchemy import select
import sqlalchemy as sa

from helpers.helpers1 import db_tables 
from Models.my_tables_model import gather_tables
from Models.login_model import login_stuff, url_builder

my_url = f'oracle+cx_oracle://USER_MISS:password@ORACLEDEV01:1521/GISDEV'
debug_session = False

class county_select():
    def __init__(self,my_self = None):
        if debug_session == True:
            self.my_url = my_url
            self.my_db_tables = db_tables  
            self.my_session = connectToDatabase(self.my_url)
            self.my_login = login_stuff()
            self.my_login.database_type = 0
            gather_tables(self)
            

        else:
            self.my_url = my_self.my_url
            self.my_login = my_self.my_login
            self.my_login.database_type = my_self.database_type
            self.my_db_tables = my_self.my_db_tables
            self.my_session = my_self.my_session
            
                   
    def get_county(self):
              
        my_list = [''] 
        db = self.my_db_tables.VCounty
            #results = self.session.query(self.VCounty).filter_by(id=1)
            #results = self.session.query(self.VCounty).all()
        stmt = select(db.c.county_name).order_by(db.c.county_name)
        results = self.my_session.execute(stmt)
        for item in results.scalars():
            #print(item)
            my_list.append(item)
            pass
           
        return my_list
  

class route_select():
    def __init__(self,my_self = None):
       
        if debug_session == True:
            self.my_url = my_url
            self.my_county = '1'
            self.my_db_tables = db_tables
            self.my_login = login_stuff()
            self.my_login.database_type = 0
            self.my_session = connectToDatabase(self.my_url)
            gather_tables(self)
        else:
            self.my_url = my_self.my_url
            self.my_login = login_stuff()
            self.my_login.database_type = 0
            self.my_county = my_self.comboBoxCounty.currentText()
            self.my_county = self.my_county[self.my_county.find('[')+1:self.my_county.find(']')]
            self.my_db_tables = my_self.my_db_tables
            self.my_session = my_self.my_session
       

    def get_route(self):
       
        my_list = [''] 
        my_list2 = []
        db = self.my_db_tables.VBase
       
            #results = self.session.query(self.VBase).filter_by(id=1)
            #results = self.session.query(self.VCounty).all()
        stmt = select(db.c.Route_ID).where(db.c.County == self.my_county).order_by(db.c.Route_ID)
        results = self.my_session.execute(stmt)
        for item in results.scalars():
            if item is None:
                pass
            else:
                #print(item)
                my_list2.append(item)
            pass

        my_list2 = (sorted(set(my_list2), reverse=False))
        #print(my_list2)
        for item in my_list2:
            my_list.append(item) 
            #print(my_list)
            
        return my_list
        

class direction_select():
    def __init__(self, my_self = None):     

        if debug_session == True:
            self.my_url = my_url
            self.my_db_tables = db_tables
            self.my_login = login_stuff()
            self.my_login.database_type = 0
            self.my_session = connectToDatabase(self.my_url)
            gather_tables(self)
            self.my_county = '1'
            self.my_route =  '61'
            self.my_road_name = '01_0061P1'
            
        else:
            self.url = my_self.my_url
            self.database_type = my_self.database_type
            self.my_county = my_self.comboBoxCounty.currentText()
            self.my_county = self.my_county[self.my_county.find('[')+1:self.my_county.find(']')]
            self.my_route =  my_self.comboBoxRoute.currentText()
            self.my_road_name = self.my_road_name[0:self.my_road_name.find('')]
            self.my_db_tables = my_self.my_db_tables
            self.my_session = my_self.my_session
            pass

    def get_direction(self):

       
        my_list = [] 
        my_list2 = []
        #self.database_type = 0
        db = self.my_db_tables.VAnalysis_Sections
        #results = self.my_session.query(db).filter_by(id=1)
            #results = self.session.query(self.VCounty).all()
           
        stmt = select(db.c.RoadName,db.c.From,db.c.To).order_by(db.c.RoadName,db.c.From).filter(db.c.RoadName == self.my_road_name)
        results = self.my_session.execute(stmt)
        for item in results:
            
            if item is None:
                pass
            else:
                
                my_line = item.RoadName + '  From : '+ str(item.From)+ ' To : '+ str(item.To)
                
                if my_line == None:
                    pass
                else:
                    my_list.append(my_line)
                    pass
                pass

            my_list = (sorted(set(my_list), reverse=False))
            #print(my_list2)
            #for item in my_list2:
            #    my_list.append(item) 
            ##print(my_list)
            
            return my_list
      

class VAS_select():
    def __init__(self,my_self = None):
        if debug_session == True:
            self.my_url = my_url
            self.my_db_tables = db_tables
            self.my_login = login_stuff()
            self.my_login.database_type = 0
            
            gather_tables(self)
            #self.my_session = connectToDatabase(self.my_url)
            self.my_county = '1'
            self.my_route =  '61'
            self.my_road_name = '01_0061P1'

            
        else:
            self.my_url = my_self.my_url
            self.database_type = my_self.database_type
            self.my_county = my_self.my_county
            self.my_route =  my_self.my_route
            self.my_road_name = my_self.my_sri
            self.my_session = my_self.my_session
            self.my_db_tables = my_self.my_db_tables
            pass
        
    def get_VAS(self):
        
        my_list = [] 
        my_as_list = []
        my_ds_list = []
        my_dd_list = []       
        my_remove_list = []
   
        db = self.my_db_tables.VAnalysis_Sections
        #db_Name = 'VAnalysis_Sections'

       

        for item in db.c:
            my_item = str(item)
            my_item2 = my_item[my_item2.find('.')+1:]   
            my_list.append(my_item2)
            pass
     
        for item2 in my_list:
            tag = item2[:3]

            ## print(tag,item2)
            #if tag == 'ds_':
            #    my_ds_list.append(item2)
            #elif tag == 'dd_':
            #    my_dd_list.append(item2)
            #else:
            my_as_list.append(item2)
            pass

        my_as_list = set(my_as_list)
        #my_as_list = columns_to_replace(my_as_list)  
        
        #my_ds_list = set(my_ds_list)
        #my_ds_list = columns_to_replace(my_ds_list)
        
        #my_dd_list = set(my_dd_list)
        #my_dd_list = columns_to_replace(my_dd_list)
       
        #my_as_select = db_query_columns(my_as_list,db_Name)
        #my_ds_select = db_query_columns(my_ds_list,db_Name)
        #my_dd_select = db_query_columns(my_dd_list,db_Name)

        return my_as_list  #,my_as_select, my_ds_list,my_ds_select, my_dd_list,my_dd_select

class VBase_Select():
    def __init__(self,my_self = None):
        if debug_session == True:
            self.my_url = my_url
            self.my_db_tables = db_tables  
            self.my_session = connectToDatabase(self.my_url)
            self.my_login = login_stuff()
            self.my_login.database_type = 0
            gather_tables(self)
            
        else:
            self.my_url = my_self.my_url
            self.my_login = my_self.my_login
            self.my_login.database_type = my_self.database_type
            self.my_db_tables = my_self.my_db_tables
            self.my_session = my_self.my_session
                   
    def get_VBase(self):
              
        my_list = [''] 
        db = self.my_db_tables.VBase
            #results = self.session.query(self.VCounty).filter_by(id=1)
            #results = self.session.query(self.VCounty).all()
        stmt = select(db.c.Name).order_by(db.c.Name).where(db.c.Name)
        results = self.my_session.execute(stmt)
        for item in results.scalars():
            #print(item)
            my_list.append(item)
            pass
           
        return my_list
    pass

def columns_to_hide():
    column_names = ['Attribute51'
                    ,'Default_Double'
                    ,'Default_Integer'
                    ,'ElementID'
                    ,'FilterColumn'
                    ,'FromElement'
                    ,'FromMeasure'
                    ,'FromOffset'
                    ,'Historic'
                    ,'ID'
                    ,'id'
                    ,'NetworkID'
                    ,'Order'
                    ,'ToElement'
                    ,'ToMeasure'
                    ,'ToOffset'
                    ,'mapid'
                    ,'mslink'
                    ,'zDensityAttribute'
                    ,'zz_Deighton_Fix'
                    ,'Map'
                    ,'Geo']
    return column_names
    pass



def columns_to_replace(my_list):
   

    temp_list1 = ['ID','id','Name','RoadName','From','To']
    #print(temp_list1)
    temp_list2 = my_list
    #print(temp_list1)
    i=0

    if 'ID' in temp_list2:
        temp_list2.remove('ID')
        pass
    else:
        temp_list1.remove('ID')
        pass
             
   
    if 'id' in temp_list2:
        temp_list2.remove('id')
        pass
    else:    
        temp_list1.remove('id')
        pass       
    
    if 'Name' in temp_list2:
        temp_list2.remove('Name')
        pass
    else:
        temp_list1.remove('Name')
        pass      

    if 'RoadName' in temp_list2:
        temp_list2.remove('RoadName')
        pass
    else:
        temp_list1.remove('RoadName')
        pass         
    
    if 'From' in temp_list2:
        temp_list2.remove('From')
        pass
    else:
        temp_list1.remove('From')
        pass           
    
    if 'To' in temp_list2:
        temp_list2.remove('To')
        pass
    else:
        temp_list1.remove('To')
        pass           
    
    temp_list2 = sorted(temp_list2)

    for item in temp_list2:
        temp_list1.append(item)

    return temp_list1
    pass

def db_query_columns(my_list, my_db):
    temp_string = ''
    i=0
    for item in my_list:
        if i==0:
            temp_string = my_db +'.'+'c'+'.'+ item
            i=i+1 
        else:
            temp_string = temp_string+','+my_db +'.c.'+item
    return temp_string



def main():

   
    my_data = VAS_select()
    a1 = my_data.get_VAS()    
    for item in a1:
        print(item)
   
    


if __name__ == '__main__':
    main()