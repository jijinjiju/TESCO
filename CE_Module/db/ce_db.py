# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 20:58:25 2020

@author: JijinAV
"""

from config import config
from sqlalchemy import create_engine

class pushDB:
    
    def __init__(self):
        self.table_name =config.MYSQL_TABLE_NAME
        self.engine = create_engine(config.CONNECTION_URL)
        self.data=None
           
    def write(self,output):
        output.to_sql(name=self.table_name, con=self.engine, if_exists = 'append', index=False)   
    