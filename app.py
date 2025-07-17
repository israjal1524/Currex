import streamlit as st
import requests

st.title("CUREX")
amount=st.number_input("Enter the Amount of Exchang in INR",min_value=1)
target_currency=st.selectbox("Exchange to currency",["USD","CAD","PKR","JPY","EUR"])
if st.button("convert"):
     url="https://api.exchangerate-api.com/v4/latest/INR"
     response= requests.get(url)

     if response.status_code ==200:
        data =response.json()
        rate=data["rates"][target_currency]
        converted =rate*amount
        st.success(f"{amount} INR={converted:.2f}{target_currency}")
        pass
     else:
         st.error("Failed to fetch")
