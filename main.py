import streamlit as st
import pandas as pd
#import mysql.connector as mysql 
import plotly.express as px

#placeholder = st.empty()
# -------------------------------------------------- Mysql server connection using mysql connect ---------------------------------------------

#connection = mysql.connect(host='localhost',database='phonepe_final',user='root',password="Ranjani@15",auth_plugin="mysql_native_password")

# ---------------------------------------------------- Fetching datas from Mysql using pandas -----------------------------------------------

#query1 = 'select * from aggtrans_data'
#df = pd.read_sql(query1, con=connection)
#query2 = 'select * from longitude_latitude_state_table'
#state = pd.read_sql(query2, con=connection)
#query3 = 'select * from data_map_districts_longitude_latitude'
#districts = pd.read_sql(query3, con=connection)
#query4 = 'select * from aggtrans_map_data'
#districts_tran = pd.read_sql(query4, con=connection)
#query5 = 'select * from aggtrans_mapuser_data'
#app_opening = pd.read_sql(query5, con=connection)
#query6 = 'select * from aggtrans_user_data'
#user_device = pd.read_sql(query6, con=connection)

# ------------------------------------------ Date preparation for geo-visualization map -----------------------------------------------------------

# Create map
#st.snow()

# --------------------------------------- use this block and comment out previous to use data directly --------------------------------------
# --------------------------------------- use this block and comment out previous to use data directly --------------------------------------

# D:\Guvi\projects\Project 2 Phonepe pluse Data Visualization & exploration\pulse\csv\Agg_Trans.csv

# https://raw.githubusercontent.com/sivaranjani9715/Phonepe/main/csv/AggTrans_data.csv
# https://raw.githubusercontent.com/sivaranjani9715/Phonepe/main/csv/AggTrans_mapuser_data.csv
# https://raw.githubusercontent.com/sivaranjani9715/Phonepe/main/csv/AggTrans_user_data.csv
# https://raw.githubusercontent.com/sivaranjani9715/Phonepe/main/csv/Data_Map_Districts_Longitude_Latitude.csv
# https://raw.githubusercontent.com/sivaranjani9715/Phonepe/main/csv/Longitude_Latitude_State_Table.csv
# https://raw.githubusercontent.com/sivaranjani9715/Phonepe/main/csv/district_map_transaction.csv

df = pd.read_csv('https://raw.githubusercontent.com/sivaranjani9715/Phonepe/main/csv/AggTrans_data.csv', index_col=0)
state = pd.read_csv('https://raw.githubusercontent.com/sivaranjani9715/Phonepe/main/csv/Longitude_Latitude_State_Table.csv')
districts = pd.read_csv('https://raw.githubusercontent.com/sivaranjani9715/Phonepe/main/csv/Data_Map_Districts_Longitude_Latitude.csv')
districts_tran = pd.read_csv('https://raw.githubusercontent.com/sivaranjani9715/Phonepe/main/csv/district_map_transaction.csv', index_col=0)
app_opening = pd.read_csv('https://raw.githubusercontent.com/sivaranjani9715/Phonepe/main/csv/AggTrans_mapuser_data.csv', index_col=0)
user_device = pd.read_csv(r'https://raw.githubusercontent.com/sivaranjani9715/Phonepe/main/csv/AggTrans_user_data.csv',index_col=0)



# ------------------------------------------ Date preparation for geo-visualization -----------------------------------------------------------
state = state.sort_values(by='state')
state = state.reset_index(drop=True)
df2 = df.groupby(['State']).sum()[['Transaction_count', 'Transaction_amount']]
df2 = df2.reset_index()

choropleth_data = state.copy()

for column in df2.columns:
    choropleth_data[column] = df2[column]
choropleth_data = choropleth_data.drop(labels='State', axis=1)

df.rename(columns={'State': 'state'}, inplace=True)
sta_list = ['andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
            'assam', 'bihar', 'chandigarh', 'chhattisgarh',
            'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
            'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
            'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
            'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
            'uttarakhand', 'west-bengal']
state['state'] = pd.Series(data=sta_list)
state_final = pd.merge(df, state, how='outer', on='state')
districts_final = pd.merge(districts_tran, districts,
                           how='outer', on=['State', 'District'])


# ------------------------------------------ Streamlit app Plot 1 Scatter plot of registered user and app opening ----------------------------

with st.container():
    st.title(':white[PhonePe Pulse Data Visualization(2018-2022)]')
    st.write(' ')
    st.subheader(
        ':white[Registered user & App installed -> State and Districtwise:]')
    st.write(' ')
    scatter_year = st.selectbox('Please select the Year',
                                ('2018', '2019', '2020', '2021', '2022'))
    st.write(' ')
    scatter_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                         'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                         'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                         'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                         'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                         'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                         'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                         'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                         'uttarakhand', 'west-bengal'), index=30)
    scatter_year = int(scatter_year)
    scatter_reg_df = app_opening[(app_opening['Year'] == scatter_year) & (
        app_opening['State'] == scatter_state)]
    scatter_register = px.scatter(scatter_reg_df, x="District", y="Registered_user",  color="District",
                                  hover_name="District", hover_data=['Year', 'Quater', 'App_opening'], size_max=60)
    st.plotly_chart(scatter_register)
st.write(' ')


# ------------------------------------- Streamlit Tabs for various analysis -----------------------------------------------------------------
geo_analysis, Device_analysis, payment_analysis, transac_yearwise = st.tabs(
    ["Geographical analysis", "User device analysis", "Payment Types analysis", "Transaction analysis of States"])
# ------------------------------------------- Geo-analysis ----------------------------------------------------------------------------------
with geo_analysis:
    st.subheader(':white[Transaction analysis->State and Districtwise:]')
    st.write(' ')
    Year = st.radio('Please select the Year',
                    ('2018', '2019', '2020', '2021', '2022'), horizontal=True)
    st.write(' ')
    Quarter = st.radio('Please select the Quarter',
                       ('1', '2', '3', '4'), horizontal=True)
    st.write(' ')
    Year = int(Year)
    Quarter = int(Quarter)
    plot_district = districts_final[(districts_final['Year'] == Year) & (
        districts_final['Quater'] == Quarter)]
    plot_state = state_final[(state_final['Year'] == Year)
                             & (state_final['Quater'] == Quarter)]
    plot_state_total = plot_state.groupby(
        ['state', 'Year', 'Quater', 'Latitude', 'Longitude']).sum()
    plot_state_total = plot_state_total.reset_index()
    state_code = ['AN', 'AD', 'AR', 'AS', 'BR', 'CH', 'CG', 'DNHDD', 'DL', 'GA',
                  'GJ', 'HR', 'HP', 'JK', 'JH', 'KA', 'KL', 'LA', 'LD', 'MP', 'MH',
                  'MN', 'ML', 'MZ', 'NL', 'OD', 'PY', 'PB', 'RJ', 'SK', 'TN', 'TS',
                  'TR', 'UP', 'UK', 'WB']
    plot_state_total['code'] = pd.Series(data=state_code)
    # ------------------------------------------- Geo-visualization of transacion data ------------------------------------------------------
    fig1 = px.scatter_geo(plot_district,
                          lon=plot_district['Longitude'],
                          lat=plot_district['Latitude'],
                          color=plot_district['Transaction_amount'],
                          size=plot_district['Transaction_count'],
                          hover_name="District",
                          hover_data=["State", 'Transaction_amount', 'Transaction_amount',
                                      'Transaction_count', 'Year', 'Quater'],
                          title='District',
                          size_max=22,)
    fig1.update_traces(marker={'color': "#CC0044",
                               'line_width': 1})
    fig2 = px.scatter_geo(plot_state_total,
                          lon=plot_state_total['Longitude'],
                          lat=plot_state_total['Latitude'],
                          hover_name='state',
                          text=plot_state_total['code'],
                          hover_data=['Transaction_count',
                                      'Transaction_amount', 'Year', 'Quater'],
                          )
    fig2.update_traces(marker=dict(color="#D5FFCC", size=0.3))
    fig = px.choropleth(
        choropleth_data,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='Transaction_amount',
        color_continuous_scale='twilight',
        hover_data=['Transaction_count', 'Transaction_amount']
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.add_trace(fig1.data[0])
    fig.add_trace(fig2.data[0])
    fig.update_layout(height=1000, width=1000)
    st.write(' ')
    st.write(' ')
    
#     if st.button('Click here to see map clearly'):
#         fig.show()
        
    st.plotly_chart(fig)


# --------------------------------------------------- Device analysis statewise ------------------------------------------------------------
with Device_analysis:
    st.subheader(':white[User Device analysis->Statewise:]')
    tree_map_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                         'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                         'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                         'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                         'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                         'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                         'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                         'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                         'uttarakhand', 'west-bengal'), index=30, key='tree_map_state')
    tree_map_state_year = int(st.radio('Please select the Year',
                                       ('2018', '2019', '2020', '2021', '2022'), horizontal=True, key='tree_map_state_year'))
    tree_map_state_quater = int(st.radio('Please select the Quarter',
                                         ('1', '2', '3', '4'), horizontal=True, key='tree_map_state_quater'))
    user_device_treemap = user_device[(user_device['State'] == tree_map_state) & (user_device['Year'] == tree_map_state_year) &
                                      (user_device['Quater'] == tree_map_state_quater)]
    user_device_treemap['Brand_count'] = user_device_treemap['Brand_count'].astype(str)

    # ----------------------------------------- Treemap view of user device ----------------------------------------------------------------
    user_device_treemap_fig = px.treemap(user_device_treemap, path=['State', 'Brand'], values='Brand_percentage', hover_data=['Year', 'Quater'],
                                         color='Brand_count',
                                         title='User device distribution in ' + tree_map_state +
                                         ' in ' + str(tree_map_state_year)+' at '+str(tree_map_state_quater)+' quater',)
    st.plotly_chart(user_device_treemap_fig)
    # ---------------------------------------- Barchart view of user device -----------------------------------------------------------------
    bar_user = px.bar(user_device_treemap, x='Brand', y='Brand_count', color='Brand',
                      title='Bar chart analysis', color_continuous_scale='sunset',)
    st.plotly_chart(bar_user)


# ----------------------------------------- Payment type analysis of Transacion data ----------------------------------------------------------
with payment_analysis:
    st.subheader(':white[Payment type Analysis -> 2018 - 2022:]')
    # querypa = 'select * from agg_transaction_table'
    # payment_mode = pd.read_sql(querypa, con=connection)
    payment_mode = pd.read_csv('https://raw.githubusercontent.com/sivaranjani9715/Phonepe/main/csv/AggTrans_data.csv', index_col=0)
    pie_pay_mode_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                         'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                         'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                         'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                         'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                         'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                         'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                         'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                         'uttarakhand', 'west-bengal'), index=30, key='pie_pay_mode_state')
    pie_pay_mode_year = int(st.radio('Please select the Year',
                                     ('2018', '2019', '2020', '2021', '2022'), horizontal=True, key='pie_pay_year'))
    pie_pay_mode__quater = int(st.radio('Please select the Quarter',
                                        ('1', '2', '3', '4'), horizontal=True, key='pie_pay_quater'))
    pie_pay_mode_values = st.selectbox(
        'Please select the values to visualize', ('Transaction_count', 'Transaction_amount'))
    pie_payment_mode = payment_mode[(payment_mode['Year'] == pie_pay_mode_year) & (
        payment_mode['Quater'] == pie_pay_mode__quater) & (payment_mode['State'] == pie_pay_mode_state)]
    # -------------------------------- Pie chart analysis of Payment mode --------------------------------------------------------------------
    pie_pay_mode = px.pie(pie_payment_mode, values=pie_pay_mode_values,
                          names='Transaction_type', hole=.5, hover_data=['Year'])
    # ------------------------------------- Bar chart analysis of payment mode ----------------------------------------------------------------
    pay_bar = px.bar(pie_payment_mode, x='Transaction_type',
                     y=pie_pay_mode_values, color='Transaction_type')
    st.plotly_chart(pay_bar)
    st.plotly_chart(pie_pay_mode)


# --------------------------------------- Transacion data analysis statewise ------------------------------------------------------------------
with transac_yearwise:
    st.subheader(':white[Transaction analysis->Statewise:]')
    transac_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                         'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                         'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                         'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                         'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                         'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                         'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                         'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                         'uttarakhand', 'west-bengal'), index=30, key='transac')
    transac__quater = int(st.radio('Please select the Quarter',
                                   ('1', '2', '3', '4'), horizontal=True, key='trans_quater'))
    transac_type = st.selectbox('Please select the Mode',
                                ('Recharge & bill payments', 'Peer-to-peer payments', 'Merchant payments', 'Financial Services', 'Others'), key='transactype')
    transac_values = st.selectbox(
        'Please select the values to visualize', ('Transaction_count', 'Transaction_amount'), key='transacvalues')
    payment_mode_yearwise = pd.read_csv('https://raw.githubusercontent.com/sivaranjani9715/Phonepe/main/csv/AggTrans_data.csv', index_col=0)

    # querypay_year = 'select * from agg_transaction_table'
    # payment_mode_yearwise = pd.read_sql(querypay_year, con=connection)

    new_df = payment_mode_yearwise.groupby(
        ['State', 'Year', 'Quater', 'Transaction_type']).sum()
    new_df = new_df.reset_index()
    chart = new_df[(new_df['State'] == transac_state) &
                   (new_df['Transaction_type'] == transac_type) & (new_df['Quater'] == transac__quater)]
    # ------------------------------- Bar chart analysis of transacion data statewise --------------------------------------------------------
    year_fig = px.bar(chart, x=['Year'], y=transac_values, color=transac_values, color_continuous_scale='armyrose',
                      title='Transaction analysis '+transac_state + ' regarding to '+transac_type)
    st.plotly_chart(year_fig)
