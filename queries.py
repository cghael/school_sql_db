# Find students who are in 3rd grade and have 5 points for all their courses. 
# The output should consist of the student names only in alphabetical order.


best_student = "
SELECT name
FROM Students
JOIN (
    SELECT student_id, AVG(result) AS r
    FROM Student_Subject
    WHERE semester = 3
    GROUP BY student_id
    HAVING r = 5
) AS subquery
ON Students.student_id = subquery.student_id
ORDER BY name;"


# Find four students with the most achievement points and list their names in alphabetical order with their scores. 
# The student's year is not critical. The output should have only the name and the bonus point column. 
# The output should be in descending order of the bonus point column.


achievement_point = "
SELECT name, s AS 'bonus point'
FROM Students
JOIN (
    SELECT student_id, sum(bonus) AS s
    FROM Student_Achievement
    JOIN Achievement
        ON Student_Achievement.achievement_id = Achievement.achievement_id
    GROUP BY student_id
    ORDER BY s DESC
    LIMIT 4
) AS subquery
ON Students.student_id = subquery.student_id
ORDER BY s DESC;"


# If the student's average is over 3.5 points for courses, output above average in the best column. 
# Otherwise, print below average. Order the results in alphabetical order by name.


average_student = "
SELECT name, CASE 
                WHEN AVG(result) > 3.5 THEN 'above average'
                ELSE 'below average'
             END AS best
FROM Students
JOIN Student_Subject
    ON Students.student_id = Student_Subject.student_id
GROUP BY name;"


# You have to find the best students. 
# The course averages of these students are above 4.5 points. 
# The result should be in ascending order by name, with their names and which department they are in.


best_of_department = "
SELECT name, department_name 
FROM Students
JOIN Department 
    ON Students.department_id = Department.department_id
JOIN (
    SELECT student_id, AVG(result) as r
    FROM Student_Subject
    GROUP BY student_id 
    HAVING r > 4.5
) AS subquary
ON Students.student_id = subquary.student_id
ORDER BY name;"
