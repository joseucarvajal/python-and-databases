import streamlit as st
import pandas as pd

def extract_students_from_excel(excel_file):
    """Extracts student information from the provided Excel file."""
    try:
        df = pd.read_excel(excel_file)
    except Exception as e:
        st.write(f"Error reading the Excel file: {e}")
        return []

    df = df.rename(columns={
        'Código': 'code',
        'Nombre': 'first_name',
        'Apellidos': 'last_name',
        'Email': 'email',
        'Email Institucional': 'institutional_email'
    })

    df['code'] = df['code'].astype(str)
    df['fullName'] = df['first_name'] + ' ' + df['last_name']
    df['emails'] = df['email'] + ',' + df['institutional_email']

    df = df[['code', 'fullName', 'emails']]

    st.write(df)

    #students = [Student(**record) for record in df.to_dict(orient='records')]

    #return students


st.title("Upload students attendance list Excel file")

uploaded_file = st.file_uploader("Attendance list Excel file", type=["xls", "xlsx"])
if uploaded_file is not None:
    extract_students_from_excel(uploaded_file)
    st.write("Se ha cargado el archivo con exito")