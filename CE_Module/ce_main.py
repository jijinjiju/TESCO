# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:47:14 2020

@author: Jijin A V
"""


import json
import pandas as pd
from utility.ce_module import ce_utility


if __name__=='__main__':
    
    #let data be the JSON object
    with open('input\\000000000000b527df0596af9165.json') as f:
        data = json.load(f)  
         
    
    #Step 1 creating an object of ce_utility class in ce_module file
    ce_util=ce_utility()
    
    #Step 2 decode subject from json and assign it back to same file
    data=ce_util.decode_json_data(data)
    
    
    value_field=[[data['entry_id'],data['subject']]]
    result=pd.DataFrame(value_field)
    
    print(result)
 
    
    """
    
    #Step 3 if the mail is not a meeting invite, generate the JSON file
    if(not ce_util.check_meeting_invite(data)):
        with open(data['entry_id']+".json","w", encoding='utf_16') as jsonfile:
            json.dump(data,jsonfile,ensure_ascii=False)
            
    """
    """
    with open('data_output2.json',encoding='utf_16') as f:
        data = json.load(f)
        print(data)
    """
    