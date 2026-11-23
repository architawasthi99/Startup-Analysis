import streamlit as st
import pandas as pd

email=st.text_input("enter your email")
password=st.text_input("enter your password",type="password")

gender=st.selectbox("select your gender",["male","female","other"])

btn=st.button('login')
if btn:
    if email=="archit2786@gmail.com" and password=="archit":
        #st.success("login success")
        st.balloons()
        st.write(gender)
    else:
        st.error("login failed")  

#file uploader
file=st.file_uploader("upload your file") 
if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df)