-- Script para crear la base de datos y las tablas necesarias

CREATE DATABASE IF NOT EXISTS college_manager;

USE professor_assistant_db;

-- Tabla para almacenar la información del curso
CREATE TABLE IF NOT EXISTS courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    cut1_percentage FLOAT NOT NULL,
    cut2_percentage FLOAT NOT NULL,
    cut3_percentage FLOAT NOT NULL
);

-- Tabla para almacenar la lista de estudiantes
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    emails VARCHAR(255) NOT NULL,
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
);
