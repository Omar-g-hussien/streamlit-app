import streamlit as st
import pandas as pd 
import plotly.express as px 
import numpy as np

# save the data to cache
@st.cache_data
def load_data(file):
    return pd.read_csv(file)
file = st.file_uploader("Upload File", type=["csv"])
if file is not None:
    df= load_data(file)
    n_rows = st.slider('Choose number of rows to display', min_value=2, 
                       max_value= len(df), step=1)
    
    columns= st.multiselect("select columns to show", 
                            df.columns, default=df.columns)
    
    st.write(df[:n_rows][columns])
    tab1, tab2 =st.tabs(["Scatter Plot", "Histogram"])
    with tab1:
        # User selection for X and Y axes
        col1, col2, col3= st.columns(3)
        with col1:
            x_axis = st.selectbox("Select X-axis Column", df.select_dtypes("number").columns)
        with col2:
            y_axis = st.selectbox("Select Y-axis Column", df.select_dtypes("number").columns)
        with col3:
            color = st.selectbox("Select column to be color", df.columns)
        # Generate Scatter Plot
        fig = px.scatter(df, x=x_axis, y=y_axis, title="Customizable Scatter Plot", color=color)
        st.plotly_chart(fig)
    with tab2: 
        # Generating Histogram
        histogram_feature = st.selectbox("Select a column for the histogram:", df.select_dtypes("number").columns)
        fig_hist = px.histogram(df, x=histogram_feature, title=f"Histogram of {histogram_feature}")
        st.plotly_chart(fig_hist)