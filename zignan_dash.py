import pandas as pd
import streamlit as st
import seaborn as sns

search = st.sidebar.radio("HOME",('home','about'))

col1,col2,col3=st.columns([4,5,3])
with col2:
     st.title('''Zignan AI''')
with col1:
    pass
with  col3:
    pass

idd='1bsWbyZbw0nZzH5XwwjTB3l88gZBhKE1WQ_iDDk1IaWs'
#idd1=st.sidebar.text_input("ENTER THE Sheet ID",'1bsWbyZbw0nZzH5XwwjTB3l88gZBhKE1WQ_iDDk1IaWs')
df=pd.read_csv(f"https://docs.google.com/spreadsheets/d/{idd}/export?format=csv")
st.dataframe(df)


