import streamlit as st 

st.title('BMI Calculator')

height = st.number_input('Enter Height')


weight = st.number_input('Enter Weight')

calculate = st.button('Calculate BMI')

if(calculate):
    bmi = weight/height**2*10000
    if(bmi<18):
        st.title(f'BMI : {bmi}. You are underweight')
    elif(bmi>18 and bmi<=20):
         st.title(f'BMI : {bmi}. You are Normal Weight')
    else:
        st.title(f'BMI : {bmi}. You are Over Weight')
