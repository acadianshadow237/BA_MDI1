




class login_stuff(object):
    def __init__(self):
        self.user_name = ''
        self.user_password = ''
        self.server_name = ''
        self.database_name = ''
        self.schema = ''
        self.database_type = 0

    


def url_builder(this_login):

    oracle_url = None
    mssql_url = None
       
    if (this_login.database_type) == 0:
        ## oracle+cx_oracle://USER_MISS:password@ORACLEDEV01:1521/GISPROD
        oracle_url = f'oracle+cx_oracle://{this_login.user_name}:{this_login.user_password}@{this_login.server_name}:1521/{this_login.database_name}'

        return oracle_url
    else:
        ## mssql+pyodbc://rvincent:Nicolesusan01!@myDTIMs
        ##mssql+pymssql://dtims_user:password@rsch11948/BA_MDOT_2020_03_30_SQL

        mssql_url = f'mssql+pymssql://{this_login.user_name}:{this_login.user_password}@{this_login.server_name}:1433/{this_login.database_name}'
        
        return mssql_url

      
            
        
    
    
    
    
        