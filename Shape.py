import streamlit as st
import time

st.header("Shapes Calculation")
st.sidebar.title("Configuration")


shape = st.selectbox("Choose Shape:", ["Circle", "Rectangle" ])
if shape == 'Circle':
    Radius = st.number_input('Radius:' , min_value=0.0, max_value= 1000.0, step=0.001)
    area = Radius**2*3.14
    perimeter = 2* 3.14* Radius
if shape== 'Rectangle':
    Width = st.number_input("Width", 0.,step=0.1)
    Height = st.number_input("Height", 0., step = 0.1) 
    area = Width * Height
    perimeter = 2 * (Width + Height)

compute_btn = st.button("compute Area and Perimeter") 
if compute_btn:
    with st.spinner("Computing..."):
        time.sleep(1)
        st.write("Area: ", area)
        st.write("perimeter: ", perimeter)
