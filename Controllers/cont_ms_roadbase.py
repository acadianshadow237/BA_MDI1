



#import Models.my_tables_model as db_mbm
##import cont_RoadBase.viewmodels as rb


#----------------------------------------------------------------------
def getAllRecords(session):
    """
    Get all records and return them
    """
    result = session.query(rb.VBase).order_by(rb.VBase.Name,rb.VBase.From).all()
    return result

#def getOneRecordBy_id(session,m_id):
#    """
#    Get one records and return it based in its id

#    """
#    result = session.query(rb.VBase).filter_by(id = m_id).all()
#    return result
#def getRecordBy_RoadName(session,m_RoadName):
#    """
#    Get one records and return it based in its RoadName

#    """
#    result = session.query(rb.VBase).filter_by(id = m_roadName).order_by(From).all()
#    return result

#def addNewRecord(session,m_data):
    
#    b1= db_mbmBase(
#    id = m_data.id,
#    Name 				= m_data.Name,
#    SelectRole 		    = m_data.SelectRole,
#    UpDateRole 		= m_data.UpDateRole,
#    DeleteRole 		    = m_data.DeleteRole,
#    Route_Class 	    = m_data.Route_Class,
#    Route_ID 		    = m_data.Route_ID,
#    Pass_Direction 	    = m_data.Pass_Direction,
#    Inventory_Number    = m_data.Inventory_Number,
#    id_1 			    = m_data.id_1,
#    Street_Name 	    = m_data.Street_Name,
#    zz_Deighton_Fix 	= m_data.zz_Deighton_Fix,
#    data_accum_direction = m_data.data_accum_direction,
#    County 			    = m_data.County,
#    Segment_Number 	    = m_data.Segment_Number	)
   
#    c1 = db_mbmChunk(
#    id 		    = m_data.ChunkID,
#    Length 			    = m_data.Length,
#    Geo  = m_data.Map)    
   
#    bc1 = db_mbmBaseChunk(
#    id = m_data.NetworkID,
#    lprid = m_data.id,
#    ChunkID 		    = m_data.ChunkID,
#    FromMeasure 	    = m_data.FromMeasure,
#    ToMeasure 		    = m_data.ToMeasure,
#    From                = m_data.From,
#    To 					= m_data.To,
#    ValidOn 		    = m_data.ValidOn,
#    ValidTo 		    = m_data.ValidTo,
#    CreatedOn 		    = m_data.CreatedOn,
#    EndedOn 		    = m_data.EndedOn,
#    Map 			    = m_data.Map,
#    Offset 			    = m_data.Offset,
#    End 			    = m_data.End)
    
        
#    session.add(b1)
#    session.add(c1)
#    session.add(bc1)
#    session.commit()

#def deleteRecordByID(session,m_id):
#    """
#    delete a single record by id
    
#    """
#    r1=session.query(rb.VBase).filter(id == m_id).one()

#    b1 = session.query(db_mbmBase).filter(id == r1.id)
#    c1 = session.query(db_mbmChunk).filter(id == r1.ChunkID)
#    bc1 = session.query(db_mbmBaseChunk).filter(id == r1.NetworkID)    

#    session.delete(b1)
#    session.delete(c1)
#    session.delete(bc1)
#    session.commit()


#def upDateRecord(session,m_id,m_data):
    
#    vb1 = session.query(rb.VBase).filter(id == m_id).one()    

#    b1 = session.query(db_mbmBase).filter(id == vb1.id)
#    c1  = session.query(db_mbmChunk).filter(id == vb1.ChunkID)
#    bc1 = session.query(db_mbmBaseChunk).filter(id = vb1.NetworkID)

#    b1= db_mbmBase(
#    id                  = m_data.id,
#    Name 				= m_data.Name,
#    SelectRole 		    = m_data.SelectRole,
#    UpDateRole 		= m_data.UpDateRole,
#    DeleteRole 		    = m_data.DeleteRole,
#    Route_Class 	    = m_data.Route_Class,
#    Route_ID 		    = m_data.Route_ID,
#    Pass_Direction 	    = m_data.Pass_Direction,
#    Inventory_Number    = m_data.Inventory_Number,
#    id_1 			    = m_data.id_1,
#    Street_Name 	    = m_data.Street_Name,
#    zz_Deighton_Fix 	= m_data.zz_Deighton_Fix,
#    data_accum_direction = m_data.data_accum_direction,
#    County 			    = m_data.County,
#    Segment_Number 	    = m_data.Segment_Number	)
   
#    c1 = db_mbmChunk(
#    id 		    = m_data.ChunkID,
#    Length 		= m_data.Length,
#    Geo         = m_data.Map)    
   
#    bc1 = db_mbmBaseChunk(
#    id                  = m_data.NetworkID,
#    lprid               = m_data.id,
#    ChunkID 		    = m_data.ChunkID,
#    FromMeasure 	    = m_data.FromMeasure,
#    ToMeasure 		    = m_data.ToMeasure,
#    From                = m_data.From,
#    To 					= m_data.To,
#    ValidOn 		    = m_data.ValidOn,
#    ValidTo 		    = m_data.ValidTo,
#    CreatedOn 		    = m_data.CreatedOn,
#    EndedOn 		    = m_data.EndedOn,
#    Map 			    = m_data.Map,
#    Offset 			    = m_data.Offset,
#    End 			    = m_data.End)
    
        
#    session.add(b1)
#    session.add(c1)
#    session.add(bc1)
#    session.commit()
