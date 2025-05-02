import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Titanic_Analysis & Classification"
                   ,page_icon="Zyad 👋"
                   ,layout="wide"
                   ,initial_sidebar_state="expanded")

with st.sidebar:
    cat_filter=st.selectbox("Cat_filter",["Sex","Survived"])
    num_filter=st.selectbox("Num_filter",["Fare","Age","Pclass","Embarked"])

    st.markdown(
     """
        <div style="display: flex; gap: 20px; align-items: center;">
         <a href="https://www.linkedin.com/in/zyad-sakoury-135405261/" target="_blank">
              <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="40"/>
            </a>
            <a href="https://www.facebook.com/zyad.ahmedsakoury" target="_blank">
             <img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" alt="Facebook" width="40"/>
         </a>
        </div>
        """,
        unsafe_allow_html=True
    )

 
df=pd.read_csv("titanc_passenger.csv")  
Passenger_Count=df.count()[0]
Count_Not_Survived=df[df["Survived"]=="No"]["Survived"].value_counts()[0]
Count_Survived=df[df["Survived"]=="Yes"]["Survived"].value_counts()[0]
avg_age=df["Age"].mean().round(2)
avg_fare=df["Fare"].mean().round(2)
c1,c2,c3,c4,c5=st.columns(5)
with c1 :
    st.metric("Passenger_Count",Passenger_Count) 
with c2 :
    st.metric("Passenger_Drowned",Count_Not_Survived)
with c3 :
    st.metric("Passenger_Survived",Count_Survived)
with c4:
    st.metric("Avg_Age",avg_age)
with c5:
    st.metric("Avg_Fare_Of_Ticket",avg_fare)
col1,col2=st.columns(2)
with col1:
    ch0=px.bar(df,x=df["Survived"],title="Num_Of_Survived",color=cat_filter)
    st.plotly_chart(ch0)
    ch2=px.pie(df,df["Pclass"],values=num_filter,title="Fare_by_Pclass")
    st.plotly_chart(ch2)


with col2:
    ch1=px.scatter(df,x=df["Age"],y=df["Fare"],title="Age & Fare",color=num_filter)
    st.plotly_chart(ch1)
    
    ch3=px.histogram(df,df["Age"],color=num_filter,title="Distrbution_Age")
    st.plotly_chart(ch3)


