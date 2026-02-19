import streamlit as st
import requests

amount = st.number_input("Enter BDT : ", min_value=1)

target_currency = st.selectbox("Convert to ", ['USD', 'INR', 'EUR','LAK'])

if st.button("Convert"):
  url = "https://api.exchangerate-api.com/v4/latest/BDT"

  response = requests.get(url)

  if response.status_code == 200:
    data = response.json()

    target_currency_rate = data["rates"][target_currency]
    covert_currency = target_currency_rate * amount

    st.success(f"{amount} BDT = {round(covert_currency, 2)}")

  else:
    st.error("Failed to fetch conversion rate")