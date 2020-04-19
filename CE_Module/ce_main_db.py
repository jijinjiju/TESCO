# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 20:31:48 2020

@author: JijinAV
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:47:14 2020

@author: JijinAV
"""

from db.ce_db import pushDB
from utility.ce_module import ce_utility


if __name__=='__main__':
    
    #Step 1 creating an object of ce_utility class in ce_module file
    ce_util=ce_utility()
    
    output=ce_util.generate_DF()
    
    print(output)
    
    """
    #create an object of pushDB class
    db_con=pushDB()
    
    #write the final output to mysql table
    db_con.write(output)
    """
    