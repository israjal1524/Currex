import streamlit as st
import requests

# Inject background + styling
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://i.pinimg.com/1200x/04/7b/3f/047b3f4517839ef37e4044a6218ff8c8.jpg");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }
""", unsafe_allow_html=True)

st.title(" CURREX")

amount = st.number_input("Enter the Amount of Exchange in INR", min_value=1)
target_currency = st.selectbox("Exchange to currency", ["USD", "CAD", "PKR", "JPY", "EUR"])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][target_currency]
        converted = rate * amount
        st.success(f"{amount} INR = {converted:.2f} {target_currency}")
    else:
        st.error(" Failed to fetch exchange rates.")

