


from sqlalchemy import create_engine, MetaData,Table
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy.ext.declarative import declarative_base

import sqlalchemy as sa
import sqlalchemy.orm as sao
import sqlalchemy.ext.declarative as sad
from sqlalchemy.ext.automap import automap_base

debug_session = True

maker = sessionmaker(autoflush=True, autocommit=False)
DBSession = scoped_session(maker)

DBase = declarative_base()
metadata = DBase.metadata

def init_model(engine):
    """Call me before using any of the tables or classes in the model."""
    DBSession.configure(bind=engine)


metadata1 = MetaData()

def gather_tables(my_self):

    engine = create_engine(my_self.my_url)
    metadata = MetaData()
    errorflag = -1
    try:
        if my_self.my_login.database_type == 0:
    # oracle   
      
            my_self.my_db_tables.VAnalysisSamples = Table('VAnalysisSamples', metadata,autoload_with = engine) 
            my_self.my_db_tables.AnalysisSamples = Table('AnalysisSamples', metadata,autoload_with = engine) 
            my_self.my_db_tables.AnalysisSamples_Base = Table('AnalysisSamples_Base', metadata,autoload_with = engine) 
            my_self.my_db_tables.VAnalysis_Sections  = Table('VAnalysis_Sections', metadata,autoload_with = engine) 
            my_self.my_db_tables.Analysis_Sections = Table('Analysis_Sections', metadata,autoload_with = engine) 
            my_self.my_db_tables.Analysis_Sections_Base = Table('Analysis_Sections_Base', metadata,autoload_with = engine)

            my_self.my_db_tables.VAnalysis_Sections_Raw = Table('VAnalysis_Sections_RAW', metadata,autoload_with = engine)	
            my_self.my_db_tables.Analysis_Sections_Raw = Table('Analysis_Sections_RAW', metadata,autoload_with = engine) 
            my_self.my_db_tables.Analysis_Sections_Raw_Base = Table('Analysis_Sections_RAW_Base', metadata,autoload_with = engine) 
    
            my_self.my_db_tables.VBase = Table('VBase', metadata,autoload_with = engine) 
            my_self.my_db_tables.Base = Table('Base', metadata,autoload_with = engine) 
            my_self.my_db_tables.Base_Chunks = Table('Base_Chunks', metadata,autoload_with = engine) 
            my_self.my_db_tables.Chunks  = Table('Chunks', metadata,autoload_with = engine) 
    
            my_self.my_db_tables.VConst_Reh_Lyr_Detail = Table('VConst_Reh_Lyr_Detail', metadata,autoload_with = engine) 
            my_self.my_db_tables.Const_Reh_Lyr_Detail = Table('Const_Reh_Lyr_Detail', metadata,autoload_with = engine) 
            my_self.my_db_tables.VConst_Rehab_History = Table('VConst_Rehab_History', metadata,autoload_with = engine) 
            my_self.my_db_tables.Const_Rehab_History = Table('Const_Rehab_History', metadata,autoload_with = engine) 
            my_self.my_db_tables.Const_Rehab_History_Base = Table('Const_Rehab_History_Base', metadata,autoload_with = engine) 
    
            my_self.my_db_tables.VDist_Feat_Tenth_2012 = Table('VDist_Feat_Tenth_2012', metadata,autoload_with = engine) 
            my_self.my_db_tables.Dist_Feat_Tenth_2012 = Table('Dist_Feat_Tenth_2012', metadata,autoload_with = engine) 
            my_self.my_db_tables.Dist_Feat_Tenth_2012_Base  = Table('Dist_Feat_Tenth_2012_Base', metadata,autoload_with = engine)

            my_self.my_db_tables.VDstrs_Feature_2012 = Table('VDstrs_Feature_2012', metadata,autoload_with = engine) 
            my_self.my_db_tables.Dstrs_Feature_2012 = Table('Dstrs_Feature_2012', metadata,autoload_with = engine) 
            my_self.my_db_tables.Dstrs_Feature_2012_Base = Table('Dstrs_Feature_2012_Base', metadata,autoload_with = engine)

            my_self.my_db_tables.VLandmark = Table('VLandmark', metadata,autoload_with = engine) 
            my_self.my_db_tables.Landmark = Table('Landmark', metadata,autoload_with = engine) 
            my_self.my_db_tables.Landmark_Base = Table('Landmark_Base', metadata,autoload_with = engine)

            my_self.my_db_tables.VLane = Table('VLane', metadata,autoload_with = engine) 
            my_self.my_db_tables.Lane = Table('Lane', metadata,autoload_with = engine) 
            my_self.my_db_tables.Lane_Base = Table('Lane_Base', metadata,autoload_with = engine) 

            my_self.my_db_tables.MDOTSectionCondition = Table('MDOTSectionCondition', metadata,autoload_with = engine) 
    
            my_self.my_db_tables.VProject = Table('VProject', metadata,autoload_with = engine) 
            my_self.my_db_tables.Project = Table('Project', metadata,autoload_with = engine) 

            my_self.my_db_tables.VSRVY_DISTRESS_FEATURES = Table('VSRVY_DISTRESS_FEATURES', metadata,autoload_with = engine) 
            my_self.my_db_tables.SRVY_DISTRESS_FEATURES = Table('SRVY_DISTRESS_FEATURES', metadata,autoload_with = engine) 

            my_self.my_db_tables.VSRVY_MRI_1_10_MILE = Table('VSRVY_MRI_1_10_MILE', metadata,autoload_with = engine) 
            my_self.my_db_tables.SRVY_MRI_1_10_MILE = Table('SRVY_MRI_1_10_MILE', metadata,autoload_with = engine) 

            my_self.my_db_tables.VSRVY_PVMT_DSTRS_FEATURE_TENTH = Table('VSRVY_PVMT_DSTRS_FEATURE_TENTH', metadata,autoload_with = engine) 
            my_self.my_db_tables.SRVY_PVMT_DSTRS_FEATURE_TENTH = Table('SRVY_PVMT_DSTRS_FEATURE_TENTH', metadata,autoload_with = engine) 

            my_self.my_db_tables.VSRVY_PVMT_SAMPLE_SGMT = Table('VSRVY_PVMT_SAMPLE_SGMT', metadata,autoload_with = engine) 
            my_self.my_db_tables.SRVY_PVMT_SAMPLE_SGMT = Table('SRVY_PVMT_SAMPLE_SGMT', metadata,autoload_with = engine) 

            my_self.my_db_tables.VSRVY_PVMT_SCTN_COND = Table('VSRVY_PVMT_SCTN_COND', metadata,autoload_with = engine) 
            my_self.my_db_tables.SRVY_PVMT_SCTN_COND = Table('SRVY_PVMT_SCTN_COND', metadata,autoload_with = engine) 

            my_self.my_db_tables.VSRVY_PVMT_SCTN_DISTRESS = Table('VSRVY_PVMT_SCTN_DISTRESS', metadata,autoload_with = engine) 
            my_self.my_db_tables.SRVY_PVMT_SCTN_DISTRESS = Table('SRVY_PVMT_SCTN_DISTRESS', metadata,autoload_with = engine) 

            my_self.my_db_tables.VSample_Segment = Table('VSample_Segment', metadata,autoload_with = engine) 
            my_self.my_db_tables.Sample_Segment = Table('Sample_Segment', metadata,autoload_with = engine) 
            my_self.my_db_tables.Sample_Segment_Base = Table('Sample_Segment_Base', metadata,autoload_with = engine) 
    
            my_self.my_db_tables.VTraffic = Table('VTraffic', metadata,autoload_with = engine) 
            my_self.my_db_tables.Traffic = Table('Traffic', metadata,autoload_with = engine) 
            my_self.my_db_tables.Traffic_Base  = Table('Traffic_Base', metadata,autoload_with = engine) 

            my_self.my_db_tables.VWeightLimits = Table('VWeightLimits', metadata,autoload_with = engine) 
            my_self.my_db_tables.WeightLimits = Table('WeightLimits', metadata,autoload_with = engine) 
            my_self.my_db_tables.WeightLimits_Base = Table('WeightLimits_Base', metadata,autoload_with = engine) 

            my_self.my_db_tables.VAnalysis_Sections_DS = Table('VAnalysis_Sections_DS', metadata,autoload_with = engine) 
            my_self.my_db_tables.Analysis_Sections_DS = Table('Analysis_Sections_DS', metadata,autoload_with = engine) 
            my_self.my_db_tables.Analysis_Sections_DS_Base = Table('Analysis_Sections_DS_Base', metadata,autoload_with = engine)

            my_self.my_db_tables.VAnalysis_Sections_DD = Table('VAnalysis_Sections_DD', metadata,autoload_with = engine) 
            my_self.my_db_tables.Analysis_Sections_DD = Table('Analysis_Sections_DD', metadata,autoload_with = engine) 
            my_self.my_db_tables.Analysis_Sections_DD_Base = Table('Analysis_Sections_DD_Base', metadata,autoload_with = engine) 

            my_self.my_db_tables.MDOTDistresses = Table('MDOTDistresses', metadata,autoload_with = engine) 
            my_self.my_db_tables.VCounty = Table('VCountyNames',metadata, autoload_with = engine)
            my_self.my_db_tables.MDOTLOG = Table('MDOTLOG',metadata,autoload_with = engine)
            errorflag = 0
        else:

            my_self.my_db_tables.VAnalysisSamples = Table('VAnalysisSamples', metadata,autoload_with = engine) 
            my_self.my_db_tables.AnalysisSamples = Table('AnalysisSamples', metadata,autoload_with = engine) 
            my_self.my_db_tables.AnalysisSamples_Base = Table('AnalysisSamples_Base', metadata,autoload_with = engine) 
            my_self.my_db_tables.VAnalysis_Sections  = Table('VAnalysis_Sections', metadata,autoload_with = engine) 
            my_self.my_db_tables.Analysis_Sections = Table('Analysis_Sections', metadata,autoload_with = engine) 
            my_self.my_db_tables.Analysis_Sections_Base = Table('Analysis_Sections_Base', metadata,autoload_with = engine)

            my_self.my_db_tables.VAnalysis_Sections_Raw = Table('VAnalysis_Sections_RAW', metadata,autoload_with = engine)	
            my_self.my_db_tables.Analysis_Sections_Raw = Table('Analysis_Sections_RAW', metadata,autoload_with = engine) 
            my_self.my_db_tables.Analysis_Sections_Raw_Base = Table('Analysis_Sections_RAW_Base', metadata,autoload_with = engine) 
    
            my_self.my_db_tables.VBase = Table('VBase', metadata,autoload_with = engine) 
            my_self.my_db_tables.Base = Table('Base', metadata,autoload_with = engine) 
            my_self.my_db_tables.Base_Chunks = Table('Base_Chunks', metadata,autoload_with = engine) 
            my_self.my_db_tables.Chunks  = Table('Chunks', metadata,autoload_with = engine) 
    
            my_self.my_db_tables.VConst_Reh_Lyr_Detail = Table('VConst_Reh_Lyr_Detail', metadata,autoload_with = engine) 
            my_self.my_db_tables.Const_Reh_Lyr_Detail = Table('Const_Reh_Lyr_Detail', metadata,autoload_with = engine) 
            my_self.my_db_tables.VConst_Rehab_History = Table('VConst_Rehab_History', metadata,autoload_with = engine) 
            my_self.my_db_tables.Const_Rehab_History = Table('Const_Rehab_History', metadata,autoload_with = engine) 
            my_self.my_db_tables.Const_Rehab_History_Base = Table('Const_Rehab_History_Base', metadata,autoload_with = engine) 
    
            my_self.my_db_tables.VDist_Feat_Tenth_2012 = Table('VDist_Feat_Tenth_2012', metadata,autoload_with = engine) 
            my_self.my_db_tables.Dist_Feat_Tenth_2012 = Table('Dist_Feat_Tenth_2012', metadata,autoload_with = engine) 
            my_self.my_db_tables.Dist_Feat_Tenth_2012_Base  = Table('Dist_Feat_Tenth_2012_Base', metadata,autoload_with = engine)

            my_self.my_db_tables.VDstrs_Feature_2012 = Table('VDstrs_Feature_2012', metadata,autoload_with = engine) 
            my_self.my_db_tables.Dstrs_Feature_2012 = Table('Dstrs_Feature_2012', metadata,autoload_with = engine) 
            my_self.my_db_tables.Dstrs_Feature_2012_Base = Table('Dstrs_Feature_2012_Base', metadata,autoload_with = engine)

            my_self.my_db_tables.VLandmark = Table('VLandmark', metadata,autoload_with = engine) 
            my_self.my_db_tables.Landmark = Table('Landmark', metadata,autoload_with = engine) 

            my_self.my_db_tables.MDOTSectionCondition = Table('MDOTSectionCondition', metadata,autoload_with = engine) 
    
            my_self.my_db_tables.VProject = Table('VProject', metadata,autoload_with = engine) 
            my_self.my_db_tables.Project = Table('Project', metadata,autoload_with = engine) 

            my_self.my_db_tables.VSRVY_DISTRESS_FEATURES = Table('VSRVY_DISTRESS_FEATURES', metadata,autoload_with = engine) 
            my_self.my_db_tables.SRVY_DISTRESS_FEATURES = Table('SRVY_DISTRESS_FEATURES', metadata,autoload_with = engine) 

            my_self.my_db_tables.VSRVY_MRI_1_10_MILE = Table('VSRVY_MRI_1_10_MILE', metadata,autoload_with = engine) 
            my_self.my_db_tables.SRVY_MRI_1_10_MILE = Table('SRVY_MRI_1_10_MILE', metadata,autoload_with = engine) 

            my_self.my_db_tables.VSRVY_PVMT_DSTRS_FEATURE_TENTH = Table('VSRVY_PVMT_DSTRS_FEATURE_TENTH', metadata,autoload_with = engine) 
            my_self.my_db_tables.SRVY_PVMT_DSTRS_FEATURE_TENTH = Table('SRVY_PVMT_DSTRS_FEATURE_TENTH', metadata,autoload_with = engine) 

            my_self.my_db_tables.VSRVY_PVMT_SAMPLE_SGMT = Table('VSRVY_PVMT_SAMPLE_SGMT', metadata,autoload_with = engine) 
            my_self.my_db_tables.SRVY_PVMT_SAMPLE_SGMT = Table('SRVY_PVMT_SAMPLE_SGMT', metadata,autoload_with = engine) 

            my_self.my_db_tables.VSRVY_PVMT_SCTN_COND = Table('VSRVY_PVMT_SCTN_COND', metadata,autoload_with = engine) 
            my_self.my_db_tables.SRVY_PVMT_SCTN_COND = Table('SRVY_PVMT_SCTN_COND', metadata,autoload_with = engine) 

            my_self.my_db_tables.VSRVY_PVMT_SCTN_DISTRESS = Table('VSRVY_PVMT_SCTN_DISTRESS', metadata,autoload_with = engine) 
            my_self.my_db_tables.SRVY_PVMT_SCTN_DISTRESS = Table('SRVY_PVMT_SCTN_DISTRESS', metadata,autoload_with = engine) 

            my_self.my_db_tables.VSample_Segment = Table('VSample_Segment', metadata,autoload_with = engine) 
            my_self.my_db_tables.Sample_Segment = Table('Sample_Segment', metadata,autoload_with = engine) 
            my_self.my_db_tables.Sample_Segment_Base = Table('Sample_Segment_Base', metadata,autoload_with = engine) 
    
            my_self.my_db_tables.VTraffic = Table('VTraffic', metadata,autoload_with = engine) 
            my_self.my_db_tables.Traffic = Table('Traffic', metadata,autoload_with = engine) 
            my_self.my_db_tables.Traffic_Base  = Table('Traffic_Base', metadata,autoload_with = engine) 

            my_self.my_db_tables.VWeightLimits = Table('VWeightLimits', metadata,autoload_with = engine) 
            my_self.my_db_tables.WeightLimits = Table('WeightLimits', metadata,autoload_with = engine) 
            my_self.my_db_tables.WeightLimits_Base = Table('WeightLimits_Base', metadata,autoload_with = engine) 

            #my_self.my_db_tables.VAnalysis_Sections_DS = Table('VAnalysis_Sections_DS', metadata,autoload_with = engine) 
            #my_self.my_db_tables.Analysis_Sections_DS = Table('Analysis_Sections_DS', metadata,autoload_with = engine) 
            #my_self.my_db_tables.Analysis_Sections_DS_Base = Table('Analysis_Sections_DS_Base', metadata,autoload_with = engine)

            #my_self.my_db_tables.VAnalysis_Sections_DD = Table('VAnalysis_Sections_DD', metadata,autoload_with = engine) 
            #my_self.my_db_tables.Analysis_Sections_DD = Table('Analysis_Sections_DD', metadata,autoload_with = engine) 
            #my_self.my_db_tables.Analysis_Sections_DD_Base = Table('Analysis_Sections_DD_Base', metadata,autoload_with = engine) 

            #my_self.my_db_tables.MDOTDistresses = Table('MDOTDistresses', metadata,autoload_with = engine) 
            my_self.my_db_tables.VCounty = Table('VCountyNames',metadata, autoload_with = engine)
            my_self.my_db_tables.MDOTLOG = Table('MDOTLOG',metadata,autoload_with = engine)
            errorflag = 0
                        
        
    except sa.exc.SQLAlchemyError as ex:
        errorflag = -1
        pass
   
    return errorflag

def get_table_county(my_self):
   
    engine = create_engine(my_self.url)
    metadata = MetaData()
    errorflag = -1
    try:
        if my_self.database_type == 0:
             
            my_self.my_db_tables.VCounty = Table('VCountyNames', metadata,autoload_with = engine) 
            errorflag = 0   
            pass
        else:   
            my_self.my_db_tables.VCounty = Table('VCountyNames', metadata,autoload_with = engine) 
            errorflag = 0
            pass

    except sa.exc.SQLAlchemyError as ex:
        errorflag = -1
        pass

    return errorflag


def get_table_route(my_self):
   
    engine = create_engine(my_selfmy_.url)
    metadata = MetaData()
    errorflag = -1
    try:
        if my_self.database_type == 0:
             
            my_self.VBase = Table('VBase', metadata,autoload_with = engine) 
            errorflag = 0   
            pass
        else:   
            my_self.VBase = Table('VBase', metadata,autoload_with = engine) 
            errorflag = 0
            pass

    except sa.exc.SQLAlchemyError as ex:
        errorflag = -1
        pass

    return errorflag


def get_table_direction(my_self):
   
    engine = create_engine(my_self.url)
    metadata = MetaData()
    errorflag = -1
    try:
        if my_self.database_type == 0:
             
            my_self.VBase = Table('VBase', metadata,autoload_with = engine) 
            errorflag = 0   
            pass
        else:   
            my_self.VBase = Table('VBase', metadata,autoload_with = engine) 
            errorflag = 0
            pass

    except sa.exc.SQLAlchemyError as ex:
        errorflag = -1
        pass

    return errorflag

def get_table_VAS(my_self):
   
    engine = create_engine(my_self.url)
    metadata = MetaData()
    errorflag = -1
    try:
        if my_self.database_type == 0:
             
            my_self.VAnalysis_Sections = Table('VAnalysis_Sections', metadata,autoload_with = engine) 
            errorflag = 0   
            pass
        else:   
            my_self.VAnalysis_Sections = Table('VAnalysis_Sections', metadata,autoload_with = engine) 
            errorflag = 0
            pass

    except sa.exc.SQLAlchemyError as ex:
        errorflag = -1
        pass

    return errorflag

def get_table_analysis_sections(my_self):
   
    engine = create_engine(my_self.url)
    metadata = MetaData()
    errorflag = -1
    try:
        if my_self.database_type == 0:
             
            my_self.Analysis_Sections = Table('Analysis_Sections', metadata,autoload_with = engine) 
            errorflag = 0   
            pass
        else:   
            my_self.Analysis_Sections = Table('Analysis_Sections', metadata,autoload_with = engine) 
            errorflag = 0
            pass

    except sa.exc.SQLAlchemyError as ex:
        errorflag = -1
        pass

    return errorflag

def get_table_log(url):
   
    engine = create_engine(url)
    metadata = MetaData()
    errorflag = -1
    try:
      
        logLink = Table('MDOTLOG', metadata,autoload_with = engine) 
        errorflag = 0   
       

    except sa.exc.SQLAlchemyError as ex:
        errorflag = -1
        return errorflag
        pass

    return logLink

    

    