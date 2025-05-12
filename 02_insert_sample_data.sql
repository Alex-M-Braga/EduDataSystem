
INSERT INTO students (student_id, full_name, date_of_birth, grade_level, address, geo_zone, emergency_contact, special_needs, transport_method, authorized_pickups, observations)
VALUES (1, 'Alanis Braga', TO_DATE('2017-05-22', 'YYYY-MM-DD'), '1st Grade', '123 School St', 'Zone A', 'Patricia Braga - 8570001111', 'Autism - Needs family support', 'School Bus', 'Patricia Braga, Alex Braga', 'No major allergies. Prefers visual learning.');

INSERT INTO attendance (attendance_id, student_id, attendance_date, status)
VALUES (1, 1, TO_DATE('2025-05-06', 'YYYY-MM-DD'), 'Present');

INSERT INTO grades (grade_id, student_id, subject, term, score)
VALUES (1, 1, 'Mathematics', 'Q1', 89);
