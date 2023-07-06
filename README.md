# Phonepe
Phonepe Pulse Data Visualization - Shows the Transactions, Registered user , Payment type detail of all states in India for year 2018-2022

Phonepe Pulse Data Visualization and Exploration

live geo visualization dashboard with information displayed about Phonepe pulse with interactive and appealing manner with 10 different dropdown which user can select facts to display and data will be stored in MySQL database for efficient retrieval of data and dashboard will be dynamically updated the latest data

Installation

To use this app, you need to have Python 3.x installed on your system, as well as the following Python packages: • streamlit • pandas • mysql-connector-python • plotly

Step 1

GitHub cloning repository
GitHub cloning repository by Git Bash

open the repository in GitHub which you need to clone it click on code dropdown and select https copy the link given at https section

Create new folder to store the repository

create the folder where you need to store the github repository and open the folder right click on mouse then select Git Bash here then type git clone in that application it will start downloading the repository which you need as local repository after downloading you can work on it without changing in main original repository

GitHub cloning repository by Visual Studio

open the repository in GitHub which you need to clone it click on code dropdown and select https copy the link given at https section

Click on Source control and click on clone repository and paste the URL

Step 2

Tranforming the data into sutable format
transform the data as csv by extracting the json file by giving the path and create data frame for extract the content in the table by using for loop

store the csv file in same path of your project

Step 3

Load csv file data to mysql
import all required libraries in python IDE

create connection to mysql by mysql.connector

create new database, create tables and store the csv file content in the database

Step 4

Create streamlit dashboard
create the streamlit dash with options for selecting year and state

when your choose the year and state then dashboard should show the relevant transaction count and other details in map and bar graph

Step 5

Extract data from mysql to streamlit dashboard
import required library and connect to mysql database

extract the content of the table and show it dashboard

main page project recording video with radio button to show video Registered user detail plot graph with year and state selection dashboard as total 4 tabs

Geographical analysis
when user select the year, state and quarter then it show update the data in India map and when mouse point place on any state then it will show the transaction count , latitude , longitude other details

User device analysis
when user select the year, state and quarter then it show detail of brand count , brand percentage and phone brand name as bar graph

Payment type analysis
when user select the year,state and quarter show the detail of transactions count and transactions amount with all payment type as bar graph

Transactions analysis
when user select the year,state and quarter and transaction type this gives the transaction count of 5 years

Streamlit deploy
for deploy this app in streamlit click on menu at right side corner then click on deploy this will ask to push the main py to github

push the python file to github and again select deploy

this will show the option to select the repository amd main file then click on deploy

then this will deploy app in streamlit

Demo video - [https://drive.google.com/file/d/1Lq1c0TxttqLBhe0mdxXEq7p-xIbr6QXt/view?usp=sharing](https://drive.google.com/file/d/1Lq1c0TxttqLBhe0mdxXEq7p-xIbr6QXt/view?usp=sharing)
