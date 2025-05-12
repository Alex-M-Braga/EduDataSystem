
SELECT 
    s.full_name,
    COUNT(a.attendance_id) AS total_records,
    SUM(CASE WHEN a.status = 'Present' THEN 1 ELSE 0 END) AS total_present,
    SUM(CASE WHEN a.status = 'Absent' THEN 1 ELSE 0 END) AS total_absent
FROM students s
LEFT JOIN attendance a ON s.student_id = a.student_id
GROUP BY s.full_name;
