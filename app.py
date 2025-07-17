import streamlit as st
import requests

st.markdown("""
    <style>
    .stApp {
        background-image: url("https://i.pinimg.com/1200x/04/7b/3f/047b3f4517839ef37e4044a6218ff8c8.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
""", unsafe_allow_html=True)
st.sidebar.title("Choose Trend")


st.sidebar.markdown(''' 
background: rgba(45, 41, 41, 0.24);
border-radius: 16px;
box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
backdrop-filter: blur(5.8px);
-webkit-backdrop-filter: blur(5.8px);
border: 1px solid rgba(45, 41, 41, 0.2);
''',unsafe_allow_html=True)


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
