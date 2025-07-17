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

    /* Use this to center the glass-box on screen */
    .glass-container {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
    }

    .glass-box {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border-radius: 20px;
        padding: 30px;
        width: 90%;
        max-width: 600px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }

    h1, label, .stNumberInput label, .stSelectbox label, .stMarkdown, .stTextInput label {
        color: white !important;
    }

    .stButton > button {
        background-color: rgba(255, 255, 255, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.3);
        color: white;
        font-weight: bold;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background-color: rgba(255, 255, 255, 0.4);
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# Begin the layout: glass container + box
st.markdown('<div class="glass-container"><div class="glass-box">', unsafe_allow_html=True)

# Now put ALL Streamlit widgets inside this area
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

# Close the glass container
st.markdown('</div></div>', unsafe_allow_html=True)
