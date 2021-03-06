# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD:Script/task.py
Created on Thu Nov 30 14:11:38 ****
=======
Created on Wed Nov 29 13:35:12 ****
>>>>>>> 6d016066d07e0a58c7a778636273b2e278395dab:task.py

@author: Gn
"""

import openapi 
import time 
import tools
import config
import main    
        
def task(access_token,requestId): 
<<<<<<< HEAD:Script/task.py
    sql = 'select TaskId,InterfaceType from ' + config.DatabaseInfo['DatabaseInterfaceTable'] + ' where Direction = 1 and ( TaskState = 0 or TaskState = 3 )' 
    datas = tools.database(sql) 
    tools.log("TaskIds : " + str(datas),'info')
=======
>>>>>>> 6d016066d07e0a58c7a778636273b2e278395dab:task.py

    # Task表交互机制============================================================================= 
    #从Task表里筛选出状态为0或3，方向为1的任务的TaskId和InterfaceType，根据不同的InterfaceType使用checkapi字典映射调用api方法
    sql = 'select TaskId,InterfaceType from ' + config.DatabaseInfo['DatabaseInterfaceTable'] + ' where Direction = 1 and ( TaskState = 0 or TaskState = 3 )' 
    datas = tools.database(sql) 
    tools.log("TaskIds : " + str(datas),'info')
    #InterfaceType写对应接口的数据库表名，默认值为General,用于调试和特殊任务 
    checkapi = {'ABSAssetBag':main.assetsSold 
                ,'ABSTrustPaymentOrder':main.assetsPlanPay 
                ,'ABSPresale':main.assetsAdjust
                ,'':main.passTask} 
    checkapiJson = {'ABSAssetBag':'assetsSold'
                ,'ABSTrustPaymentOrder':'assetsPlanPay' 
                ,'ABSPresale':'assetsAdjust'
                ,'':'no TaskName'}
    i = 0 
    while i<len(datas): 
        i = i + 1 
        data = datas[i-1] 
        InterfaceType = data[1] 
        TaskId = data[0] 
        tools.log("TaskId : "+TaskId,'info')
        tools.log("TaskFunc : "+checkapiJson[InterfaceType],'info')
        checkapi[InterfaceType](access_token,requestId,TaskId)
    return
        
        
if __name__ == '__main__': 
    tools.log("DataInterfaceTask Start--",'warn')
    access_token = openapi.getToken() 
    requestId = str(int(time.time())) 
    
    task(access_token,requestId)
    tools.log("DataInterfaceTask End--",'warn')
