import pandas as pd
import streamlit as st
import plotly.express as px #pip install plotly-express]

st.set_page_config(page_title='My Sale Dashboard',page_icon=':bar_chart:',layout='wide')

df=pd.read_csv('alldf.csv')

st.sidebar.header('Please filter here')

product=st.sidebar.multiselect("Select product: ",
                      options=df['Product'].unique(),
                      default=df['Product'].unique()[:5]
                      )

city=st.sidebar.multiselect("Select City: ",
                      options=df['City'].unique(),
                      default=df['City'].unique()[:5])

month=st.sidebar.multiselect("Select Month: ",
                      options=df['Order_month'].unique(),
                      default=df['Order_month'].unique()[:5])

st.title(":bar_chart:  Sales Dashbord for 2019")
st.markdown('##')

total_sale=df['Total_sale'].sum()
product_num=df['Product'].nunique()


left_col,right_col=st.columns(2)

with left_col:
    st.subheader('TOtal Sales')
    st.subheader(f"US $ {total_sale}")
    
with right_col:
    st.subheader('Number of Product')
    st.subheader(f"{product_num}")

df_select=df.query('City==@city and Order_month==@month and Product==@product')

sale_by_product=(df_select.groupby('Product')['Total_sale'].sum().sort_values(ascending=False))

fig_product_sales =px.bar(
    sale_by_product,
    x=sale_by_product.values,
    y=sale_by_product.index,
    orientation='h',
    title='Sales by product line'
)

#
sale_city_pie= px.pie(df_select,values='Total_sale',names='City',title='Sales of City')

#sale_city_pie =px.pie(
  #df_select,values='Total_sale', names='City'
    #x=sale_by_month_pie.values,
 
    #title='Sales by city'
#)
#fig = px.pie(df, values='pop', names='country', title='Population of European continent')
#sale_city_pie.show()

sale_by_month=(df_select.groupby('Order_month')['Total_sale'].sum().sort_values(ascending=False))

fig_month_sales =px.bar(
    sale_by_month,
    x=sale_by_month.values,
    y=sale_by_month.index,
    title='Sales by month'
)

a_col,b_col,c_col=st.columns(3)

a_col.plotly_chart(fig_product_sales,use_container_width=True)
c_col.plotly_chart(fig_month_sales,use_container_width=True)
b_col.plotly_chart(sale_city_pie,use_container_width=True)
#c_col.plotly_chart(sale_by_month_pie,use_container_width=True)

#c-col -- sales by month - bar chart

l_col,r_col=st.columns(2)

#fig1=px.line(df,x=sale_by_month.index,y=sale_by_month.values, title='Sales by Month')
#r_col.plotly_chart(fig1,use_container_width=True)

df1=df.query('Order_month==@month')
vv=df1.groupby('Order_month')['Total_sale'].sum()
fig=px.line(df,x=vv.index, y=vv.values, title='Sales by Month')
r_col.plotly_chart(fig,use_container_width=True)


fig2=px.scatter(df,x='Total_sale',y='Quantity Ordered', title='Sales and Item amount')

l_col.plotly_chart(fig2,use_container_width=True)






