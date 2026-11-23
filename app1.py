import streamlit as st
import numpy as np
import pandas as pd

df=pd.read_csv('startup_funding.csv')

st.sidebar.markdown("# 📊 Startup Analytics")
st.sidebar.caption("Explore India's startup funding ecosystem")
st.sidebar.divider()

options=st.sidebar.selectbox(
    "Select one",
    ['Overall Analysis','Startup Analysis','Investor Analysis']
)

if options=='Overall Analysis':
    st.title("Overall Analysis")
elif options=='Startup Analysis':
    st.sidebar.selectbox("Select Startup",sorted(df['Startup'].unique().tolist()))
    btn1=st.sidebar.button("Search")
    st.title("Startup Analysis")
else:
    st.sidebar.selectbox("Select Investor",sorted(df['Investors'].unique().tolist()))
    btn2=st.sidebar.button("Search")
    st.title("Investor Analysis")
