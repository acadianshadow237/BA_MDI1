import sys
import operator
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QComboBox, QDialog)
from PySide6 import QtCore
from Views.VAS_view_ui import Ui_VAS_Form
from Views.VCRH_view_ui import Ui_VCRH_Form
from Controllers.orm_select import county_select, route_select, direction_select, VAS_select
from Models.login_model import login_stuff
from Models.tableModel import MyTableModel , tableCreate2
import sqlalchemy as sa



class VAS_view(Ui_VAS_Form):
    def __init__(self,my_self):
        super(VAS_view, self).__init__()
           
        #self.fileName = 'VAS'
        self.index = 0
        self.my_login = login_stuff()
        self.my_db_tables = my_self.my_db_tables
        self.my_url = my_self.my_url
        self.database_type = my_self.my_login.database_type
        self.my_session = my_self.my_session
        self.my_login = my_self.my_login
        self.setWindowFlag

        self.my_VAS_Sql = None
        self.my_VAS_DS_Sql = None
        self.my_VAS_DD_Sql = None
        self.my_VAS_Theaders = None
        self.my_VAS_DS_Theaders = None
        self.my_VAS_DD_Theaders = None

        self.my_county = None
        self.my_route = None
        self.my_sri = None
        self.my_from = None
        self.my_to = None

        self.setupUi(self)

        self.setup_county()        

       
        self.comboBoxCounty.currentIndexChanged.connect(self.county_change)
        self.comboBoxRoute.currentIndexChanged.connect(self.route_change)
        self.comboBoxDirection.currentIndexChanged.connect(self.direction_change)
      
        self.pushButtonReset.clicked.connect(self.reset_all)
        
        self.VAS_tab.setFocus()
    
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
        self.VAS_tableWidget.clearContents()
        self.VAS_DS_tableWidget.clearContents()
        self.VAS_DS_tableWidget.clearContents()
        self.FilterColumncheckBox.setChecked(False)
       

    def setup_county(self):
        my_list = [''] 
        db = self.my_db_tables.VCounty
        stmt = select(db.c.county_name).order_by(db.c.county_name)
        results = self.my_session.query(stmt)
        for item in results.scalars():
            #print(item)
            my_list.append(item)
            pass
        
        self.comboBoxCounty.addItems(my_list)


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
            self.my_VAS_Sql = None
            self.my_VAS_DS_Sql = None
            self.my_VAS_DD_Sql = None
            self.my_VAS_Theaders = None
            self.my_VAS_DS_Theaders = None
            self.my_VAS_DD_Theaders = None

            my_item = ''  
            my_vas_keys = [] 
            my_ds_keys = []
            my_dd_keys = []
            my_data = []
            my_temp = []
            my_vas_data = []
            my_ds_data = []
            my_dd_data = []
  

        
  
            db = self.my_db_tables.VAnalysis_Sections
            
 
           
            stmt = sa.select(db.c.id,db.c.Name,db.c.RoadName,db.c.From,db.c.To,db.c.pvmt_analysis_section_id,db.c.Pavement_A,
db.c.FilterColumn,db.c.maint_dis_nmbr,db.c.FunctionClass,db.c.dd_avg_fault_depth_qty,db.c.dd_avg_iri_qty,
db.c.dd_avg_rut_depth,db.c.dd_distress_rating_nmbr,db.c.dd_faults_qty,db.c.dd_pvmt_condition_rating_nmbr,
db.c.dd_pvmt_section_survey_year,db.c.dd_roughness_rating_nmbr,db.c.data_accum_direction,db.c.dd_data_orientation,
db.c.pvmt_condition_rating_nmbr,db.c.pvmt_type_code,db.c.pvmt_type_desc,db.c.left_shoulder_width_code,
db.c.left_shoulder_width_desc,db.c.right_shoulder_width_code,db.c.right_shoulder_width_desc,
db.c.road_type,db.c.route_id,db.c.pvmt_structure_nmbr,db.c.pvmt_type_code_clustering,db.c.section_lane_cnt,
db.c.section_total_lanes,db.c.survey_avg_lane_width,db.c.total_roadway_width_code,
db.c.total_roadway_width_desc,db.c.county_name,db.c.county_nmbr,db.c.create_date,db.c.create_user,
db.c.update_date,db.c.update_user,db.c.divided_hwy_ind,db.c.Budget_Category_Override,db.c.com_cost,
db.c.com_trt,db.c.com_year,db.c.Comments,db.c.eold,db.c.esal,db.c.RD_Name,db.c.RT_Class,db.c.Reversed,
db.c.sri,db.c.SRI_From,db.c.SRI_To,db.c.Segment,db.c.Segment_Length,db.c.Trt_Family,db.c.Year,db.c.anl_chip_seal,
db.c.anl_rural,db.c.anlss_sctn_annual_flex_esal,db.c.anlss_sctn_annual_rigid_esal,db.c.anlss_sctn_cumul_flex_esal,
db.c.anlss_sctn_cumul_rigid_esal,db.c.begin_english_station_nmbr,db.c.begin_landmark_desc,db.c.begin_lat,db.c.begin_long,
db.c.dFragWithSkip_Cluster,db.c.design_lane_width,db.c.document_id,db.c.end_english_station_nmbr,db.c.end_landmark_desc,
db.c.end_lat,db.c.end_long,db.c.esal_aadt,db.c.esal_flexible_annual,db.c.esal_kip_factor,db.c.esal_pct_trucks,
db.c.esal_rigid_annual,db.c.full_annual_flexible_esal,db.c.full_annual_rigid_esal,db.c.full_cumulative_flexible_esal,
db.c.full_cumulative_rigid_esal,db.c.max_design_hourly_vol,db.c.max_design_hourly_vol_year,
db.c.max_trffc_growth_rate,db.c.max_trffc_section_aadt,db.c.max_trffc_section_aadt_year,
db.c.max_truck_trffc_pct,db.c.measured_section_length,db.c.paved_shoulder_ind,db.c.ph_pvmt_proj_actl_end_date,
db.c.ph_pvmt_rehab_affctd_srfc_pct,db.c.ph_rehab_thickness,db.c.ph_rehab_type_code,db.c.ph_resurfacing_type_code,
db.c.plan_section_length,db.c.pvmt_analysis_section_id_,db.c.pvmt_anlyss_sctn_nhs_ind,db.c.pvmt_mdfd_structure_nmbr,db.c.pvmt_memo,
db.c.pvmt_pre_type_code,db.c.traffic_esal_base_year,db.c.weight
).filter(db.c.RoadName == self.my_sri) 

            if self.FilterColumncheckBox.isChecked() == True:
                stmt = stmt.filter(db.c.FilterColumn == 1)
          
            results1 = self.my_session.execute(stmt)
            
            for item1 in results1.keys():
                my_vas_keys.append(item1)
              
            for item1 in results1:
                my_vas_data.append(item1)



            stmt = sa.select(db.c.id,db.c.Name,db.c.RoadName,db.c.From,db.c.To,db.c.pvmt_analysis_section_id
    ,db.c.ds_Alligator_Cracking_0,db.c.ds_Alligator_Cracking_1,db.c.ds_Alligator_Cracking_2,db.c.ds_Bleeding_0
    ,db.c.ds_Bleeding_1	,db.c.ds_Bleeding_2	,db.c.ds_Block_Cracking_0	,db.c.ds_Block_Cracking_1
    ,db.c.ds_Block_Cracking_2	,db.c.ds_Blowup_0	,db.c.ds_Blowup_1	,db.c.ds_Blowup_2	,db.c.ds_Corner_Break_0
    ,db.c.ds_Corner_Break_1	,db.c.ds_Corner_Break_2	,db.c.ds_D_Cracking_0	,db.c.ds_D_Cracking_1	,db.c.ds_D_Cracking_2
    ,db.c.ds_Edge_Cracking_0	,db.c.ds_Edge_Cracking_1	,db.c.ds_Edge_Cracking_2	,db.c.ds_Faulting_0
    ,db.c.ds_Faulting_1	,db.c.ds_Faulting_2	,db.c.ds_IRI_0	,db.c.ds_IRI_1	,db.c.ds_IRI_2	,db.c.ds_Joint_Count_0
    ,db.c.ds_Joint_Count_1	,db.c.ds_Joint_Count_2	,db.c.ds_Joint_Deterioration_0	,db.c.ds_Joint_Deterioration_1
    ,db.c.ds_Joint_Deterioration_2	,db.c.ds_Joint_Seal_Deterioration_0	,db.c.ds_Joint_Seal_Deterioration_1
    ,db.c.ds_Joint_Seal_Deterioration_2	,db.c.ds_Lane_Shoulder_Dropoff_0	,db.c.ds_Lane_Shoulder_Dropoff_1
    ,db.c.ds_Lane_Shoulder_Dropoff_2	,db.c.ds_Longitudinal_Cracking_0	,db.c.ds_Longitudinal_Cracking_1
    ,db.c.ds_Longitudinal_Cracking_2	,db.c.ds_Map_Cracking_0	,db.c.ds_Map_Cracking_1	,db.c.ds_Map_Cracking_2
    ,db.c.ds_Patching_0	,db.c.ds_Patching_1	,db.c.ds_Patching_2	,db.c.ds_Potholes_0	,db.c.ds_Potholes_1
    ,db.c.ds_Potholes_2	,db.c.ds_Pumping_0	,db.c.ds_Pumping_1	,db.c.ds_Pumping_2	,db.c.ds_Punchouts_0
    ,db.c.ds_Punchouts_1	,db.c.ds_Punchouts_2	,db.c.ds_Raveling_0	,db.c.ds_Raveling_1	,db.c.ds_Raveling_2
    ,db.c.ds_Refl_Crack_Transverse_0	,db.c.ds_Refl_Crack_Transverse_1	,db.c.ds_Refl_Crack_Transverse_2
    ,db.c.ds_Reflective_Cracking_Long_0	,db.c.ds_Reflective_Cracking_Long_1	,db.c.ds_Reflective_Cracking_Long_2
    ,db.c.ds_Rutting_0	,db.c.ds_Rutting_1	,db.c.ds_Rutting_2	,db.c.ds_Slab_Replacement	,db.c.ds_Slab_Replacement_0
    ,db.c.ds_Slab_Replacement_1	,db.c.ds_Spalling_Longitudinal_0	,db.c.ds_Spalling_Longitudinal_1
    ,db.c.ds_Spalling_Longitudinal_2	,db.c.ds_Spalling_Transverse_0	,db.c.ds_Spalling_Transverse_1
    ,db.c.ds_Spalling_Transverse_2	,db.c.ds_Transverse_Cracking_0	,db.c.ds_Transverse_Cracking_1
    ,db.c.ds_Transverse_Cracking_2	,db.c.ds_Slab_Replacement_2).filter(db.c.RoadName == self.my_sri) 

            
            if self.FilterColumncheckBox.isChecked() == True:
                stmt = stmt.filter(db.c.FilterColumn == 1)

            results2 = self.my_session.execute(stmt)
            
            for item2 in results2.keys():
                my_ds_keys.append(item2)

            for item2 in results2:
                my_ds_data.append(item2)
               


            stmt = sa.select(db.c.id,db.c.Name,db.c.RoadName,db.c.From,db.c.To,db.c.pvmt_analysis_section_id
    ,db.c.dd_Alligator_Cracking_0	,db.c.dd_Alligator_Cracking_1	,db.c.dd_Alligator_Cracking_2
    ,db.c.dd_Bleeding_0	,db.c.dd_Bleeding_1	,db.c.dd_Bleeding_2	,db.c.dd_Block_Cracking_0
    ,db.c.dd_Block_Cracking_1	,db.c.dd_Block_Cracking_2	,db.c.dd_Blowup_0	,db.c.dd_Blowup_1
    ,db.c.dd_Blowup_2	,db.c.dd_Corner_Break_0	,db.c.dd_Corner_Break_1	,db.c.dd_Corner_Break_2
    ,db.c.dd_D_Cracking_0	,db.c.dd_D_Cracking_1	,db.c.dd_D_Cracking_2	,db.c.dd_Edge_Cracking_0
    ,db.c.dd_Edge_Cracking_1	,db.c.dd_Edge_Cracking_2	,db.c.dd_Faulting_0	,db.c.dd_Faulting_1
    ,db.c.dd_Faulting_2	,db.c.dd_IRI_0	,db.c.dd_IRI_1	,db.c.dd_IRI_2
    ,db.c.dd_Joint_Count_0	,db.c.dd_Joint_Count_1	,db.c.dd_Joint_Count_2	,db.c.dd_Joint_Deterioration_0
    ,db.c.dd_Joint_Deterioration_1	,db.c.dd_Joint_Deterioration_2	,db.c.dd_Joint_Seal_Deterioration_0
    ,db.c.dd_Joint_Seal_Deterioration_1	,db.c.dd_Joint_Seal_Deterioration_2	,db.c.dd_Lane_Shoulder_Dropoff_0
    ,db.c.dd_Lane_Shoulder_Dropoff_1	,db.c.dd_Lane_Shoulder_Dropoff_2	,db.c.dd_Longitudinal_Cracking_0
    ,db.c.dd_Longitudinal_Cracking_1	,db.c.dd_Longitudinal_Cracking_2	,db.c.dd_Map_Cracking_0
    ,db.c.dd_Map_Cracking_1	,db.c.dd_Map_Cracking_2	,db.c.dd_Patching_0	,db.c.dd_Patching_1	,db.c.dd_Patching_2
    ,db.c.dd_Potholes_0	,db.c.dd_Potholes_1	,db.c.dd_Potholes_2	,db.c.dd_Pumping_0	,db.c.dd_Pumping_1
    ,db.c.dd_Pumping_2	,db.c.dd_Punchouts_0	,db.c.dd_Punchouts_1	,db.c.dd_Punchouts_2	,db.c.dd_Punchouts_ph
    ,db.c.dd_Raveling_0	,db.c.dd_Raveling_1	,db.c.dd_Raveling_2	,db.c.dd_Refl_Crack_Transverse_0
    ,db.c.dd_Refl_Crack_Transverse_1	,db.c.dd_Refl_Crack_Transverse_2	,db.c.dd_Reflective_Cracking_Long_0
    ,db.c.dd_Reflective_Cracking_Long_1	,db.c.dd_Reflective_Cracking_Long_2	,db.c.dd_Rutting_0	,db.c.dd_Rutting_1
    ,db.c.dd_Rutting_2	,db.c.dd_Slab_Replacement	,db.c.dd_Slab_Replacement_0	,db.c.dd_Slab_Replacement_1
    ,db.c.dd_Spalling_Longitudinal_0	,db.c.dd_Spalling_Longitudinal_1	,db.c.dd_Spalling_Longitudinal_2
    ,db.c.dd_Spalling_Transverse_0	,db.c.dd_Spalling_Transverse_1	,db.c.dd_Spalling_Transverse_2
    ,db.c.dd_Transverse_Cracking_0	,db.c.dd_Transverse_Cracking_1	,db.c.dd_Transverse_Cracking_2
    ,db.c.dd_Slab_Replacement_2).filter(db.c.RoadName == self.my_sri).order_by(db.c.RoadName, db.c.From)  
            

            if self.FilterColumncheckBox.isChecked() == True:
                stmt = stmt.filter(db.c.FilterColumn == 1)

            results3 = self.my_session.execute(stmt)

            for item3 in results3.keys():    
                my_dd_keys.append(item3)
               

            for item3 in results3:    
                my_dd_data.append(item3)
               
            
         
            self.VAS_tableWidget.clearContents()
            self.VAS_DS_tableWidget.clearContents()
            self.VAS_DD_tableWidget.clearContents()
            
            tableCreate2(self.VAS_tableWidget,my_vas_keys, my_vas_data)
            tableCreate2(self.VAS_DS_tableWidget,my_ds_keys, my_ds_data)
            tableCreate2(self.VAS_DD_tableWidget,my_dd_keys, my_dd_data)
            
            self.VAS_tableWidget.viewport().update()
            self.VAS_DS_tableWidget.viewport().update()
            self.VAS_DD_tableWidget.viewport().update()

            self.tabWidget.setCurrentIndex(0)
        
            
        else:
            pass
            


  

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form =  VAS_VIEW()
    form.show()

    sys.exit(app.exec())
