# Git clone in terminal or git dash or VS 

# by terminal git clone (copy link)

# git clone https://github.com/PhonePe/pulse.git


# convert json file to dataframe 

#Once created the clone of GIT-HUB repository then,
#Required libraries for the program

import pandas as pd
import json
import os
#import openpyxl 

#This is to direct the path to get the data as states

#C:\Users\admin\Desktop\sivaranjani\DATA SCIENCE\project\phonepe\code\pulse\data\aggregated\transaction\country\india\state

path="C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/code/pulse/data/aggregated/transaction/country/india/state/"
Agg_state_list=os.listdir(path)
#Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

#This is to extract the data's to create a dataframe

clm={'State':[], 'Year':[],'Quater':[],'Transacion_type':[], 'Transacion_count':[], 'Transacion_amount':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)    
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)        
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              clm['Transacion_type'].append(Name)
              clm['Transacion_count'].append(count)
              clm['Transacion_amount'].append(amount)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))
#Succesfully created a dataframe
Agg_Trans=pd.DataFrame(clm)


print(Agg_Trans)


# dataframe of agg_trans to csv

Agg_Trans.to_csv("C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/csv/AggTrans_data.csv")


#This is to direct the path to get the list of user in state 

path="C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/code/pulse/data/aggregated/user/country/india/state/"
Agg_user_list=os.listdir(path)
#Agg_user_list--> to get the list of user in state

#This is to extract the data's to create a dataframe

clm = {'State': [], 'Year': [], 'Quater': [], 'User_Brand': [],
    'User_Brand_count': [], 'User_Brand_percentage': []}
for i in Agg_user_list:
    p_i = path+i+"/"
    year = os.listdir(p_i)
    for j in year:
        p_j = p_i+j+"/"
        file = os.listdir(p_j)
        for k in file:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']["usersByDevice"]:
                    brand = z['brand']
                    brand_count = z['count']
                    brand_percentage = z["percentage"]
                    clm['User_Brand'].append(brand)
                    clm['User_Brand_count'].append(brand_count)
                    clm['User_Brand_percentage'].append(brand_percentage)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
            except:
                pass 
                

Agg_user_list = pd.DataFrame(clm)

#user_by_device.to_csv('user_by_device.csv')
Agg_user_list.to_csv("C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/csv/AggTrans_user_data.csv")

# print data frame 
print(Agg_user_list)


#This is to direct the path to get the list of user in state in map 

path="C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/code/pulse/data/map/transaction/hover/country/india/state/"
Agg_map_list=os.listdir(path)
#Agg_map_list--> to get the list of transaction in state in map

#This is to extract the data's to create a dataframe

clm = {'State': [], 'Year': [], 'Quater': [], 'District': [],
    'Transaction_count': [], 'Transaction_amount': []}
for i in Agg_map_list:
    p_i = path+i+"/"
    year = os.listdir(p_i)
    for j in year:
        p_j = p_i+j+"/"
        file = os.listdir(p_j)
        for k in file:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']["hoverDataList"]:
                    district = z['name']
                    transaction_count = z['metric'][0]['count']
                    transaction_amount = z['metric'][0]['amount']
                    clm['District'].append(brand)
                    clm['Transaction_count'].append(brand_count)
                    clm['Transaction_amount'].append(brand_percentage)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
            except:
                pass 
                

Agg_map_list = pd.DataFrame(clm)

#user_by_device.to_csv('user_by_device.csv')
Agg_map_list.to_csv("C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/csv/AggTrans_map_data.csv")

# print data frame 
print(Agg_map_list)

#This is to direct the path to get the list of registered user in state in map 

path="C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/code/pulse/data/map/user/hover/country/india/state/"
Agg_mapuser_list=os.listdir(path)
#Agg_mapuser_list--> to get the list of registered users in state in map

#This is to extract the data's to create a dataframe

clm = {'State': [], 'Year': [], 'Quater': [], 'District': [],
    'Registered_user': [], 'App_opening': []}
for i in Agg_mapuser_list:
    p_i = path+i+"/"
    year = os.listdir(p_i)
    for j in year:
        p_j = p_i+j+"/"
        file = os.listdir(p_j)
        for k in file:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']["hoverData"]:
                    district = z
                    registered_user =  D['data']["hoverData"][z]["registeredUsers"]
                    app_opening = D['data']["hoverData"][z]["appOpens"]
                    clm['District'].append(district)
                    clm['Registered_user'].append(registered_user)
                    clm['App_opening'].append(app_opening)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
# Succesfully created a dataframe
            except:
                pass   
                

Agg_mapuser_list = pd.DataFrame(clm)

#user_by_device.to_csv('user_by_device.csv')
Agg_mapuser_list.to_csv("C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/csv/AggTrans_mapuser_data.csv")

# print data frame 
print(Agg_mapuser_list)