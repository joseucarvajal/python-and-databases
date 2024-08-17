import streamlit as st
import os

st.title("Create course")
name = st.text_input('Course name')
start_date = st.date_input(label="Start date")
end_date = st.date_input(label="End date")
cut1_percentaje = st.number_input(label="Cut 1 percentaje")
cut2_percentaje = st.number_input(label="Cut 2 percentaje")
cut3_percentaje = st.number_input(label="Cut 3 percentaje")
submit = st.button("Submit")

if submit:
    st.write(f"Course name is: {name}")
    st.write(f"database name: {os.getenv("DB_NAME")}")
