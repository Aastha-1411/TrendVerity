import streamlit as st
import time

st.set_page_config(
    page_title="TrendVerity", layout="centered"
)

full_text = ":blue[TrendVerity] - Insights Made Simple"
words = full_text.split()
placeholder = st.empty()

display_text = ""
for word in words:
    display_text += word + " "
    placeholder.markdown(f"# {display_text}")
    time.sleep(0.4)  # Adjust the speed as needed

# Optionally, show the final text in case of refresh
placeholder.markdown(f"# {full_text}")