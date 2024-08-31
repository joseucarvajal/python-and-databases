import streamlit as st
import pandas as pd
from course_db_helper import get_all_the_courses
from student_db_helper import insert_students_in_bulk

st.title("Upload students")

def extract_students_from_excel(excel_file, course_id):
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

    insert_students_in_bulk(df, course_id, table_name='students')
    
    st.write(df)

# Obtener los cursos
courses = get_all_the_courses()

# Crear un diccionario para mapear IDs de cursos a sus nombres
course_dict = {course['id']: course['name'] for course in courses}
course_ids = list(course_dict.keys())

# Crear el dropdown con los IDs como valor de selección y los nombres como valor de visualización
selected_course_id = st.selectbox("Select a course", course_ids, format_func=lambda id: course_dict[id])

# Subir el archivo de Excel
uploaded_file = st.file_uploader("Attendance list Excel file", type=["xls", "xlsx"])

# Botón para procesar la carga y mostrar los valores
if st.button("Save students"):
    if uploaded_file is not None:
        extract_students_from_excel(uploaded_file, selected_course_id)
        st.write("Students have been created successfully")
    