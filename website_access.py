import streamlit as st
import requests

def fetch_data(card_number, year):
    # Example URL, you need to adjust it to the real one
    url = f"https://app.semovi.cdmx.gob.mx/MI_movilidad/trazabilidad?card_number={card_number}&year={year}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

# Streamlit interface
st.title("Card Information Retrieval")

card_number = st.text_input("Enter the card number")
year = st.number_input("Enter the year", min_value=2000, max_value=2100, step=1)

if st.button("Get Information"):
    if card_number and year:
        data = fetch_data(card_number, year)
        if data:
            st.write("Data retrieved:", data)
        else:
            st.write("Failed to retrieve data.")
    else:
        st.write("Please provide both card number and year")
