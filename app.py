import streamlit as st
import requests

st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1502920514313-52581002a659?crop=entropy&cs=srgb&fm=jpg&ixid=M3wyMTU1fDB8MXxzZWFyY2h8OXx8bW9uZXklMjB8ZW58MHx8fHwxNzUyNzc1ODE2fDA&ixlib=rb-4.1.0&q=85");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
""", unsafe_allow_html=True)

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
