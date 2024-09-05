import streamlit as st 

st.title('Calculator')
num1=st.number_input('Angka 1')
operator=st.selectbox('Operator',['+','-','*','/'])
num2=st.number_input('Angka 2')
sama_dengan=st.button('=')
st.write('Hasil')
