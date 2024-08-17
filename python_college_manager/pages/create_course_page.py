import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.title("Create course")
name = st.text_input('Course name')
start_date = st.date_input(label="Start date")
end_date = st.date_input(label="End date")
cut1_percentage = st.number_input(label="Cut 1 percentage")
cut2_percentage = st.number_input(label="Cut 2 percentage")
cut3_percentage = st.number_input(label="Cut 3 percentage")
submit = st.button("Submit")

if submit:
    st.write(f"Course name is: {name}")
    st.write(f"database name: {os.getenv("DB_NAME")}")
