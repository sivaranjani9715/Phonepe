import pandas as pd
import mysql.connector as mysql 
from mysql.connector import Error

# Aggrtrans_table 

# C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/csv/AggTrans_data.csv

aggrtrans_db = pd.read_csv('C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/csv/AggTrans_data.csv',index_col=False)
print(aggrtrans_db.head()) 

'''
# create database 
try:
    conn = mysql.connect(host='localhost',user='root',password="Ranjani@15",auth_plugin="mysql_native_password")
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE phonepe_final")
        print("phonepe_final is created")
except Error as e:
    print("Error while connecting to MySQL",e)

'''

# Select database and import the data of CSV content 
try:
    conn = mysql.connect(host='localhost',database='phonepe_final',user='root',password="Ranjani@15",auth_plugin="mysql_native_password")
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("You are connected to database: ",record)
        cursor.execute('DROP TABLE IF EXISTS Agg_Transaction_Table;')
        print('Creating table...')
        cursor.execute("CREATE TABLE Agg_Transaction_Table(MyIndex INT NOT NULL ,State LONGTEXT,Year INT,Quater INT,Payment_Mode VARCHAR(50),Total_Transactions_count BIGINT,Total_Amount BIGINT,PRIMARY KEY (MyIndex))")
        print("Agg_Transaction_Table is created....")
        for i,row in aggrtrans_db.iterrows():
            sql ="INSERT INTO phonepe_final.Agg_Transaction_Table VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,tuple(row))
            print("Record inserted")
            conn.commit() # connection is not autocommit so we do manually
except Error as e:
    print("Error while connecting to MySQL",e)

# agg_userbydevice_table

# C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/csv/AggTrans_user_data.csv'

aggrtrans_user_db = pd.read_csv(r'C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/csv/AggTrans_user_data.csv',index_col=False)
print(aggrtrans_user_db.head()) 

# Select database and import the data of CSV content 
try:
    conn = mysql.connect(host='localhost',database='phonepe_final',user='root',password="Ranjani@15",auth_plugin="mysql_native_password")
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("You are connected to database: ",record)
        cursor.execute('DROP TABLE IF EXISTS agg_userbydevice_table;')
        print('Creating table...')
        cursor.execute("CREATE TABLE agg_userbydevice_table(MyIndex INT NOT NULL ,State LONGTEXT,Year INT,Quater INT,Brand VARCHAR(50),Brand_count BIGINT,Brand_percentage BIGINT,PRIMARY KEY (MyIndex))")
        print("agg_userbydevice_table is created....")
        for i,row in aggrtrans_user_db.iterrows():
            sql ="INSERT INTO phonepe_final.agg_userbydevice_table VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,tuple(row))
            print("Record inserted")
            conn.commit() # connection is not autocommit so we do manually
except Error as e:
    print("Error while connecting to MySQL",e)

# district_map_transaction_table

# C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/csv/district_map_transaction.csv

aggrtrans_map_db = pd.read_csv('C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/csv/district_map_transaction.csv',index_col=False)
print(aggrtrans_map_db.head()) 

# Select database and import the data of CSV content 
try:
    conn = mysql.connect(host='localhost',database='phonepe_final',user='root',password="Ranjani@15",auth_plugin="mysql_native_password")
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("You are connected to database: ",record)
        cursor.execute('DROP TABLE IF EXISTS district_map_transaction_table;')
        print('Creating table...')
        cursor.execute("CREATE TABLE district_map_transaction_table(MyIndex INT NOT NULL,State LONGTEXT,Year INT,Quater INT,District VARCHAR(50),Transaction_count BIGINT,Transaction_amount BIGINT,PRIMARY KEY (MyIndex))")
        print("district_map_transaction_table is created....")
        for i,row in aggrtrans_map_db.iterrows():
            sql ="INSERT INTO phonepe_final.district_map_transaction_table VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,tuple(row))
            print("Record inserted")
            conn.commit() # connection is not autocommit so we do manually
except Error as e:
    print("Error while connecting to MySQL",e)

# district_map_registering_table

# C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/csv/AggTrans_mapuser_data.csv

aggrtans_mapuser_db = pd.read_csv('C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/csv/AggTrans_mapuser_data.csv',index_col=False)
print(aggrtans_mapuser_db.head()) 

# Select database and import the data of CSV content 
try:
    conn = mysql.connect(host='localhost',database='phonepe_final',user='root',password="Ranjani@15",auth_plugin="mysql_native_password")
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("You are connected to database: ",record)
        cursor.execute('DROP TABLE IF EXISTS district_map_registering_table;')
        print('Creating table...')
        cursor.execute("CREATE TABLE district_map_registering_table(MyIndex INT NOT NULL,State LONGTEXT,Year INT,Quater INT,District VARCHAR(50),Registered_user BIGINT,App_opening BIGINT,PRIMARY KEY (MyIndex))")
        print("district_map_registering_table is created....")
        for i,row in aggrtans_mapuser_db.iterrows():
            sql ="INSERT INTO phonepe_final.district_map_registering_table VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,tuple(row))
            print("Record inserted")
            conn.commit() # connection is not autocommit so we do manually
except Error as e:
    print("Error while connecting to MySQL",e)



# longitude_latitude_state_table

# C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/csv/Longitude_Latitude_State_Table.csv

Dist_db = pd.read_csv('C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/csv/Longitude_Latitude_State_Table.csv',index_col=False)
print(Dist_db.head()) 

# Select database and import the data of CSV content 
try:
    conn = mysql.connect(host='localhost',database='phonepe_final',user='root',password="Ranjani@15",auth_plugin="mysql_native_password")
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("You are connected to database: ",record)
        cursor.execute('DROP TABLE IF EXISTS longitude_latitude_state_table;')
        print('Creating table...')
        cursor.execute("CREATE TABLE longitude_latitude_state_table(MyIndex INT NOT NULL,code LONGTEXT,Latitude DOUBLE, Longitude DOUBLE, State LONGTEXT,PRIMARY KEY (MyIndex))")
        print("longitude_latitude_state_table is created....")
        for i,row in Dist_db.iterrows():
            sql ="INSERT INTO phonepe_final.longitude_latitude_state_table VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(sql,tuple(row))
            print("Record inserted")
            conn.commit() # connection is not autocommit so we do manually
except Error as e:
    print("Error while connecting to MySQL",e)


# districts_longitude_latitude_table

# C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/csv/Data_Map_Districts_Longitude_Latitude.csv

State_db = pd.read_csv('C:/Users/admin/Desktop/sivaranjani/DATA SCIENCE/project/phonepe/csv/Data_Map_Districts_Longitude_Latitude.csv',index_col=False)
print(State_db.head()) 

# Select database and import the data of CSV content 
try:
    conn = mysql.connect(host='localhost',database='phonepe_final',user='root',password="Ranjani@15",auth_plugin="mysql_native_password")
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("You are connected to database: ",record)
        cursor.execute('DROP TABLE IF EXISTS districts_longitude_latitude_table;')
        print('Creating table...')
        cursor.execute("CREATE TABLE districts_longitude_latitude_table(MyIndex INT NOT NULL,State LONGTEXT,District LONGTEXT,Latitude DOUBLE, Longitude DOUBLE,PRIMARY KEY (MyIndex))")
        print("districts_longitude_latitude_table is created....")
        for i,row in State_db.iterrows():
            sql ="INSERT INTO phonepe_final.districts_longitude_latitude_table VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(sql,tuple(row))
            print("Record inserted")
            conn.commit() # connection is not autocommit so we do manually
except Error as e:
    print("Error while connecting to MySQL",e)





