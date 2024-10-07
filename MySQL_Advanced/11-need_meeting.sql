-- Creating view with specific parameters
-- Student scores below 80 with no recent last_meeting dates

CREATE VIEW need_meeting AS
-- Select name column from students table
SELECT name
FROM students
WHERE
    score < 80
    AND (
        last_meeting IS NULL -- No last_meeting on record
        OR last_meeting < CURDATE() - INTERVAL 1 MONTH -- last_meeting was more than a month ago
    );