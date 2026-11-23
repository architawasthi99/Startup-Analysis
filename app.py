
import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Startup Funding Analysis",
    page_icon="📊",
    layout="wide"
)

df = pd.read_csv('startup_funding.csv')

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-color: #0E1117;
    }

    [data-testid="stSidebar"] {
        background-color: #161B22;
    }

    .main-title {
        font-size: 38px;
        font-weight: 800;
        color: #FFFFFF;
        margin-bottom: 5px;
    }

    .sub-title {
        color: #9CA3AF;
        font-size: 15px;
        margin-bottom: 30px;
    }

    div[data-testid="stMetric"] {
        background-color: #1C2333;
        border: 1px solid #303B50;
        padding: 20px;
        border-radius: 12px;
    }

    div.stButton > button {
        background-color: #6366F1;
        color: white;
        border-radius: 8px;
        border: none;
        width: 100%;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background-color: #4F46E5;
        color: white;
    }
</style>
""", unsafe_allow_html=True)


# Sidebar
st.sidebar.markdown("# 📊 Startup Analytics")
st.sidebar.caption("Explore India's startup funding ecosystem")

st.sidebar.divider()

options = st.sidebar.selectbox(
    "Select Analysis",
    ['Overall Analysis', 'Startup Analysis', 'Investor Analysis']
)


# Overall Analysis
if options == 'Overall Analysis':

    st.markdown('<div class="main-title">📈 Overall Analysis</div>',
                unsafe_allow_html=True)

    st.markdown(
        '<div class="sub-title">A complete overview of startup funding data</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Records", f"{df.shape[0]:,}")
    col2.metric("Total Startups", f"{df['Startup'].nunique():,}")
    col3.metric("Total Investors", f"{df['Investors'].nunique():,}")

    st.divider()

    st.subheader("Dataset Preview")
    st.dataframe(df, use_container_width=True, height=400)


# Startup Analysis
elif options == 'Startup Analysis':

    st.markdown('<div class="main-title">🚀 Startup Analysis</div>',
                unsafe_allow_html=True)

    st.markdown(
        '<div class="sub-title">Explore funding details of individual startups</div>',
        unsafe_allow_html=True
    )

    startup = st.sidebar.selectbox(
        "Select Startup",
        sorted(df['Startup'].dropna().unique().tolist())
    )

    btn1 = st.sidebar.button("🔍 Search Startup")

    if btn1:
        st.success(f"Showing analysis for {startup}")

        temp_df = df[df['Startup'] == startup]

        st.subheader(f"📌 {startup}")

        st.metric("Total Funding Records", len(temp_df))

        st.subheader("Funding Details")
        st.dataframe(temp_df, use_container_width=True)


# Investor Analysis
else:

    st.markdown('<div class="main-title">💼 Investor Analysis</div>',
                unsafe_allow_html=True)

    st.markdown(
        '<div class="sub-title">Explore investments made by individual investors</div>',
        unsafe_allow_html=True
    )

    investor = st.sidebar.selectbox(
        "Select Investor",
        sorted(df['Investors'].dropna().unique().tolist())
    )

    btn2 = st.sidebar.button("🔍 Search Investor")

    if btn2:
        st.success(f"Showing analysis for {investor}")

        temp_df = df[df['Investors'] == investor]

        st.subheader(f"📌 {investor}")

        st.metric("Total Funding Records", len(temp_df))

        st.subheader("Investment Details")
        st.dataframe(temp_df, use_container_width=True)
