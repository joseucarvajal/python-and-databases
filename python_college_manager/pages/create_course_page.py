import os
import streamlit as st
import mysql.connector
from mysql.connector import Error


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
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)

            query = """
            INSERT INTO courses (name, start_date, end_date, cut1_percentage, cut2_percentage, cut3_percentage)
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            values = (
                name,
                start_date,
                end_date,
                cut1_percentage,
                cut2_percentage,
                cut3_percentage
            )

            cursor.execute(query, values)
            connection.commit()

            cursor.close()

            st.write("The course has been successfully saved")

    except Error as e:
        st.error("Error connecting to database")
        connection = None
