
-- EduDataSystem Initialization Script
-- Author: Alex de Moraes Braga

CREATE TABLE students (
    student_id NUMBER PRIMARY KEY,
    full_name VARCHAR2(100),
    date_of_birth DATE,
    grade_level VARCHAR2(20),
    address VARCHAR2(255),
    geo_zone VARCHAR2(100),
    emergency_contact VARCHAR2(100),
    special_needs VARCHAR2(255),
    transport_method VARCHAR2(50),
    authorized_pickups VARCHAR2(255),
    observations CLOB
);

CREATE TABLE attendance (
    attendance_id NUMBER PRIMARY KEY,
    student_id NUMBER,
    attendance_date DATE,
    status VARCHAR2(10),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

CREATE TABLE grades (
    grade_id NUMBER PRIMARY KEY,
    student_id NUMBER,
    subject VARCHAR2(50),
    term VARCHAR2(20),
    score NUMBER,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

CREATE TABLE emergency_info (
    student_id NUMBER PRIMARY KEY,
    emergency_details VARCHAR2(255),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

CREATE TABLE special_support (
    support_id NUMBER PRIMARY KEY,
    student_id NUMBER,
    condition VARCHAR2(100),
    recommended_action VARCHAR2(255),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
